//init
	@256
	D=A
	@SP
	M=D
//initend
//pushargument1
	@1
	D=A
	@ARG
	M=M+D
	@ARG
	A=M
	D=M
	@SP
	A=M
	M=D
	@SP
	M=M+1
	@1
	D=A
	@ARG
	M=M-D
//pushargument1end
//poppointer1
	@SP
	M=M-1
	A=M
	D=M
	@4
	M=D
//poppointer1end
//pushconstant0
	@0
	D=A
	@SP
	A=M
	M=D
	@SP
	M=M+1
//pushconstant0end
//popthat0
	@0
	D=A
	@THAT
	M=M+D
	@SP
	M=M-1
	A=M
	D=M
	@THAT
	A=M
	M=D
	@0
	D=A
	@THAT
	M=M-D
//popthat0end
//pushconstant1
	@1
	D=A
	@SP
	A=M
	M=D
	@SP
	M=M+1
//pushconstant1end
//popthat1
	@1
	D=A
	@THAT
	M=M+D
	@SP
	M=M-1
	A=M
	D=M
	@THAT
	A=M
	M=D
	@1
	D=A
	@THAT
	M=M-D
//popthat1end
//pushargument0
	@0
	D=A
	@ARG
	M=M+D
	@ARG
	A=M
	D=M
	@SP
	A=M
	M=D
	@SP
	M=M+1
	@0
	D=A
	@ARG
	M=M-D
//pushargument0end
//pushconstant2
	@2
	D=A
	@SP
	A=M
	M=D
	@SP
	M=M+1
//pushconstant2end
//sub
	@SP
	M=M-1
	A=M
	D=M
	@SP
	M=M-1
	A=M
	D=M-D
	@SP
	M=M+1
	A=M-1
	M=D
//subend
//popargument0
	@0
	D=A
	@ARG
	M=M+D
	@SP
	M=M-1
	A=M
	D=M
	@ARG
	A=M
	M=D
	@0
	D=A
	@ARG
	M=M-D
//popargument0end
//label
(MAIN_LOOP_START)
//label end
//pushargument0
	@0
	D=A
	@ARG
	M=M+D
	@ARG
	A=M
	D=M
	@SP
	A=M
	M=D
	@SP
	M=M+1
	@0
	D=A
	@ARG
	M=M-D
//pushargument0end
//ifCOMPUTE_ELEMENT
	@SP
	M=M-1
	A=M
	D=M
	@COMPUTE_ELEMENT
	D;JNE
//ifCOMPUTE_ELEMENTend
//gotoEND_PROGRAM
	@END_PROGRAM
	0;JMP
//gotoEND_PROGRAMend
//label
(COMPUTE_ELEMENT)
//label end
//pushthat0
	@0
	D=A
	@THAT
	M=M+D
	@THAT
	A=M
	D=M
	@SP
	A=M
	M=D
	@SP
	M=M+1
	@0
	D=A
	@THAT
	M=M-D
//pushthat0end
//pushthat1
	@1
	D=A
	@THAT
	M=M+D
	@THAT
	A=M
	D=M
	@SP
	A=M
	M=D
	@SP
	M=M+1
	@1
	D=A
	@THAT
	M=M-D
//pushthat1end
//add
	@SP
	M=M-1
	A=M
	D=M
	@SP
	M=M-1
	A=M
	D=M+D
	@SP
	M=M+1
	A=M-1
	M=D
//addend
//popthat2
	@2
	D=A
	@THAT
	M=M+D
	@SP
	M=M-1
	A=M
	D=M
	@THAT
	A=M
	M=D
	@2
	D=A
	@THAT
	M=M-D
//popthat2end
//pushpointer1
	@4
	D=M
	@SP
	A=M
	M=D
	@SP
	M=M+1
//pushpointer1end
//pushconstant1
	@1
	D=A
	@SP
	A=M
	M=D
	@SP
	M=M+1
//pushconstant1end
//add
	@SP
	M=M-1
	A=M
	D=M
	@SP
	M=M-1
	A=M
	D=M+D
	@SP
	M=M+1
	A=M-1
	M=D
//addend
//poppointer1
	@SP
	M=M-1
	A=M
	D=M
	@4
	M=D
//poppointer1end
//pushargument0
	@0
	D=A
	@ARG
	M=M+D
	@ARG
	A=M
	D=M
	@SP
	A=M
	M=D
	@SP
	M=M+1
	@0
	D=A
	@ARG
	M=M-D
//pushargument0end
//pushconstant1
	@1
	D=A
	@SP
	A=M
	M=D
	@SP
	M=M+1
//pushconstant1end
//sub
	@SP
	M=M-1
	A=M
	D=M
	@SP
	M=M-1
	A=M
	D=M-D
	@SP
	M=M+1
	A=M-1
	M=D
//subend
//popargument0
	@0
	D=A
	@ARG
	M=M+D
	@SP
	M=M-1
	A=M
	D=M
	@ARG
	A=M
	M=D
	@0
	D=A
	@ARG
	M=M-D
//popargument0end
//gotoMAIN_LOOP_START
	@MAIN_LOOP_START
	0;JMP
//gotoMAIN_LOOP_STARTend
//label
(END_PROGRAM)
//label end
(END)
	@END
	0;JMP
