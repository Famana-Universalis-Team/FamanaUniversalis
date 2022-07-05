#!/bin/bash

#convert
CONVERT=" iconv -f utf8 -t iso88591"
#loop to convert multiple files 
for  file  in  *.txt; do
     $CONVERT "$file"
done
exit 0