bits 32 
global start        
extern exit               
import exit msvcrt.dll    
segment data use32 class=data
        S db 2,-1, 5, -3; 02 ff, 05 , -3? 00 00 00
        l equ $-S
        D1 times l db 0 ;positive number
        D2 times l db 1;
segment code use32 class=code
    start:
        ;exercise 14
        ;A byte string S is given. 
        ;Obtain the string D1 which contains all the positive numbers of S 
        ;and the string D2 which contains all the negative numbers of S.
    
        mov ecx, l ; we put the length l in ECX in order to make the loop
        mov esi, 0
        mov edi, 0
        jecxz Sfarsit      
        Repeta:
            mov al, [S+esi]         ;we move the "esi-th" index number of the S string
            mov bl, 0               ;we move 0 in bl in order to see if a number is lower (negative) or higher than 0
            cmp al,bl               ;we compare al with bl (it calculates al-bl)
            jl checks               ;if the number is lower than 0 it jumps to line 27, where checks keyword is
               mov [D1+esi],al      ;else it continues with the following instructions
               inc esi                ;we move the positive number from al in D1 on the esi position
            jge jumpp
            checks:
               mov [D2+edi],al     ;we move the negative number from al in D2 on the edi position
               inc edi
            jumpp:
        loop Repeta
        Sfarsit:                    ;end of the program
        ; exit(0)
        push    dword 0      
        call    [exit]       
