

bits 32 
global start        
extern exit               
import exit msvcrt.dll    
segment data use32 class=data
        ;variables:
  
segment code use32 class=code
    start:
        mov ax,61440 

        mov bl,5 

        div bl    ;Given the doublewords A si B, obtain the quadword C as follows:
        ;the bits 8-15 of C are the same as the bits 23-30 of B complemented
        ;the bits 16-21 of C have the value 101010
        ;the bits 22-31 of C have the value 0
        ;the bits 32-42 of C are the same as the bits 21-31 of B
        ;the bits 43-55 of C are the same as the bits 1-13 of A
        ;the bits 56-63 of C are the same as the bits 24-31 of the result A XOR 0ABh
        
        
        push    dword 0      
        call    [exit]    