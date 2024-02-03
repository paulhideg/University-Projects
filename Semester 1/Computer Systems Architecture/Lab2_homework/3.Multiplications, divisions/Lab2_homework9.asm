bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    a db 5h
    d db 3h
    e dw 2h
    f dw 6h
; our code starts here
segment code use32 class=code
    start:
        ; ...
        ;a*d*e/(f-5)
        mov AL,[a]  ;AL=a
        mov DH,[d]  ;DH=d
        mul DH      ;AX=AL*DH=a*d
        mov DX,[e]  ;DX=e
        mul DX      ;DX:AX ← AX * DX=a*d*e
        
        
        mov SI,[f]  ;CX=f
        mov DX,5h   ;DX=5
        sub SI,DX   ;CX=CX-DX=f-5
        div SI      ; AX ← DX:AX / SI, DX ← DX:AX % SI


        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
