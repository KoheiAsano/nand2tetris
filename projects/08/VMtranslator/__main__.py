import os
from sys import argv, stderr, exit

from CodeWriter import CodeWriter
from Parser import Parser
from CommandType import CommandType


if __name__ == "__main__":
    if len(argv) < 2:
        raise Exception("Usage: python3 VMtranslator $FILENAME")

    C = CodeWriter(argv[1])
    # file name リストを取得
    try:
        dirPath = "/".join(argv[1].split("/")) + "/"
        files = [dirPath + fn for fn in os.listdir(argv[1]) if fn[-3:] == ".vm"]
    except NotADirectoryError:
        files = [argv[1]]
    #それぞれParse, コード生成
    for file in files:
        P = Parser(file)
        C.setFileName(file)
        while(P.hasMoreCommands):
            P.advance()
            if P.commandType == CommandType.C_ARITHMETIC:
                C.writeArithmetic(P.arg0)
            elif P.commandType == CommandType.C_PUSH:
                C.writePushPop(P.commandType, P.arg0, P.arg1)
            elif P.commandType == CommandType.C_POP:
                C.writePushPop(P.commandType, P.arg0, P.arg1)
            elif P.commandType == CommandType.C_LABEL:
                C.writeLabel(P.arg0)
            elif P.commandType == CommandType.C_GOTO:
                C.writeGoto(P.arg0)
            elif P.commandType == CommandType.C_IF:
                C.writeIf(P.arg0)
            elif P.commandType == CommandType.C_FUNCTION:
                C.writeFunction(P.arg0, P.arg1)
            elif P.commandType == CommandType.C_RETURN:
                C.writeReturn()
            elif P.commandType == CommandType.C_CALL:
                C.writeCall(P.arg0, P.arg1)
    C.close()
