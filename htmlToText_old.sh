#! /bin/bash

# This id.sh file for convert html page for text documents,

javac SourceViewer.java
java SourceViewer https://forums.linuxmint.com/viewtopic.php?t=113309 source.html


./id.sh

# lynx -dump  computers.html|tr '[:upper:]' '[:lower:]' | tr -cs 'a-zA-Z' '\n' | sort | grep -v -x -F -f stopWordList  | uniq -c | sort -nr


#sed -e 's/\.//g' indexsam.txt > out.txt
for file in `ls *.txt`
 do 
textName=`basename $file txt`

 cat $file |tr '[:upper:]' '[:lower:]' | tr -cs 'a-zA-Z' '\n' | sort | grep -v -x -F -f stopWordList > temp.out
 cat temp.out | uniq -c | sort -nr > source.out
 cat temp.out | uniq | spell  > improper.out



#cat $file | #open the file
#tr '[:upper:]' '[:lower:]'| # transform upper letters to lower
#tr -cs 'a-zA-Z' '\n'| #filter only alphabetical charcters
#sort | #sort the list in alphabetical order
#uniq -c | #make a word frequency list
#tail -n +41| #remove the first 41 words which seem to be irrelevant
#head -n +51726 | #remove the lines after 51726 which seem to be irrelevant
#sort -nr| #sort descending with the frequency of terms
#head -n +25153 |  #remove the words that are having a frequency of 2 or less
#tr " *[0-9]* *" " " | #remove the numbers representing frequencies
#cut -d ' ' -f9 | #remove the spaces preceding the words
#sort |
#grep -v -x -F -f stopWordList >> unf

done






