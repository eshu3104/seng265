#!/bin/bash

#To run this script, type ./script1.sh
grep -v -f omitted_extensions.txt crawling_data.txt > filtered_crawling.txt
