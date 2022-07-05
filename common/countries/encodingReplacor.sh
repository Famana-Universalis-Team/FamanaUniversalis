#!/bin/bash

FROM_ENCODING="UTF-8"
TO_ENCODING="ISO_8859-1"
#convert
CONVERT=" iconv  -f   $FROM_ENCODING  -t   $TO_ENCODING"
#loop to convert multiple files 
for  file  in  *.txt; do
     $CONVERT   "$file"   -o  "${file%.txt}.txt"
done
exit 0