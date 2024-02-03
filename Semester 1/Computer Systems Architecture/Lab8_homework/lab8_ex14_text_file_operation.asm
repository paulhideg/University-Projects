bits 32
global start        

extern exit,fopen,fprintf,fclose ; need to declare functions as extern
import exit msvcrt.dll
import fopen msvcrt.dll ; need to import the functions
import fprintf msvcrt.dll
import fclose msvcrt.dll

segment data use32 class=data
    ; 14. A file name and a text (defined in the data segment) are given. The text contains lowercase letters, uppercase letters, digits and special characters. Transform all the uppercase letters from the given text in lowercase. Create a file with the given name and write the generated text to file.

    fname db "file.txt",0
    access_mode db "w",0 ; we open the file for writing
    fd dd -1             ; store the file descriptor
    format_write db "%s",0 ; format in which we write in the file
    
    text db "*tHiS iS A nICe tExT123!!",0   ; given text
    len equ ($-text)    ; length of text
    
segment code use32 class=code
    start:
    
        mov ecx,len ; store length in ecx for loop
        cld     ; clear direction flag to move forward with string operations
        mov esi,text    ; store starting address of text
        ; the plan is to parse the text letter by letter and if the letter is uppercase, change it to lowercase
        start_loop:
            mov edi,esi ; destination address is the same as source address
            lodsb       ; al = each letter from the text
            cmp al,'A'
            jl skip
            cmp al,'Z'
            jg skip     ; if not uppercase, skip this letter
                add al,'a'-'A' ; if uppercase, make it lowercase
                stosb          ; replace the uppercase letter with the lowercase
            skip:
        loop start_loop
        
        ;eax = fopen(const char *filename,const char *mode);
        push dword access_mode
        push dword fname
        call [fopen]
        add esp,4*2
        
        cmp eax,0
        je error_opening_file
        
        mov [fd],eax
        
        ;eax = fprintf(FILE *stream,const char *format, [arguments..]);
        
        push dword text
        push dword format_write
        push dword [fd]
        call [fprintf]
        add esp,4*3
        
        push dword [fd]
        call [fclose]
        add esp,4
        
        error_opening_file:
        
        push    dword 0
        call    [exit]