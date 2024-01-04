#!/usr/bin/env python3

# Libraries used
import os
import sys
import math

# CONSTANTS - FILES TO BE CREATED
SORTED_DOCS = "sorted_documents.txt"
SORTED_TERMS = "sorted_terms.txt"
TERM_DOC_MATRIX = "td_matrix.txt"

def make_document_dict(input_path):
	
	# Lists of sorted_docs and sorted_terms
	filenames = []
	words = []
				
	with open(input_path + "/" + TERM_DOC_MATRIX, "r") as td_matrix:
			# Skip first line of td_matrix.txt
			next(td_matrix)
			# Create lists of sorted_docs and sorted_terms
			with open(input_path + "/" + SORTED_DOCS, "r") as docs:
				for line1 in docs:
					filenames.append(line1.strip())
				with open (input_path + "/" + SORTED_TERMS, "r") as terms:
					for line2 in terms: 
						words.append(line2.strip())
					# document vector dictionary
					matrix_dict = {}								
					# Iterate over both lists to create keys for dictionary, values = frequencies
					i = 0
					for line in td_matrix:
						j = 0
						for freq in line.split():
							matrix_dict[(words[i],filenames[j])] = freq
							j = j + 1
						i = i + 1
				
	return matrix_dict
				
def make_query_vector(input_path):
	
	query_dict = {} # Intermediate dictionary
	sorted_words = [] # Terms from sorted_terms.txt
	query_vector = [] # Query vector
	
	# Create sorted words list
	with open (input_path + "/" + SORTED_TERMS, "r") as terms:
		for line in terms:
			sorted_words.append(line.strip()) 
	# Default value of key = 0
	for term in sorted_words:
		query_dict[term] = 0
	# Read from stdin	
	for line in sys.stdin:
		term, freq = line.split()
		# Update values of keys
		if term in sorted_words:
			query_dict[term] = int(freq)
	# Create tuple query vector
	for term in sorted(query_dict.keys()):
		query_vector.append(query_dict[term])	
	return tuple(query_vector)
			 
def calc_cosine_similarity(query_vector, document_vector):
	
	dot_query_document = 0
	document_magnitude = 0
	query_magnitude = 0
	
	# Calculate dot product
	for i in range(len(query_vector)):
		product = query_vector[i] * document_vector[i]
		dot_query_document += product
		
	# Calculate magnitude of document_vector
	for j in range(len(document_vector)):
		squared = document_vector[j]**2
		document_magnitude += squared
	document_magnitude = math.sqrt(document_magnitude)
	
	# Calculate magnitude of query_vector
	for k in range(len(query_vector)):
		squared = query_vector[k]**2
		query_magnitude += squared
	query_magnitude = math.sqrt(query_magnitude)
	
	# Calculate cosine_similarity
	cos_sim = round(dot_query_document / (document_magnitude * query_magnitude), 4)
	
	return cos_sim 
	
	
def make_similarity_document_dict(input_path, matrix_dict, query_vector):
	
	# Lists of sorted_docs and sorted_terms
	filenames = []
	words = []
	similarity_document_dict = {}	
	
	with open(input_path + "/" + TERM_DOC_MATRIX, "r") as td_matrix:
			# Skip first line of td_matrix.txt
			next(td_matrix)
			
			# Create lists of sorted_docs and sorted_terms
			with open(input_path + "/" + SORTED_DOCS, "r") as docs:
				for line1 in docs:
					filenames.append(line1.strip())
				with open (input_path + "/" + SORTED_TERMS, "r") as terms:
					for line2 in terms: 
						words.append(line2.strip())
	
	for document in filenames:
		# Make document vector
		document_vector = []
		for term in words:
			freq = int(matrix_dict[(term, document)])
			document_vector.append(freq)
		tuple(document_vector)
		
		# Calculate & store  cosine similarity 
		cosine_similarity = calc_cosine_similarity(query_vector, document_vector)
		similarity_document_dict[cosine_similarity] = similarity_document_dict.get(cosine_similarity, []) + [document]
	
	# Print cosine similarity file pair
	for cosine_similarity in sorted(similarity_document_dict.keys(), reverse=True):
		for document in sorted(similarity_document_dict[cosine_similarity], reverse = True):
			print("%.4f %s" % (cosine_similarity, document))

def main():
	# Checks number of arguments
	if len(sys.argv)!= 2:
		print("Usage: ./search.py input_path")
		quit()
	else:
		# Get input_path
		input_path = sys.argv[1]
		
		matrix_dict = make_document_dict(input_path)
		query_vector = make_query_vector(input_path)
		make_similarity_document_dict(input_path, matrix_dict, query_vector)	
		
if __name__ == "__main__":
	main()

