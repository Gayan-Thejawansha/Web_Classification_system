#! /bin/bash

#javac SourceViewer.java
#java SourceViewer www.wikipedia.org source.html


# This removeHTMLtags.sh file for convert html page for text documents,
./removeHTMLtags.sh



#sed -e 's/\.//g' indexsam.txt > out.txt
for file in `ls *.txt`
 do
textName=`basename $file txt`
 sed  's/[!@#\$%^";:_{}&*()<>]//g' $file | tr [:upper:] [:lower:]  > ${textName}txt2
done
rm *.txt


for file in `ls *.txt2`
 do
textName=`basename $file txt2`
sed  "s/[^a-z | ]//g" $file  > ${textName}txt3
done
rm *.txt2

for file in `ls *.txt3`
 do
textName=`basename $file txt3`
sed  "/[s]^/d" $file | more > ${textName}txt
done
rm *.txt3


