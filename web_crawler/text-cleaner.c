#include <stdio.h>
#include <ctype.h>


int main() {
    char letter;

    // Iterate char by char until you reach the end of the file
    while ((letter = getchar()) != EOF) {
	// Check if punctuation
	if (ispunct(letter)) {
	 	// do nothing
            continue;
	// Check if uppercase
        } else if (isupper(letter)) {
		// Convert to lower case and output to stdout
            fputc(tolower(letter), stdout);
        } else {
		// Output char to stdout
            fputc(letter, stdout);
        }
	}

    return 0;
}

