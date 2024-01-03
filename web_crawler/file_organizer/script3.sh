#!/bin/bash

# To run this script, type ./script3.sh

filename='filtered_crawling.txt'

cat $filename | while read -r line
do
        ((i++))
        OLDIFS=$IFS
        IFS="/"
        directory_path="web_dirs"
        j=0
        for word in $line
        do
                ((j++))
                if [[ $j -eq 3 ]]
		# if it is the third word, it is the first directory (web server name)
                then
                        directory_path=$directory_path"/$word"
                fi

                if [[ $j -gt 3 && ! $word == *.???* ]]
		# if it is the third word or greater and it is not a file
        	# then concatenate the word with the path to form the directory name
                then
                        directory_path=$directory_path"/$word"
                fi
        done
	# makes corresponding directories
        mkdir -p "$directory_path"
        IFS=$OLDIFS
done

