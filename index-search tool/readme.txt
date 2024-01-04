Term Frequency Counter - reads line by line from the standard input and stores the count of each term in a dictionary that uses the term
as key and the term count as value;
- whenever it finds a repeated term existent in the dictionary, it does not erase the existing key, just updates
the current value associated to that key;
- stores the keys sorted lexicographically in the dictionary;
- finally, dumps all key value pairs separated by a space to the standard output, each pair in a different line

Term Document Matrix - Reads all the filenames from the input directory path, sorts them, and saves the sorted terms in
sorted_documents.txt;
 - Reads all the terms from all the files, stores them in memory with no duplicates, and saves a sorted version
of them in sorted_terms.txt;
 - Creates a data structure to store the term frequencies inside a matrix with the number of terms in the set as
the number of rows and the number of documents as the number of columns: how you implement the matrix
is up to you (you may use, for instance, either dictionaries of tuples or lists of lists, but know that one choice
may be more effective for large matrices);
 - For each input document file, it reads line by line the term and term frequency pairs and stores the term
frequency in the term document matrix created above and in the appropriate matrix cell (i.e., the cell with the
row for the given document and the column for the given term);
 - finally, saves the term-document matrix in td_matrix.txt.

Search Tool - First recovers the index files from the index directory (which is a command-line argument given by the user)
and loads into memory both the sorted documents from sorted_documents.txt, the sorted terms from
sorted_terms.txt and the term-document matrix from td_matrix.txt;
- Reads the input from stdin with the term frequencies of the preprocessed query, and converts it into a query
vector;
- Computes the cosine similarity of the query vector with all the document vectors inside the term-document
matrix;
- Sorts the documents by similarity; and
- finally, dumps the similarity and document name pairs into stdout.