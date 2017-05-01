#!/bin/bash

# MFCC feature extraction of the uttereance given as argument
./make_mfcc.sh --nj $nj --cmd run.pl demo_train/ make_mfcc/log mfcc
./compute_cmvn_stats.sh demo_train/ make_mfcc/log mfcc


#Aligning the utterance given as argument using the learned model that  is mono
./align_si.sh demo_train lang mono mono_ali

for i in mono_ali/ali.*.gz;
do ./ali-to-phones --ctm-output mono_ali/final.mdl ark:"gunzip -c $i|" -> ${i%.gz}.ctm;
done;

cat mono_ali/*.ctm > mono_ali/merged_alignment.txt

python PhoneID2Phone_Chars.py
python getwordsfromphones.py  final_alignment.txt

i=1
while IFS= read -a line; do
	#printf "%s\n" "${line[@]}"
	tokens=( $line )
	sox $1 word$i.wav trim ${tokens[0]} ${tokens[1]}
	let i++
done < "Start_End_dictionary.txt"
