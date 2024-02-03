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
        ;exercise 14: (a+d)-(c-b)+c
        
        mov AL,[a]  ;AL=a
        mov AH,0    ;converting AL → AX
        mov DX,0    ;converting AX → DX:AX
        push AX
        push DX
        pop EAX     ;EAX=a
        mov EDX,0   ;EAX ->quad --> EDX:EAX = a
        
        mov EBX,dword[d] ;EBX=d
        mov ECX,dword[d+4]  ;ECX=d(part2)
        add EBX,EDX         ;d+a
        add ECX,EAX         ;d+a
        
        mov EDX,[c] ;ECX=c
        
        mov AX,[b]  ;AX=b
        mov DX,0    ;converting AX → DX:AX = b
        push AX
        push DX
        pop EAX     ;EAX=b
        
        sub EDX,EAX ;EDX=EDX-EAX=c-b
        mov EAX,EDX     
        mov EDX,0   ;EAX -->EDX:EAX = c-b
        
        sub EBX,EDX     ;EBX=(d+a)-(c-b)
        sbb ECX,EAX     ;ECX=(d+a)-(c-b)
        
       
        
        mov EAX,[c] ;EAX=c
        mov EDX,0   ;EAX --> EDX:EAX = c
        
        add EBX,EDX     ;EBX=[(d+a)-(c-b)]+c
        adc ECX,EAX     ;ECX=[(d+a)-(c-b)]+c
        
        
        push    dword 0      
        call    [exit]       
