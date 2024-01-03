#!/bin/bash

# To run this script, type ./script4.sh


filename="filtered_crawling.txt"

# Saves old IFS=" "
OLDIFS="$IFS"

cat $filename | while read -r line
do
	# Set IFS to /
	IFS="/"
	set -- $line

	# Checks for dirs
	if [[ "line" == */ ]]
	then
		name="index.html"
		dir_path="${@:2:(( $# - 1 ))}"
	
	# Checks for .html and .txt
	elif [[ "line" == *html ]] || [[ "$line" == *txt ]]
	then
		name="${!#}"
		dir_path="${@:2:(( $# - 2 ))}"
	# Appends .html to everything else
	else
		name="${!#}.html"
		dir_path="${@:2:(( $# - 2 ))}"
	fi
	
	# Renames files and downloads them into respective dirs
	dir_path="${dir_path// //}"
	curl -s "$line" > "$name"
	mv "$name" "web_dirs/$dir_path"
	# Resets IFS
	IFS="$OLDIFS"
done
