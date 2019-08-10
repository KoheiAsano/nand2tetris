import re

class Parser:

    def __init__(self, filename):
        self.src = open(filename, "r")
        self.hasMoreCommands = True
        self.commandType = ""
        self.symbol = ""
        self.dest = ""
        self.comp = ""
        self.jump = ""

    def advance(self):
        l = self.src.readline()
        # EOF?
        if l:
            # //以前を入手
            l = list(re.split(r"\/\/",l))[0]
            # 空白、タブ、改行コードの削除
            l = "".join(re.split(r"[\s\t\n]",l))

            if l:#not comment only?
                if l[0] == "@":
                    self.commandType = "A"
                    self.symbol = l[1:]
                elif l[0] == "(":
                    self.commandType = "L"
                    self.symbol = l[1:-1]
                else:
                    self.commandType = "C"
                    self.symbol = ""

                    CD_J = l.split(";")
                    # JUMP領域の計算
                    if len(CD_J) > 1:
                        self.jump = CD_J[1]
                    else:
                        self.jump = "N"
                    # C,Dを分離(=がないならDはない？)
                    operands = CD_J[0].split("=")[::-1]
                    self.comp = operands[0]
                    if len(operands) == 1:
                        self.dest = "N"
                    else:
                        self.dest = operands[1]
                return
            else:
                self.commandType = ""
        else:
            self.hasMoreCommands = False
            self.commandType = ""
            self.src.seek(0)
            return
