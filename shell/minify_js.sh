#!/bin/sh
# combine and minify multiple js files

foreachd(){
for file in ${1}/*
do
        if [ "${file##*.}" = "js" ]
        then
           uglifyjs --ascii -nm -nc --overwrite $file
           echo $file
        fi

        if [ -d $file ]
        then
                foreachd $file
        fi
done
}

if [ $# -gt 0 ]
then
    foreachd $1
else
    foreachd .
fi
