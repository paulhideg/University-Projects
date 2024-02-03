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
       a db 4h
       b db 10h
       c db 2h
       d db 5h
       e dw 6h
       f dw 5h
       ; our code starts here
segment code use32 class=code
    start:
        ; ...
        ;[b*c-(e+f)]/(a+d)
        mov AL,[b]      ;AL=b
        mov DH,[c]      ;DH=c
        mul DH          ;AX=AL*DH=b*c
        
        mov BX,[e]      ;BX=e
        mov CX,[f]      ;CX=f
        add BX,CX       ;BX=BX+CX=e+f
        
        sub AX,BX       ;AX=AX-BX=(b*c)-(e+f)
            
        mov AL,[a]      ;AL=a
        mov BH,[d]      ;BH=d
        add AL,BH       ;AL=AL+BH=a+d
        
        mov CL,AL       ;CL=AL=a+d
        div CL          ;AL=AX/CL=[b*c-(e+f)]/(a+d)
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
