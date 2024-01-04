#!/usr/bin/env python3

import sys

def sort_unique_words():
    
    line_list = []
    word_list = []

    # Reads line from stdin and makes the words elements. Removes newline.
    for line in sys.stdin:
        line_list.append(line.strip().split())
    # Flattens list
    for element in line_list:
        for word in element:
            word_list.append(word)
    # Keep only the unique words
    word_list = list(set(word_list))
    # Sort list
    word_list.sort()
    # Return list
    return line_list, word_list
    

def counter(line_list, word_list):
    
    counter_dict = {}
    
    # Iterate through list of unique words
    for word in word_list:
        counter = 0
        # Iterate through each line
        for line in line_list:
            # Add to counter if word in line
            counter += line.count(word)
        # Update item in dictionary
        counter_dict.update({word:counter})


    # Print dictionary
    for word, counter in counter_dict.items():
        print(word, counter)    
    
        

def main():

    line_list, word_list = sort_unique_words()
    counter(line_list, word_list)

    


if __name__ == "__main__":
    main()
