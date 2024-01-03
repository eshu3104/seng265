#!/bin/bash

# To run this script, type ./script2.sh

filename='filtered_crawling.txt'
i=0
cat $filename | while read -r line
do
    ((i++))
    OLDIFS=$IFS
    IFS='/'
    directory_path=''
    j=0
    for word in $line
    do
        ((j++)) 
        if [ $j -eq 3 ]
        # if it is the third word, it is the first directory (web server name)
        then
            directory_path=$word
        fi
    done
    IFS=$OLDIFS
	# makes directories
    mkdir -p 'web_dirs/'"$directory_path"
done

