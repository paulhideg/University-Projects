#include <stdio.h>
/*
29. Read a sentence from the keyboard. Count the letters from each word and print the numbers on the screen.
*/
void cnt_word_letters(char []);
int main()
{
    char s[101];
    printf("\nEnter sequence: ");
    fgets(s,101,stdin);
    cnt_word_letters(s);
	return 0;
}



