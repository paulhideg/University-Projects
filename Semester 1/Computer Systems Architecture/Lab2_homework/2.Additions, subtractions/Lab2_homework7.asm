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
        ;(d-b*c+b*2)/a
        mov AL,[b]  ;AL=b
        mov DH,[c]  ;DH=c
        mul DH      ;AX=AL*DH=b*c
        mov BX,AX   ;BX=AX=b*c
        mov DH,2h   ;DH=2
        mul DH      ;AX=AL*DH=b*2
        mov CX,[d]  ;CX=d
        sub CX,BX   ;CX=CX-BX=d-b*c
        add CX,AX   ;CX=CX+AX=(d-b*c)+b*2
        mov AX,CX   ;AX=CX=d-b*c+b*2
        mov CL,[a]    ;CL=a
        div CL      ;AL=AX/CL=(d-b*c+b*2)/a
        


        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
