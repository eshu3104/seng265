File Organizer - You were hired to work as part of a team that is building a new web search tool. You will be responsible for analyzing such text
files with web links, downloading the files, and organizing them in a local Unix filesystem. This organizer preprocesses the files by filtering out
certain file types like .gif and .png. It then creates a directory for each web server and subdirectories for each in the URL path. It also downloads files to the appropriate path.

stop-word-remover.c - Reads a plain text file as input and produces an output file with the preprocessed text. Focuses
on the step of removing stop words (Stop words are very common words in a language.
In English, they would be word such as articles such as the, a, an, prepositions such as of, for, to, and conjunctions
such as and, but, yet). Those words are so common that they do ). Thus, output files will be similar to the input
files, but should not have any of the stop words from a given list of stop words.

Text-cleaner.c - Uses tests1/* . It reads character by character from the standard
input and sends a cleaner version to the standard output, doing the following actions:
-When the character is a punctuation sign, skip it, i.e., do not reproduce it in the standard output;
-When the character is an uppercase letter, send to standard output the lowercase version of that letter;
-Otherwise, i.e., when the character is a regular character (letters, numbers, spaces, tabs or newlines), just
send it unchanged to the standard output. 

Stemmer.c - https://tartarus.org/martin/PorterStemmer/c.txt - Refactored code to receive no parameters from command line and read main function instead of stdin
