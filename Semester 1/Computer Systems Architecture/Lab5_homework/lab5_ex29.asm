bits 32 
global start        
extern exit               
import exit msvcrt.dll    
segment data use32 class=data
        S db 2,-1, 5, -3
        l equ ($-S)-1
        D times l db 0 
segment code use32 class=code
    start:
        ;exercise 29
    
        mov ecx, l ; we put the length l in ECX in order to make the loop
        mov esi, 0
        jecxz Sfarsit      ;if l equals to 0, it jumps to the end of the program (sfarsit)
        Repeta:
            mov al, [S+esi]         ;we move the "esi-th" index number of the S string
            mov bl, [S+esi+1]       ;we move the "esi-th"+1 index number of the S string (the next consecutive number of esi)
            add al,bl               ;we add the 2 consecutive numbers
            mov [D+esi],al          ;we move the result in the D+esi position
            inc esi                 
        loop Repeta
        Sfarsit:                    ;end of the program
        ; exit(0)
        push    dword 0      
        call    [exit]       
