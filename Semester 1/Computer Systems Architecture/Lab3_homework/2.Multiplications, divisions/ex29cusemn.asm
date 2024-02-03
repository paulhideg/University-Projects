bits 32 
global start        
extern exit               
import exit msvcrt.dll    
segment data use32 class=data
        ;variables:
        a db 3h
        b db 5h
        c db 6h
        d dd 8h
        x dq 9h
        
segment code use32 class=code
    start:
        ;exercise 29: (a+b)/(c-2)-d+2-x
        ; a,b,c-byte; d-doubleword; x-qword   (cu semn)
        
        mov AL,[a]
        mov BL,[b]
        add AL,BL   ;a+b
        cbw         ;AX=a+b
        
        mov AL,[c]
        cbw         ;AX=c
        sub CL,2 ;c-2
        div CL    ;AX= (a+b)/(c-2)
       
        cbw
        mov EBX,[d]
        sub EAX,EBX ;EAX=[(a+b)/(c-2)]-d
        
        mov EBX,2h
        add EAX,EBX ;EAX=[(a+b)/(c-2)-d]+2
        cdq         ;EDX:EAX=(a+b)/(c-2)-d+2
        
        mov EBX,[x]
        mov ECX,[x+4]   ;EBX:ECX=x
        
        sub EDX,EBX 
        sbb EAX,ECX     ;EDX:EAX=[(a+b)/(c-2)-d+2]-x
        
        
        push    dword 0      
        call    [exit]       
