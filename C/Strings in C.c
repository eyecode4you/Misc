/* 17/04/22
 * stringsExample.c
 * 
 * Strings in C example
 * We will look at implementing strings in C and some functions we
 * can call on them.
 * 
 * EyeCode4You - do what you like with this code!
 */

/* A note on the structure of strings in C:
 * 
 * Strings in C are handled a bit differently than what 
 * you're probably used to in languages such as Java or Python 
 * (in reality these languages handle strings much the same in the 
 * background but are defined by the programmer in a more user-friendly 
 * way e.g. String x = "Hello";).
 * 
 * C does not have a built-in String data type, instead it uses
 * character arrays to achieve the same effect.
 */

#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int main(){
	//SECTION 1: Creating & Defining Strings in C
		/*1.1: With specified char array size
		 * One way to create a string in C is to declare a char array &
		 * specifiy the length of the word or information you are going 
		 * to store:
		 * 	char myString[10]; - will create an array that stores 10
		 * 	elements
		 * 
		 * Each character in your string will take up an element in the
		 * char array, however when specifying a size you must also add 
		 * a terminator character /0 (also called a NULL character) 
		 * to the end of the char array to indicate the end of the 
		 * string, think of it like an invisible full stop for the word 
		 * or phrase contained within your string, to this effect the 
		 * length of your char array will be the number of characters +1 
		 * (for the NULL Terminator). 
		 * If you omit \0 in your char array definition one will be 
		 * added automatically.
		*/
		
		printf("****SECTION 1****\n");
		
		char text1[9] = {'E', 'y', 'e', ' ', 'C', 'o', 'd', 'e', '\0'};
		
		printf("1.1: %s", text1);//To use string in C with printf use %s
		printf("\nSize of text1 (%d)\n", sizeof(text1));
		
		/*1.2: Without a specific array size
		 * A simpler way to define a string in C is without specifying 
		 * the char array size. Remember, if you omit \0, one will be 
		 * added to the end of the char array implicitly, so below if 
		 * you were to enter "content" the array would contain:
		 * 	c o n t e n t \0
		*/
		
		char text2[] = "4 You!"; // '4', ' ', 'Y', 'o', 'u', '!', '\0'
		printf("\n1.2: %s", text2);
		printf("\nSize of text2 (%d)\n", sizeof(text2));
		
		printf("\n%s %s", text1, text2);
		
		/*SECTION 2: Modifying Strings in C
		 * This section is a bit of a misnomer as what we'll be doing 
		 * isn't actually modifying the character arrays that make up 
		 * our strings, long story about memory allocation short, when 
		 * you define a string in C it's stored in a place that is 
		 * read-only, meaning you don't directly modify the created 
		 * string itself, but rather we work on various copies and new 
		 * strings from our original.
		 * 
		 * Each index of the array contains a single character, starting 
		 * from index 0 e.g. For a char array containing "EyeCode" 
		 * 						Index: 0 1 2 3 4 5 6  7
		 * 						 Char: E y e C o d e \0
		*/
		printf("\n\n\n****SECTION 2****\n");
		
		/*2.1: We can modify individual characters in a string by 
		 * accessing their index and supplying a new character, note 
		 * single quotes '' are used when dealing with single characters
		*/
		char text3[] = "original";
		printf("%s", text3);
		
		text3[0] = 's';
		text3[1] = 'u';
		text3[2] = 'b';
		text3[3] = 'l';
		text3[5] = 'm';
		
		printf("\n%s", text3);
				
		/*SECTION 3: C String Methods
		 * C includes a lot of methods to simplify working with strings.
		 * We will take a look at some useful
		 * Note, to use most string methods in C we must add: 
		 * #include <string.h> to the preprocessor directives
		*/
		printf("\n\n\n****SECTION 3****\n");
		
		char text4[] = "eyecode4you";
		printf("%s", text4);
		
		/*3.1: To get the number of non-null chars in a string use 
		 * strlen() - strlen() function does NOT count the \0 character 
		 * in a string's length as it stops at the first occurence of \0
		 * 
		 * strlen() returns an INTEGER value
		*/
		printf("\nLength of text with no \\0: (%d)", strlen(text4));
		
		/*3.2: To compare different strings we can use strcmp().
		 * 		SYNTAX: strcmp(string1, string2); 
		 * This method returns 0 if the compared strings are equal, 
		 * typically -1 if they aren't. Buffer size isn't compared.
		*/
		char text5[] = "eyecode4you";
		char text6[] = "noteyecode4you";
		char text7[25] = "eyecode4you";
		
		printf("\n\nstrcmp() comparisons:");
		printf("\n%d (eyecode4you)", strcmp(text4, text5));
		printf("\n%d (noteyecode4you)", strcmp(text4, text6));
		printf("\n%d (eyecode4you [25])", strcmp(text4, text7));
		
		//strcmpi() can be used to compare irrespective of case
		char text8[] = "EyEcOdE4YoU";
		printf("\n%d (strcmpi() EyEcOdE4YoU)", strcmpi(text4, text8));
		
		/*3.3: You can concatenate (stick together) strings with the 
		 * strcat() method
		*/
		printf("\n\nstrcat():");
		printf("\n%s", strcat(text5, text6));
		
		/*3.4: You can copy the contents of one string to another using 
		 * strcpy()
		 * 		SYNTAX: strcpy(string1, string2);
		 * string2 will be copied into string 1, including the null \0
		*/
		printf("\n\nstrcpy()");
		
		char stringA[] = "Oh no I'm gonna be overwritten!";
		char stringB[] = "I'm gonna get ya!";
		printf("\nstringA: %s \nstringB: %s", stringA, stringB);
		
		strcpy(stringA, stringB);
		printf("\n\nstringA: %s \nstringB: %s", stringA, stringB);
		
		/*3.5: Lower and Upper case conversions, strrev()
		 * you can use strupr() and strlwr() to convert strings to upper 
		 * and lower case respectively. strrev() can be used to 
		 * reverse your string.
		*/
		printf("\n\nstrupr(), strlwr(), & strrev()");
		
		char caseChanger[] = "eLaStIc";
		printf("\n%s", strupr(caseChanger));
		printf("\n%s", strlwr(caseChanger));
		printf("\n%s", strrev(caseChanger));
		
		/*3.6: toupper() & tolower() can be used to convert single 
		 * characters to upper or lower case, requires <ctype.h>
		*/
		printf("\n\ntoupper() & tolower()");
		char upperlower[] = "beginning";
		
		upperlower[0] = toupper(upperlower[0]);
		printf("\n%s", upperlower);
		
		upperlower[0] = tolower(upperlower[0]);
		printf("\n%s", upperlower);
		
		/*3.7: Character Checks
		 * We can use various methods to perform checks on the 
		 * characters within a string:
		 * 
		 * isupper() - check if uppercase
		 * islower() - check if lowercase
		 * isalpha() - check if letter
		 * isdigit() - check if number 0-9
		 * ispunct() - check if punctuation
		 * isspace() - check if space including \n, \t, etc
		 * 
		 * In C all of these return non-zero if true and zero if false
		 * 
		 * Note all the above functions require <ctype.h>
		*/
		printf("\n\nChecking Characters");
		char checkThis[] = "Eye code88!";
		printf("\n%s", checkThis);
		
		printf("\nchar[0] 'E' isupper()? %d", isupper(checkThis[0]));
		printf("\nchar[0] 'E' islower()? %d", islower(checkThis[0]));
		printf("\nchar[0] 'E' isalpha()? %d", isalpha(checkThis[0]));
		printf("\nchar[0] 'E' isdigit()? %d", isdigit(checkThis[0]));
		printf("\nchar[10] '!' ispunct()? %d", ispunct(checkThis[10]));
		printf("\nchar[3] ' ' isspace()? %d", isspace(checkThis[3]));
		
		/*3.8: Converting strings to integers
		 * To convert string content into an integer we can use the 
		 * atoi() method, this method will read from a string UNTIL it 
		 * encounters a non-number character e.g. "Year 1964" will not 
		 * be converted but "1964 Year" would return 1964 as an int
		 * 
		 * NOTE conversion methods like atoi(), atol(), and atof() 
		 * require the inclusion of <stdlib.h> to use
		*/
		char numberString[] = "123 Hoose Geese";
		printf("\n\n%d", atoi(numberString));
	
	return 0;
}

/*
 * FURTHER READING
 * An in-depth look at working with strings in C from Dionysia Lemonaki 
 * at FreeCodeCamp: 
 * https://www.freecodecamp.org/news/c-string-how-to-declare-strings-in-the-c-programming-language/
 * 
 * Is it possible to modify a string of char in C?: 
 * https://stackoverflow.com/questions/1011455/is-it-possible-to-modify-a-string-of-char-in-c
 * 
 * String methods in C:
 * https://www.dremendo.com/c-programming-tutorial/c-string-methods
*/
