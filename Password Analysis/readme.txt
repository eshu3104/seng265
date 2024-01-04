1. Reads the input from stdin with the example passwords to be tested, and interprets each line as a single
password (of course, removing the newline character before any analysis).
2. For each password string that comes from stdin, checks its validity first by means of regular expressions;
if invalid, it outputs the string 0,INVALID,[[TOO_SHORT],[NONASCII]] to describe that it is invalid.
Notice that TOO_SHORT or NONASCII will only be printed if the password is invalid for one of more of
such reasons.
3. If the string is valid, it assesses its strength by means of one or more regular expressions, and outputs any of
the following messages according to the strength of the password. Notice that UPPERCASE, LOWERCASE,
NUMBER, and SPECIAL will only be printed if the password has a larger strength for such reasons.
 2,WEAK[,UPPERCASE][,LOWERCASE][,NUMBER][,SPECIAL]
 3,MEDIUM[,UPPERCASE][,LOWERCASE][,NUMBER][,SPECIAL]
 4,STRONG[,UPPERCASE][,LOWERCASE][,NUMBER][,SPECIAL]
 5,VERY_STRONG,UPPERCASE,LOWERCASE,NUMBER,SPECIAL
4. When a sequence of three characters happens, it reduces the strength of the password by one. Notice that in
such cases, sequence will always be printed after any of the other messages.
 1,VERY_WEAK[,UPPERCASE][,LOWERCASE][,NUMBER][,SPECIAL],sequence
 2,WEAK[,UPPERCASE][,LOWERCASE][,NUMBER][,SPECIAL],sequence
 3,MEDIUM[,UPPERCASE][,LOWERCASE][,NUMBER][,SPECIAL],sequence
 4,STRONG[,UPPERCASE][,LOWERCASE][,NUMBER][,SPECIAL],sequence
5. The process is repeated for all the passwords that come from stdin, dumping in different lines of the
stdout the information about each password.