

bits 32 
global start        
extern exit               
import exit msvcrt.dll    
segment data use32 class=data
        ;variables:
        A dd 10101110011001001010100111101111b
        B dd 0
        C dd 0
  
segment code use32 class=code
    start:
        ;Given the doubleword A, obtain the integer number n represented on the bits 14-17 of A. 
        ;Then obtain the doubleword B by rotating A n positions to the left. 
        ;Finally, obtain the byte C as follows:
        ;the bits 0-5 of C are the same as the bits 1-6 of B
        ;the bits 6-7 of C are the same as the bits 17-18 of B
        mov EAX,0
        mov ECX,0
        mov EAX,[A]                                 ;EAX=A
        and EAX, 00000000000000111100000000000000b  ;we keep only the 14-17 bits of A
        ror EAX,14                                  ;rotates A 14 bits to the right with 14 bits
        or CL,AL                                   ;CL=n
        
        mov EDX,[A]                                 ;EDX=A
        rol EDX,CL                                  ;rotate to left A with n positions
        mov [B],EDX         ;B                      :B=EDX
        
        mov ECX,0            ;C
        mov EAX,[B]                                 ;EAX=B
        and EAX, 0000000000000000000000001111110b   ;we only keep the 1-6 bits of B
        ror EAX,1                                   ;rotate B to right with 1 bit
        or CL,AL                                    ;the bits 0-5 of C are the same as the 1-6 of B
        
        mov EAX,[B]                                 ;EAX=b
        and EAX, 0000000000000000110000000000000b   ;we keep 17-18 bits of B
        ror EAX,17                                  ;we rotate B to the right with 17 bits
        or CL,AL                                    ;the bits 6-7 of C are the same as the 17-18 of B
        mov [C],CL                                  
        
        
        push    dword 0      
        call    [exit]    