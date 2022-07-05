#!/bin/bash

FROM_ENCODING="utf8"
TO_ENCODING="iso88591"
#convert
CONVERT=" iconv  -f   $FROM_ENCODING  -t   $TO_ENCODING"
#loop to convert multiple files 
for  file  in  *.txt; do
     $CONVERT   "$file"
done
exit 0