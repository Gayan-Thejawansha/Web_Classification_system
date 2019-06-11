#! /bin/sh
#######################################
#for *.html pages
for file in `ls *.html`
 do
fileName=`basename $file html`
lynx -dump $file > ${fileName}txt
done
#######################################

#######################################
#for *.htm pages
for file in `ls *.htm`
 do
fileName=`basename $file htm`
lynx -dump $file > ${fileName}txt
done
#######################################

#######################################
#for *.xml pages
for file in `ls *.xml`
 do
fileName=`basename $file xml`
lynx -dump $file > ${fileName}txt
done
#######################################

#######################################
#for *.php pages
for file in `ls *.php`
 do
fileName=`basename $file php`
lynx -dump $file > ${fileName}txt
done
#######################################
