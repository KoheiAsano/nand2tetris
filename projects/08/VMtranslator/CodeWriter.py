from sys import argv
import os
from CommandType import CommandType

class CodeWriter:
    def __init__(self, name):
        if os.path.isdir(name):
            self.out = open(name.split(".")[0] + "/" + name.split("/")[-1] + ".asm", "w")
        else:
            self.out = open(name.split(".")[0] + ".asm", "w")
        self.fn = ""
        # fn と合わせてloop labelを区別するためのindex
        self.lc = 0
        # return address一意のためのカウンタ
        self.rc = 0
        # 本文中 writeInitの処理
        self.out.write("//init\n")
        self.out.write("\t@256\n")
        self.out.write("\tD=A\n")
        self.out.write("\t@SP\n")
        self.out.write("\tM=D\n")
        self.out.write("\t@Sys.init\n")
        self.out.write("\t0;JMP\n")
        self.out.write("//initend\n")

    def setFileName(self, fileName):
        self.fn = fileName.split("/")[-1][:-3]
        self.lc = 0
        return
    # 二項演算のアセンブリ生成
    def gen_bin(self, op):
        # 1pop
        self.out.write("\t@SP\n")
        self.out.write("\tM=M-1\n")
        self.out.write("\tA=M\n")
        self.out.write("\tD=M\n")
        # 2pop
        self.out.write("\t@SP\n")
        self.out.write("\tM=M-1\n")
        self.out.write("\tA=M\n")
        # 処理
        self.out.write("\tD=M"+ op + "D\n")
        # push
        self.out.write("\t@SP\n")
        self.out.write("\tM=M+1\n")
        self.out.write("\tA=M-1\n")
        self.out.write("\tM=D\n")
        return
    # 比較
    def gen_cmp(self, op):
        self.out.write("//" + op + "\n")
        # 1pop
        self.out.write("\t@SP\n")
        self.out.write("\tM=M-1\n")
        self.out.write("\tA=M\n")
        self.out.write("\tD=M\n")
        # 2pop
        self.out.write("\t@SP\n")
        self.out.write("\tM=M-1\n")
        self.out.write("\tA=M\n")
        # 処理
        self.out.write("\tD=M-D\n")
        lid = self.fn + str(self.lc)
        self.lc += 1
        # trueなら-1にしてくれるところに飛ぶそうでなければ0
        self.out.write("\t@T" +lid + "\n")
        self.out.write("\tD;" + op+ "\n")
        self.out.write("\tD=0\n")
        self.out.write("\t@EC" +lid + "\n")
        self.out.write("\t0;JMP\n")
        # push
        #True処理
        self.out.write("(T" + lid + ")\n")
        self.out.write("\tD=-1\n")
        self.out.write("\t@EC" +lid + "\n")
        self.out.write("\t0;JMP\n")

        # end output
        self.out.write("\t(EC" +lid + ")\n")
        self.out.write("\t@SP\n")
        self.out.write("\tM=M+1\n")
        self.out.write("\tA=M-1\n")
        self.out.write("\tM=D\n")
        self.out.write("//" + op + "end\n")
        return
    # unary
    def gen_uni(self, op):
        # sp参照して処理
        self.out.write("//" + op + "\n")
        self.out.write("\t@SP\n")
        self.out.write("\tA=M-1\n")
        self.out.write("\tM=" + op + "M\n")
        self.out.write("//" + op + "end\n")

        return

    def writeArithmetic(self, command):
        self.out.write("//" + command + "\n")
        if command == "add":
            self.gen_bin("+")
        elif command == "sub":
            self.gen_bin("-")
        elif command == "neg":
            self.gen_uni("-")
        elif command == "eq":
            self.gen_cmp("JEQ")
        elif command == "gt":
            self.gen_cmp("JGT")
        elif command == "lt":
            self.gen_cmp("JLT")
        elif command == "and":
            self.gen_bin("&")
        elif command == "and":
            self.gen_bin("|")
        elif command == "not":
            self.gen_uni("!")
        self.out.write("//" + command + "end\n")
        return

    def writePushPop(self,command, segment, index):
        if command == CommandType.C_PUSH:
            self.out.write("//push" + segment  + str(index)+ "\n")
            # baseからindex分ずらす必要があるものは先にbaseをずらす(popしたデータを持ってたらDが使えないので)
            if segment in {"local", "argument", "this", "that"}:
                self.out.write("\t@" + str(index) + "\n")
                self.out.write("\tD=A\n")
                if segment == "local":
                    self.out.write("\t@LCL\n")
                    self.out.write("\tM=M+D\n")
                elif segment == "argument":
                    self.out.write("\t@ARG\n")
                    self.out.write("\tM=M+D\n")
                elif segment == "this":
                    self.out.write("\t@THIS\n")
                    self.out.write("\tM=M+D\n")
                elif segment == "that":
                    self.out.write("\t@THAT\n")
                    self.out.write("\tM=M+D\n")
            # まずsegmentで参照元を決めて、データをとってくる
            # 定数ならその数字をそのまま
            if segment == "constant":
                self.out.write("\t@" + str(index) + "\n")
            elif segment == "local":
                self.out.write("\t@LCL\n")
                self.out.write("\tA=M\n")
            elif segment == "argument":
                self.out.write("\t@ARG\n")
                self.out.write("\tA=M\n")
            elif segment == "this":
                self.out.write("\t@THIS\n")
                self.out.write("\tA=M\n")
            elif segment == "that":
                self.out.write("\t@THAT\n")
                self.out.write("\tA=M\n")
            elif segment == "pointer":
                targ = 3 + index
                self.out.write("\t@" + str(targ) + "\n")
            elif segment == "temp":
                targ = 5 + index
                self.out.write("\t@" + str(targ) + "\n")
            #Global変数
            elif segment == "static":
                self.out.write("\t@" + self.fn + str(index) +"\n")

            # 定数以外はアドレスをたどってデータをとる
            if segment == "constant":
                self.out.write("\tD=A\n")
            else:
                self.out.write("\tD=M\n")

            #stack pointer に値をセット
            self.out.write("\t@SP\n")
            self.out.write("\tA=M\n")
            self.out.write("\tM=D\n")
            #stack pointer をincrement
            self.out.write("\t@SP\n")
            self.out.write("\tM=M+1\n")
            # ずらしたbase addressを戻す
            if segment in {"local", "argument", "this", "that"}:
                self.out.write("\t@" + str(index) + "\n")
                self.out.write("\tD=A\n")
                if segment == "local":
                    self.out.write("\t@LCL\n")
                    self.out.write("\tM=M-D\n")
                elif segment == "argument":
                    self.out.write("\t@ARG\n")
                    self.out.write("\tM=M-D\n")
                elif segment == "this":
                    self.out.write("\t@THIS\n")
                    self.out.write("\tM=M-D\n")
                elif segment == "that":
                    self.out.write("\t@THAT\n")
                    self.out.write("\tM=M-D\n")
            self.out.write("//push" + segment  + str(index)+ "end\n")
        elif command == CommandType.C_POP:
            self.out.write("//pop" + segment  + str(index)+ "\n")
            # baseからindex分ずらす必要があるものは先にbaseをずらす(popしたデータを持ってたらDが使えないので)
            if segment in {"local", "argument", "this", "that"}:
                self.out.write("\t@" + str(index) + "\n")
                self.out.write("\tD=A\n")
                if segment == "local":
                    self.out.write("\t@LCL\n")
                    self.out.write("\tM=M+D\n")
                elif segment == "argument":
                    self.out.write("\t@ARG\n")
                    self.out.write("\tM=M+D\n")
                elif segment == "this":
                    self.out.write("\t@THIS\n")
                    self.out.write("\tM=M+D\n")
                elif segment == "that":
                    self.out.write("\t@THAT\n")
                    self.out.write("\tM=M+D\n")
            #stack pointer から値を取得, sp decrement
            self.out.write("\t@SP\n")
            self.out.write("\tM=M-1\n")
            self.out.write("\tA=M\n")
            self.out.write("\tD=M\n")
            # pop先Addressを参照する
            if segment == "constant":
                self.out.write("\t@" + str(index) + "\n")
            elif segment == "local":
                self.out.write("\t@LCL\n")
                self.out.write("\tA=M\n")
            elif segment == "argument":
                self.out.write("\t@ARG\n")
                self.out.write("\tA=M\n")
            elif segment == "this":
                self.out.write("\t@THIS\n")
                self.out.write("\tA=M\n")
            elif segment == "that":
                self.out.write("\t@THAT\n")
                self.out.write("\tA=M\n")
            elif segment == "pointer":
                targ = 3 + index
                self.out.write("\t@" + str(targ) + "\n")
            elif segment == "temp":
                targ = 5 + index
                self.out.write("\t@" + str(targ) + "\n")
            # 新しいGlobal変数
            elif segment == "static":
                self.out.write("\t@" + self.fn + str(index) +"\n")
            # 書き込み

            self.out.write("\tM=D\n")
            # ずらしたbase addressを戻す
            if segment in {"local", "argument", "this", "that"}:
                self.out.write("\t@" + str(index) + "\n")
                self.out.write("\tD=A\n")
                if segment == "local":
                    self.out.write("\t@LCL\n")
                    self.out.write("\tM=M-D\n")
                elif segment == "argument":
                    self.out.write("\t@ARG\n")
                    self.out.write("\tM=M-D\n")
                elif segment == "this":
                    self.out.write("\t@THIS\n")
                    self.out.write("\tM=M-D\n")
                elif segment == "that":
                    self.out.write("\t@THAT\n")
                    self.out.write("\tM=M-D\n")
            self.out.write("//pop" + segment  + str(index)+ "end\n")
        return

    def writeLabel(self, label):
        self.out.write("//label\n")
        self.out.write("("+ label + ")\n")
        self.out.write("//label end\n")
        return

    def writeGoto(self, label):
        self.out.write("//goto" + label + "\n")
        self.out.write("\t@"+ label+ "\n")
        self.out.write("\t0;JMP\n")
        self.out.write("//goto" + label + "end\n")
        return

    def writeIf(self, label):
        self.out.write("//if" + label + "\n")
        # pop
        self.out.write("\t@SP\n")
        self.out.write("\tM=M-1\n")
        self.out.write("\tA=M\n")
        self.out.write("\tD=M\n")
        # 0でなければJUMP
        self.out.write("\t@"+ label+ "\n")
        self.out.write("\tD;JNE\n")
        self.out.write("//if" + label + "end\n")
        return

    def writeCall(self, functionName, numArgs):
        self.out.write("//call" + functionName + str(numArgs) + "\n")
        # return addressをpush
        returnAddress = "re" + functionName + str(self.rc)
        self.rc += 1
        self.out.write("\t@" + returnAddress + "\n")
        self.out.write("\tD=A\n")
        self.out.write("\t@SP\n")
        self.out.write("\tM=M+1\n")
        self.out.write("\tA=M-1\n")
        self.out.write("\tM=D\n")
        # リストの順番で４つ前の状態をスタックにpush
        for b in ["LCL", "ARG", "THIS", "THAT"]:
            self.out.write("\t@"+ b+"\n")
            self.out.write("\tD=M\n")
            self.out.write("\t@SP\n")
            self.out.write("\tM=M+1\n")
            self.out.write("\tA=M-1\n")
            self.out.write("\tM=D\n")

        # 引数は↑でpushした５つから、numArgsさかのぼったところまで
        self.out.write("\t@SP\n")
        self.out.write("\tD=M\n")
        self.out.write("\t@" + str(numArgs) +"\n")
        self.out.write("\tD=D-A\n")
        self.out.write("\t@5\n")
        self.out.write("\tD=D-A\n")
        self.out.write("\t@ARG\n")
        self.out.write("\tM=D\n")

        # Local変数は上のあとのspにする
        self.out.write("\t@SP\n")
        self.out.write("\tD=M\n")
        self.out.write("\t@LCL\n")
        self.out.write("\tM=D\n")

        # 関数へ飛ぶ
        self.writeGoto(functionName)

        # return addressはここにくるはず
        self.out.write("(" + returnAddress + ")\n")
        self.out.write("//call" + functionName + str(numArgs) + "end\n")
        return

    def writeReturn(self):
        self.out.write("//return\n")
        # FRAME = LCL,,, localのベースポインタはフレームの先頭
        self.out.write("\t@LCL\n")
        self.out.write("\tD=M\n")
        self.out.write("\t@FRAME\n")
        self.out.write("\tM=D\n")

        # *ARG = pop()関数の戻り地を別の場所に移す(ARGは前のStackの一番上から並べたからARGへ)
        # pop
        self.out.write("\t@SP\n")
        self.out.write("\tM=M-1\n")
        self.out.write("\tA=M\n")
        self.out.write("\tD=M\n")
        # *ARG = D
        self.out.write("\t@ARG\n")
        self.out.write("\tA=M\n")
        self.out.write("\tM=D\n")

        #のちのためにDへARGのアドレスをいれる
        # SP = ARG+1
        self.out.write("\t@ARG\n")
        self.out.write("\tD=M\n")
        self.out.write("\t@SP\n")
        self.out.write("\tM=D+1\n")
        # FRAME基準に前の状態を復元する
        # ["THAT", "THIS", "ARG", "LCL"] = *(FRAME-["1","2","3","4"])

        for i,b in zip(["1","2","3","4"],["THAT", "THIS", "ARG", "LCL"]):

            self.out.write("\t@" + i + "\n")
            self.out.write("\tD=A\n")

            self.out.write("\t@FRAME\n")
            self.out.write("\tA=M-D\n")
            self.out.write("\tD=M\n")
            self.out.write("\t@" + b + "\n")
            self.out.write("\tM=D\n")

        # RET = *(FRAME-5)
        self.out.write("\t@5\n")
        self.out.write("\tD=A\n")
        self.out.write("\t@FRAME\n")
        self.out.write("\tA=M-D\n")#これのあとのMがreturn address
        self.out.write("\tA=M\n")
        self.out.write("\t0;JMP\n")

        self.out.write("//return end\n")
        return

    # 関数の宣言
    def writeFunction(self, functionName, numLocals):
        self.out.write("//decl func"+functionName+str(numLocals)+"\n")
        # まず関数名ラベルの作成
        self.out.write("(" + functionName + ")\n")

        # local変数の0での初期化
        for _ in range(numLocals):
            self.writePushPop(commandType.C_PUSH, "constant", 0)
        # あとの処理はここではかかない
        self.out.write("//decl func"+functionName+str(numLocals)+"end\n")
        return
    def close(self):
        self.out.write("(END)\n")
        self.out.write("\t@END\n")
        self.out.write("\t0;JMP\n")
        self.out.close()
        return





if __name__ == "__main__":
    C = CodeWriter(argv[1])
    print(C.out)
