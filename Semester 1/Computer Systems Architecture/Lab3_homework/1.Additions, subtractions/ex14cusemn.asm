bits 32 
global start        
extern exit               
import exit msvcrt.dll    
segment data use32 class=data
        ;variables:
        a db 3h
        b dw 5h
        c dd 6h
        d dq 8h

segment code use32 class=code
    start:
        ;exercise 14:   c-b-(a+a)-b (cu semn)
        
        mov EBX,[c]     ;EBX=c
        mov AX,[b]      ;AX=b
        cwde            ;AX -> EAX=b
        sub EBX,EAX     ;c-b
        
        mov AL,2h
        mov DH,[a]      ;DH=a
        mul DH          ;AX=2*a=a+a
        cwde            ;EAX=a+a
        
        sub EBX,EAX     ;(c-b)-(a+a)
        
        mov EAX,EBX     ;EAX=(c-b)-(a+a)
        cdq             ;EDX:EAX=(c-b)-(a+a)
        
        mov EBX,dword[d]    ;EBX=d
        mov ECX,dword[d+4]  ;ECX=d
        
        sub EDX,EBX     ;EDX=[c-b-(a+a)]-b
        sub EAX,ECX     ;EAX=[c-b-(a+a)]-b
        
        
        push    dword 0      
        call    [exit]       
