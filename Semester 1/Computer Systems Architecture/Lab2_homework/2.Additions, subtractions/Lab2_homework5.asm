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
    ;(c+d)+(a-b)+a
    a dw 3h
    b dw 2h
    c dw 3h
    d dw 1h
; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov AX,[a]
        mov BX,[b]
        mov CX,[c]
        mov DX,[d]
        
        add CX,DX   ;c+d
        sub AX,BX   ;a-b
        mov BX,[a]  
        add CX,AX   ;(c+d)+(a-b)
        add CX,BX   ;(c+d)+(a-b)+b
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
