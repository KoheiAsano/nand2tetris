//init
//initend
//decl funcSimpleFunction.test2
(SimpleFunction.test)
	@0
	D=A
	@SP
	M=M+1
	A=M-1
	M=D
	@SP
	M=M+1
	A=M-1
	M=D
//decl funcSimpleFunction.test2end
//pushlocal0
	@0
	D=A
	@LCL
	M=M+D
	@LCL
	A=M
	D=M
	@SP
	A=M
	M=D
	@SP
	M=M+1
	@0
	D=A
	@LCL
	M=M-D
//pushlocal0end
//pushlocal1
	@1
	D=A
	@LCL
	M=M+D
	@LCL
	A=M
	D=M
	@SP
	A=M
	M=D
	@SP
	M=M+1
	@1
	D=A
	@LCL
	M=M-D
//pushlocal1end
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
//not
//!
	@SP
	A=M-1
	M=!M
//!end
//notend
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
//return
	@LCL
	D=M
	@FRAME
	M=D
	@SP
	M=M-1
	A=M
	D=M
	@ARG
	A=M
	M=D
	D=A
	@SP
	M=D+1
	@1
	D=A
	@FRAME
	A=M-D
	D=M
	@THAT
	M=D
	@2
	D=A
	@FRAME
	A=M-D
	D=M
	@THIS
	M=D
	@3
	D=A
	@FRAME
	A=M-D
	D=M
	@ARG
	M=D
	@4
	D=A
	@FRAME
	A=M-D
	D=M
	@LCL
	M=D
	@5
	D=A
	@FRAME
	A=M-D
	0;JMP
//return end
(END)
	@END
	0;JMP
