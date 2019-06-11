cat ~/CO227/CO227/example/computing/* ~/CO227/CO227/example/recreational/*| #concatenate all individual files
tr '[:upper:]' '[:lower:]'| #convert uppercase to lowercase
tr -cs 'a-zA-Z' '\n'| #filter only alphabetical charcters
sort | #sort the list in alphabetical order
uniq -c | #make a word frequency list
tail -n +41| #remove the first 41 words which seem to be irrelevant
head -n +51726 | #remove the lines after 51726 which seem to be irrelevant
sort -nr| #sort descending with the frequency of terms
head -n +25153 |  #remove the words that are having a frequency of 2 or less
tr " *[0-9]* *" " " | #remove the numbers representing frequencies
cut -d ' ' -f9 | #remove the spaces preceding the words
sort |
grep -v -x -F -f stopWordList > unf


