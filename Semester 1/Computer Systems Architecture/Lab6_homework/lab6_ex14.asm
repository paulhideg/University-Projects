bits 32 ; assembling for the 32 bits architecture
; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ;14.Given an array S of doublewords, build the array of bytes D formed from bytes of doublewords sorted as unsigned numbers in ascending order.
     s dd 12345608h, 1A2B3C15h
     len equ ($-s)
     ;d db 07h, 12h, 15h, 1Ah, 2Bh, 34h, 3Ch, 56h
     d resb len
     i dd 0
     j dd 0
segment code use32 class=code
    start:
        
        mov ecx,len ; n,length of string
        dec ecx ; first loop goes to n-1
        ;the loop does a basic sorting algorithm,
        ;for(i=0;i<n-1;i++)
        ;    for(j=i+1;j<n;j++)
        ;    if(s[i]>s[j])
        ;        swap(s[i],s[j]);
        ; at the end, the string s will be sorted in place
        start_loop1:
            push ecx ; save ecx because we will change it in second loop
                mov eax,[i]
                inc eax  ; eax=i+1
                mov [j],eax ;j=i+1
                start_loop2:    ; second loop goes from j to n, so from i+1 to n
                    push ecx    ;save ecx because we will change it later
                    
                    mov esi,s
                    add esi,[i] ;get address of s+i
                    lodsb   ;al = s[i]
                    mov cl,al ;cl=s[i]
                    mov esi,s
                    add esi,[j] ;get address of s+j
                    lodsb  ;al=s[j]
                    mov bl,al;bl=s[j]
                    
                    cmp cl,al ; cmp s[i],s[j]
                    jbe skip
                        mov dl,cl   ;aux=s[i]; dl=s[i]
                        mov edi,s
                        add edi,[i]
                        stosb       ;s[i]=s[j]
                        mov edi,s
                        add edi,[j]  
                        mov al,dl
                        stosb       ;s[j]=aux
                    skip:
                    inc dword [j] ;j++
                    pop ecx ;restore ecx
                loop start_loop2
            inc dword [i] ;i++
            pop ecx ; restore ecx
        loop start_loop1
        
        mov ecx,len ; length of string in bytes
        mov esi,s   ; address of string
        mov edi,d   ;address of result
        
        storee:
            lodsb   ;al=each byte from string
            stosb   ; each byte from string is stored in result
        loop storee
         
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program