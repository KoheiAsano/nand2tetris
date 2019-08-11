from CommandType import CommandType
import re
class Parser:
    def __init__(self, filename):
        self.src = open(filename, "r")
        self.hasMoreCommands = True
        self.commandType = ""
        self.arg0 = ""
        self.arg1 = 0xffff

    def advance(self):
        l = self.src.readline()
        if l:
            # コメント除去、改行も
            l = list(re.split(r"[\/\/\n]",l))[0]
            if not l:
                self.commandType = ""
                self.arg0 = ""
                self.arg1 = 0xffff
                return
            coms = l.split(" ")
            # print(coms)

            if coms[0] in {"add", "sub", "neg", "eq", "gt", "lt", "and", "or", "not"}:
                self.commandType = CommandType.C_ARITHMETIC
                self.arg0 = coms[0]
                self.arg1 = 0xffff
            elif coms[0] == "push":
                self.commandType = CommandType.C_PUSH
                self.arg0 = coms[1]
                self.arg1 = int(coms[2])
            elif coms[0] == "pop":
                self.commandType = CommandType.C_POP
                self.arg0 = coms[1]
                self.arg1 = int(coms[2])
            elif coms[0][-1] == ":":
                self.commandType = CommandType.C_LABEL
                self.arg0 = coms[1]
                self.arg1 = 0xffff
            elif coms[0] == "goto":
                self.commandType = CommandType.C_GOTO
                self.arg0 = coms[1]
                self.arg1 = 0xffff
            elif coms[0] == "if-goto":
                self.commandType = CommandType.C_IF
                self.arg0 = coms[1]
                self.arg1 = 0xffff
            elif coms[0] == "function":
                self.commandType = CommandType.C_FUNCTION
                self.arg0 = coms[1]
                self.arg1 = int(coms[2])
            elif coms[0] == "return":
                self.commandType = CommandType.C_RETURN
                self.arg0 = ""
                self.arg1 = 0xffff
            elif coms[0] == "call":
                self.commandType = CommandType.C_CALL
                self.arg0 = coms[1]
                self.arg1 = int(coms[2])
        else:
            self.hasMoreCommands = False
            self.commandType = ""
            self.arg0 = ""
            self.arg1 = 0xffff
