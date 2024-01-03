#include <stdio.h>
#include <string.h> // For str functions
#include <ctype.h> // For tolower functions

// Array & element size
int STOP_WORDS_ARR_SIZE = 9; 
int STOP_WORDS_SIZE = 4;


// Function to check if stop word -------------------------------------------------------------------------------------------
int is_stop_word(const char *word, char stop_words[STOP_WORDS_ARR_SIZE][STOP_WORDS_SIZE], int stop_words_arr_size) {

    // Checks if stop word
    for (int i = 0; i < stop_words_arr_size; i++) {
        if (strcmp(word, stop_words[i]) == 0) {
            return 1; 
        }
    }
    return 0; 
}

// Function to remove newline character - truncates line by 1 char if \n is present -------------------------------------------
void remove_newline(char line[]) {
    size_t len = strlen(line);
    if (len > 0 && line[len - 1] == '\n') {
        line[len - 1] = '\0';
    }	
}



// main ----------------------------------------------------------------------------------------------------------------------
int main(int argc, char *argv[]) {
    
    char line[10000];
    char word[1000];
    
    char stop_words[9][4] = {"the", "a", "an", "of", "for", "to", "and", "but", "yet"};

    int is_first_word_in_line = 1; // boolean flag

    // Loop until we reach end of file
    while (fgets(line, sizeof(line), stdin) != NULL) {

        // Remove the newline character, if present
        remove_newline(line);

	// tokenise with space as delimiter
        char *token = strtok(line, " "); 

	// Loop until last word
        while (token != NULL) {
            
            // Check if the token is a stop word
            strncpy(word, token, sizeof(word));

            if (!is_stop_word(word, stop_words, STOP_WORDS_ARR_SIZE)) { // if not stop word, print word
                if (!is_first_word_in_line) { // puts space between every word in sentence except the start
                    printf(" "); 
                }
                printf("%s", word);
                is_first_word_in_line = 0; // changes val of boolean flag
            }

            token = strtok(NULL, " "); // Continue tokenizing with space as the delimiter
        }

        // Print a newline character at end of sentence
        printf("\n");
        is_first_word_in_line = 1; // Reset boolean flag
    }

    return 0;
}
