// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed.
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.
//白と黒の色(bit)を設定
(INIT)
  @0
  D=A
  @cur
  M=D

  @8192
  D=A
  @size
  M=D

  @BORW
  0;JMP

(BORW)
  @KBD
  D=M

  @WHITE
  D;JEQ

  @BLACK
  D;JGT

(BLACK)
  @cur
  D=M
  M=M+1
  @SCREEN
  A=A+D
  M=-1

  @size
  M=M-1
  D=M
  @BLACK
  D;JGT
  @INIT
  0;JMP

(WHITE)
  @cur
  D=M
  M=M+1
  @SCREEN
  A=A+D
  M=0

  @size
  M=M-1
  D=M

  @WHITE
  D;JGT
  @INIT
  0;JMP
