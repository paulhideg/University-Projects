bits 32 
global start        
extern exit               
import exit msvcrt.dll    
segment data use32 class=data
        ;variables:
        a db 3h
        b dw 5h
        c dd 6h
        x dq 8h

segment code use32 class=code
    start:
        ;exercise 14: x+(2-a*b)/(a*3)-a+c
        ; a-byte; b-word; c-doubleword; x-qword
        mov AL,[a]  ;AL=a
        mov AH,0    ;AX=a
        mov DX,[b]  ;DX=b
        mul DX      ;DX:AX=a*b
        mov BX,2h
        sub BX,AX   ;2-a*b
        
        mov AL,[a]
        mov DH,3h
        mul DH      ;AX=a*3
        mov CX,AX   ;CX=a*3
        mov SI,CX   ;SI=a*3
        
        mov AX,BX   ;AX=2-a*b
        mov DX,0    ;DX:AX=2-a*b
        div SI      ;AX=(2-a*b)/(a*3)
        mov BX,AX   ;BX=(2-a*b)/(a*3)
        
        mov AL,[a]
        mov AH,0    ;AX=a
        sub BX,AX   ;[(2-a*b)/(a*3)]-a
        
        mov AX,BX   ;AX=[(2-a*b)/(a*3)]-a
        mov DX,0    
        push DX
        push AX
        pop EAX     ;EAX=[(2-a*b)/(a*3)]-a
        
        mov EBX,[c]
        add EAX,EBX ;[(2-a*b)/(a*3)-a]+c
        mov EDX,0   ;EDX:EAX=(2-a*b)/(a*3)-a+c
        
        mov EBX,dword[x]
        mov ECX,dword[x+4]  ;EBX:ECX=x
        
        add EBX,EDX
        adc ECX,EAX     ;EBX:ECX=x+[(2-a*b)/(a*3)-a+c]
        
        
        
        push    dword 0      
        call    [exit]       
