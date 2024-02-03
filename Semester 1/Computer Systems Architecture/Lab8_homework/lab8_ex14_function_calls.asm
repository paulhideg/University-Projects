bits 32

global start        

extern exit,scanf,printf
import exit msvcrt.dll

import scanf msvcrt.dll
import printf msvcrt.dll

segment data use32 class=data
    ; 14. Read two numbers a and b (in base 16) from the keyboard and calculate a+b. Display the result in base 10
    a dd 0
    b dd 0
    message db "Enter number (in base 16): ",0  ; message for scanf
    format_read db "%x",0           ; format for reading with scanf
    format_write db "%d + %d = %d",0    ; format for printing with printf
; our code starts here
segment code use32 class=code
    start:
        ; int printf(const char *format [,argument]...);
        push dword message
        call [printf]   ; show nice message for user interaction
        add esp,4   ; we pushed one dword to the stack which decreased esp with 4, so we increase it with 4
        
        push dword a
        push dword format_read
        call [scanf]    ; read first number
        add esp,4*2
        
        push dword message
        call [printf]
        add esp,4
        
        push dword b
        push dword format_read
        call [scanf]    ; read second number
        add esp,4*2
        
        mov eax,[a]
        mov ebx,[b]
        add eax,ebx ; eax=a+b
        
        push dword eax
        push dword [b]
        push dword [a]
        push dword format_write
        call [printf]   ; print result
        add esp,4*4
        
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program