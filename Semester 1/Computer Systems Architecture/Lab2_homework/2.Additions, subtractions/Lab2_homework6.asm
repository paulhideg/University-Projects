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
    a dw 5h
    b dw 2h
    c dw 1h
    d dw 5h
; our code starts here
segment code use32 class=code
    start:
        ;(d-a)+(b+b+c)
        ; ...
        mov AX,[b]
        mov BX,[a]
        mov CX,[c]
        mov DX,[d]

        sub DX,BX  ;d-a
        mov BX,DX  ; BX=d-a
        mov DX,2h   ;DX=2
        mul DX      ;DX=b*2
        push AX
        push DX
        pop EBX
        mov AX,[c]
        mov DX,0    ;pentru conversia AX → DX:AX (EAX)
        push AX
        push DX
        pop EAX
        add EBX,EAX ; b+b+c
        mov AX,BX
        mov DX,0 
        push AX
        push DX
        pop ECX
        
        add ECX,EBX  ;(d-a)+(b+b+c)

        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
