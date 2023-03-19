#!/bin/bash

wget -O NAVAll.txt http://amfiindia.com/spages/NAVAll.txt

awk -F ';' '{print $4 "," $5}' NAVAll.txt > output.csv

echo "Extraction complete. Output saved in output.csv"


#Steps:
## Download the file from the URL and save it as NAVAll.txt
## Extract the Scheme Name and Asset Value fields and save them in a CSV file