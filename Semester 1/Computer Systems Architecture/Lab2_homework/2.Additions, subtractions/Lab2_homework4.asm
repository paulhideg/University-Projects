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
    ;(b+c)+(a+b-d)
    a db 3h
    b db 2h
    c db 3h
    d db 1h

; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov AL,[c]    ;AL=c
        mov AH,[b]    ;AH=b
        add AL,AH   ;AL=AL+AH (b+c)
        
        mov BH,[a]    ;BH=a
        add BH,AH   ;BH=BH+AH (a+b)
        mov BL,[d]  ;BL=d
        sub BH,BL   ;BH=BH+DL   (a+b-d)
        add AL,BH   ;AL=AL+BH   (b+c)+(a+b-d)

        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
