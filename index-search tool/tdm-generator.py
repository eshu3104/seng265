#!/usr/bin/env python3

# Libraries used
import os
import sys

# CONSTANTS - FILES TO BE CREATED
SORTED_DOCS = "sorted_documents.txt"
SORTED_TERMS = "sorted_terms.txt"
TERM_DOC_MATRIX = "td_matrix.txt"

def write_sorted_dir(input_path, output_path):
	
	# Sorts list of files in input_path
	file_list = sorted(os.listdir(input_path))
	
	# Create output_path if it doesn't exist
	if not os.path.exists(output_path):
		os.mkdir(output_path)
	
	# Create a txt file that contains the sorted filenames
	with open(output_path + "/" + SORTED_DOCS, "w") as filenames:
		for filename in file_list:
			filenames.write(filename + "\n")

def write_sorted_unique_terms(input_path, output_path):
	
	# Access the filenames
	with open(output_path + "/" + SORTED_DOCS, "r") as sorted_docs:
		
		line_list = []
		word_list = []

		# Iterate through the filenames		
		for filename in sorted_docs:
			
			# Open each filename
			with open(input_path + "/" + filename.strip(), "r") as input_doc:
				
				# Add each word to the list				
				for line in input_doc:
					line_list.append(line.split())
				for word in line_list:
						word_list.append(word[0])
		
		# Get unique terms and sort list
		word_list = list(set(word_list))
		word_list.sort()
					
		# Create a .txt file that holds the sorted list of terms			
		with open(output_path + "/" + SORTED_TERMS, "w") as terms:
			for term in word_list:
				terms.write(term + "\n")
				
				
def create_matrix(input_path, output_path):
	 # Matrix is dict of tuples
    matrix = {}
    
    # Create iterable and count rows
    with open(output_path + "/" + SORTED_TERMS, "r") as st:
        terms = st.readlines()
        rows = len(terms)
    
    # Create iterable and count columns
    with open(output_path + "/" + SORTED_DOCS, "r") as sd:
        doc_lines = sd.readlines()
        columns = len(doc_lines)
        
        # Iterate over filenames
        for j, filename in enumerate(doc_lines):
        		# Create list of lists where sublists are term, frequency pairings
            line_list = []
            with open(input_path + "/" + filename.strip(), "r") as input_doc:
                for line in input_doc:
                    line_list.append(line.split())
            # Iterate over sorted terms
            for i, term in enumerate(terms):
            	 # Set boolean flag
                found = False
                # iterate of term, frequency pairings
                for element in line_list:
                	  # Check if sorted term is equal to term in file
                    if term.strip() == element[0]:
                    		# Update dictionary and boolean flag
                        matrix[(i, j)] = int(element[1])
                        found = True
                if not found:
                	  # If row, column aren't in dictionary, create new entry with value of 0
                    if (i, j) not in matrix:
                        matrix[(i, j)] = 0

	# Create a .txt file that writes the rows, columns and matrix
    with open(output_path + "/" + TERM_DOC_MATRIX, "w") as values:
    	  # Write number of rows and columns
        values.write(f"{rows} {columns}\n")
        
        # Write value to file if key is present in matrix, else write 0. No spaces in last columns  
        for r in range(rows):
        	for c in range(columns):
        		if c != max(range(columns)):
        			if (r,c) in matrix:
        				values.write(f"{matrix[(r,c)]} ")
        			else:
        				values.write("0 ")
        		else:
        			if (r,c) in matrix:
        				values.write(f"{matrix[(r,c)]}")
        			else:
        				values.write("0")
        			
        	values.write("\n")
            

def main():
	# Checks number of arguments
	if len(sys.argv)!= 3:
		print("Usage: Path to input directory, Path to output directory")
		quit()
	else:
		# Get input and output path
		input_path = sys.argv[1]
		output_path = sys.argv[2]
		
		# Make sorted_documents.txt, sorted_terms.txt, td_matrix.txt
		write_sorted_dir(input_path, output_path)
		write_sorted_unique_terms(input_path, output_path)
		create_matrix(input_path, output_path)


if __name__ == "__main__":
	main()
	
