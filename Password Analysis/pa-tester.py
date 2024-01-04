#!/usr/bin/env python3

import sys
import re

def is_password_valid(password):
    
    ascii_pattern = re.compile(r'^[\x00-\x7F!#\$%\&\(\)*+,\-.\/:;<=>?@\[\]\^_`\{\|\}~]+$') 
    ascii_match = ascii_pattern.match(password)
    
    invalid_reasons = ['0', 'INVALID']
    
    if len(password) < 8:
    	invalid_reasons.append('TOO_SHORT')
    if ascii_match is None:
    	invalid_reasons.append('NONASCII')
        
    if len(password) < 8 or ascii_match is None:
        print(','.join(invalid_reasons))
        return False
    
    return True

    
def analyze_password_strength(password):
	# Assess password strength
    strength = 1
    strength_reasons = []

    # Check for uppercase letters
    if re.search(r'[A-Z]+', password):
        strength += 1
        strength_reasons.append('UPPERCASE')

    # Check for lowercase letters
    if re.search(r'[a-z]+', password):
        strength += 1
        strength_reasons.append('LOWERCASE')

    # Check for numbers
    if re.search(r'\d', password):
        strength += 1
        strength_reasons.append('NUMBER')

    # Check for special characters
    if re.search(r'[!#\$%&\(\)*+,\-.\/:;<=>?\@\[\]\^_`{\|}~]', password):
        strength += 1
        strength_reasons.append('SPECIAL')

    # Check for sequences of three characters
    if re.search(r'(.)\1\1', password):
        strength -= 1
        strength_reasons.append('sequence')
    
    # Output password strength information
    if strength == 2:
        print(f'2,WEAK,{",".join(strength_reasons)}')
    elif strength == 3:
        print(f'3,MEDIUM,{",".join(strength_reasons)}')
    elif strength == 4:
        print(f'4,STRONG,{",".join(strength_reasons)}')
    elif strength == 5:
        print('5,VERY_STRONG,UPPERCASE,LOWERCASE,NUMBER,SPECIAL')
    else:
        print(f'1,VERY_WEAK,{",".join(strength_reasons)}')

    
        
	 

def main():
	""" This script reads a text from standard input,
	analyzes the validity of a password in each line,
	if valid assesses the strength of the password,
	and writes results of the password analysis into
	the standard output  """

	# if arguments provided, show error message
	if len(sys.argv) != 1:
		print("No arguments should be provided.")
		print("Usage: %s" % sys.argv[0])
		return 1;

	# ADD YOUR CODE HERE
	for password in sys.stdin:
		if (is_password_valid(password.strip())):
			analyze_password_strength(password.strip())

	

if __name__ == "__main__":
	main()
