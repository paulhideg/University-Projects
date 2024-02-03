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
        ;exercise 14:   (a+a)-(b+b)-(c+d)+(d+d)  (cu semn)
        
        mov DH,[a]
        mov AL,2h
        mul DH      ;AX=a+a
        
        mov BX,AX   ;BX=a+a
        
        mov AX,[b]
        mov DX,2h
        mul DX      ;DX:AX=b+b
        push DX
        push AX
        pop EBX     ;EBX=b+b
        
        mov AX,BX   ;AX=a+a
        cwde        ;EAX=a+a
        
        sub EAX,EBX ;EAX=(a+a)-(b+b)
        
        mov EBX,EAX ; EBX=(a+a)-(b+b)
        
        mov EAX,[c]
        cdq         ;EDX:EAX=c
        mov ECX,dword[d]
        mov ESI,dword[d+4]
        add EDX,ECX     
        adc EAX,ESI     ;EDX:EAX=c+d
        mov ECX,EDX     
        mov EBX,EAX     ;ECX:EBX=c+d
        
        mov EAX,EBX     ;EAX=(a+a)-(b+b)
        cdq             ;EDX:EAX=(a+a)-(b+b)
        sub EDX,ECX
        sbb EAX,EBX     ;EDX:EAX=[(a+a)-(b+b)]-(c+d)
        mov ECX,EDX     
        mov EBX,EAX     ;ECX:EBX=[(a+a)-(b+b)]-(c+d)
        
        mov EDX,dword[d+4]
        mov EAX,dword[d]
        mov ESI,dword[d+4]
        mov EDI,dword[d]
        add EDX,ESI
        adc EAX,EDI      ;EDX:EAX=d+d
        
        add ECX,EDX
        adc EBX,EAX      ;ECX:EBX=[(a+a)-(b+b)-(c+d)]+(d+d)  
        
        
        push    dword 0      
        call    [exit]       
