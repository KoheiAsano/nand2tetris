//push
//まずindexずらす
//データとってくる
	@10
	D=A
	@SP
	A=M
	M=D
	@SP
	M=M+1
//indexをもどす
//pop
//まずindexずらす
	@0
	D=A
	@LCL
	M=M+D
	@SP
	M=M-1
	A=M
	D=M
	@LCL
	A=M
	M=D
//indexをもどす
	@0
	D=A
	@LCL
	M=M-D
//push
//まずindexずらす
//データとってくる
	@21
	D=A
	@SP
	A=M
	M=D
	@SP
	M=M+1
//indexをもどす
//push
//まずindexずらす
//データとってくる
	@22
	D=A
	@SP
	A=M
	M=D
	@SP
	M=M+1
//indexをもどす
//pop
//まずindexずらす
	@2
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
//indexをもどす
	@2
	D=A
	@ARG
	M=M-D
//pop
//まずindexずらす
	@1
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
//indexをもどす
	@1
	D=A
	@ARG
	M=M-D
//push
//まずindexずらす
//データとってくる
	@36
	D=A
	@SP
	A=M
	M=D
	@SP
	M=M+1
//indexをもどす
//pop
//まずindexずらす
	@6
	D=A
	@THIS
	M=M+D
	@SP
	M=M-1
	A=M
	D=M
	@THIS
	A=M
	M=D
//indexをもどす
	@6
	D=A
	@THIS
	M=M-D
//push
//まずindexずらす
//データとってくる
	@42
	D=A
	@SP
	A=M
	M=D
	@SP
	M=M+1
//indexをもどす
//push
//まずindexずらす
//データとってくる
	@45
	D=A
	@SP
	A=M
	M=D
	@SP
	M=M+1
//indexをもどす
//pop
//まずindexずらす
	@5
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
//indexをもどす
	@5
	D=A
	@THAT
	M=M-D
//pop
//まずindexずらす
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
//indexをもどす
	@2
	D=A
	@THAT
	M=M-D
//push
//まずindexずらす
//データとってくる
	@510
	D=A
	@SP
	A=M
	M=D
	@SP
	M=M+1
//indexをもどす
//pop
//まずindexずらす
	@SP
	M=M-1
	A=M
	D=M
	@11
	M=D
//indexをもどす
//push
//まずindexずらす
	@0
	D=A
	@LCL
	M=M+D
//データとってくる
	@LCL
	A=M
	D=M
	@SP
	A=M
	M=D
	@SP
	M=M+1
//indexをもどす
	@0
	D=A
	@LCL
	M=M-D
//push
//まずindexずらす
	@5
	D=A
	@THAT
	M=M+D
//データとってくる
	@THAT
	A=M
	D=M
	@SP
	A=M
	M=D
	@SP
	M=M+1
//indexをもどす
	@5
	D=A
	@THAT
	M=M-D
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
//push
//まずindexずらす
	@1
	D=A
	@ARG
	M=M+D
//データとってくる
	@ARG
	A=M
	D=M
	@SP
	A=M
	M=D
	@SP
	M=M+1
//indexをもどす
	@1
	D=A
	@ARG
	M=M-D
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
//push
//まずindexずらす
	@6
	D=A
	@THIS
	M=M+D
//データとってくる
	@THIS
	A=M
	D=M
	@SP
	A=M
	M=D
	@SP
	M=M+1
//indexをもどす
	@6
	D=A
	@THIS
	M=M-D
//push
//まずindexずらす
	@6
	D=A
	@THIS
	M=M+D
//データとってくる
	@THIS
	A=M
	D=M
	@SP
	A=M
	M=D
	@SP
	M=M+1
//indexをもどす
	@6
	D=A
	@THIS
	M=M-D
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
//push
//まずindexずらす
//データとってくる
	@11
	D=M
	@SP
	A=M
	M=D
	@SP
	M=M+1
//indexをもどす
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
(END)
	@END
	0;JMP
