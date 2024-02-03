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

    a db 3h
    b db 2h
    c db 1h
    d dw 5h
; our code starts here
segment code use32 class=code
    start:
        ; ...
        ;[d-(a+b)*2]/c
        mov AL,[a]  ;AL=a
        mov AH,[b]  ;AH=b
        add AL,AH   ;AL=AL+AH=a+b
        mov DH,2h   ;DH=2
        mul DH      ;AX=AL*DH=AL*2=(a+b)*2
        mov BX,[d]  ;BX=d
        sub BX,AX   ;BX=BX-AX=d-(a+b)*2
        mov AX,BX   ;AX=BX=d-(a+b)*2
        mov CL,[c]  ;CL=c
        div CL      ;AL=AX/CL=[d-(a+b)*2]/c

        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
