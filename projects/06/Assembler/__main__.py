from sys import argv

from Parser import Parser
from Code import Code
from SymbolTable import SymbolTable

C = Code()
S = SymbolTable()
if __name__ == "__main__":
    P = Parser(argv[1])
    out = open(argv[1].split(".")[0] + ".hack","w")
    # 1パス目lは読んでる行
    l = 0
    while(P.hasMoreCommands):
        P.advance()
        if P.commandType == "L":
            S.addEntry(P.symbol, l)
            continue
        elif P.commandType:
            l+=1
    # ここクソ
    P.hasMoreCommands = True
    varptr = 16
    while(P.hasMoreCommands):
        P.advance()
        if P.commandType == "A":
            # constant
            if P.symbol.isnumeric():
                out.write(bin(int(P.symbol))[2:].zfill(16) + "\n")
            # label
            elif P.symbol in S.table:
                out.write(bin(S.table[P.symbol])[2:].zfill(16) + "\n")
            # var
            else:
                if not S.contains(P.symbol):
                    S.addEntry(P.symbol, varptr)
                    varptr += 1
                out.write(bin(S.table[P.symbol])[2:].zfill(16) + "\n")
                # out.write("\n")
        elif P.commandType == "C":
            out.write("111" + C.comp(P.comp) + C.dest(P.dest) + C.jump(P.jump) + "\n")
        else:
            continue
    out.close()
    # print(S.table)
