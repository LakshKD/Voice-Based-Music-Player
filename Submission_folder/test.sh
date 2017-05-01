#!/bin/bash
rm -rf ../result.txt
#touch ../result.txt
parentdir="$(dirname "$PWD")"
echo $parentdir
for i in "$parentdir/$1"/*
do
	file_name=$(basename $i)
	file_name_witout_ext=${file_name%.wav}
	echo $file_name_witout_ext
	result=$(grep -m1 $file_name_witout_ext  $2)
	if [ ! -z "$result" ]; then
		echo $result >> ../result.txt
	fi
done
