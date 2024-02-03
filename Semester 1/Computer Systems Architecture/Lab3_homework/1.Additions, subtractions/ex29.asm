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
        ;exercise 29:   d+c-b+(a-c)
        
        mov EBX,dword[d]    ;EAX=d
        mov ECX,dword[d+4]  ;EBX=d(part2)
        mov EAX,[c]         ;EBX=c
        mov EDX,0           ;EAX ->quad --> EDX:EAX = c
        add EBX,EDX         ;d+c
        add ECX,EAX         ;d+c
        
        mov AX,[b]          ;AX=b
        mov DX,0            ; pentru conversia AX → DX:AX=b
        push DX
        push AX
        pop EAX             ;EAX=b
        mov EDX,0           ; pentru conversia EAX → EDX:EAX=b
        
        sub EBX,EDX         ;d+c-b
        sub ECX,EAX         ;d+c-b
        
        mov AL,[a]          ;AL=a
        mov AH,0            ;AX=a
        mov DX,0
        push DX
        push AX
        pop EAX             ;EAX=a
        mov EDX,[c]         ;EDX=c
        sub EAX,EDX         ;a-c
        mov EDX,0           ; pentru conversia EAX → EDX:EAX=a-c
        
        add EBX,EDX         ;(d+c-b)+(a-c)
        add ECX,EAX         ;(d+c-b)+(a-c)
        
        
        
        push    dword 0      
        call    [exit]       
