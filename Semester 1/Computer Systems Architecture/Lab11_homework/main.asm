bits 32

global start        

extern exit         
extern scanf         
extern gets         
extern printf      
          
import exit msvcrt.dll
import scanf msvcrt.dll
import gets msvcrt.dll
import printf msvcrt.dll

%include "module.asm"

segment data use32 class=data
    n dd 0
    n_fr db "%d",0
    i dd 0
    s times 100 db 0
    result times 300 db 0
    format_print db '%s',10,0
    nice_message db 10,"Enter sentence %d: ",0
    nice_message0 db 10,"Enter n: ",0
    bad_message db "You can read 100 characters max per string.",0
segment code use32 class=code
    start:
    push dword nice_message0
    call [printf]
    add esp,4*1
    
    push dword n
    push dword n_fr
    call [scanf]
    add esp,4*2  
    
    push dword s
    call [gets]
    add esp, 4
    
    xor ecx,ecx
    loop_sentences:
        cmp ecx,[n]
        jae done_looping
    pushad
        push ecx
        push dword nice_message
        call [printf]
        add esp,4*2
    popad
    
    
        ;char *fgets(char *s, int size, FILE *stream);
    pushad
        push dword s
        call [gets]
        add esp, 4
    popad
        
        cmp byte [result-1],0
        jne bad
        cmp eax,0
        je bad
        
        ;concatenate_words(s,result,i)
        ; we take the i'th word from string s,add it to end of result
        pushad
        
        push dword ecx
        push dword result
        push dword s
        call concatenate_words
        add esp,4*3
    popad
        
        inc ecx
    jmp loop_sentences
    done_looping:
    
    
    push dword result
    push dword format_print
    call [printf]
    add esp,4*2
    jmp done
    
    bad:
    push dword bad_message
    call [printf]
    
    done:

        push    dword 0
        call    [exit]
