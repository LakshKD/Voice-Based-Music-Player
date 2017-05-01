#!/bin/bash

rm -rf demo_train
nj=1
dev_nj=1
mkdir demo_train

for NAME in $1/*.wav; do
	NAME=$(echo $NAME| cut -d'/' -f 2)
	speaker='x'
	echo $NAME "/home/lakshya/kaldi-trunk/egs/Music_Player/Submission_folder/$1/$NAME" >> demo_train/wav.scp
	echo $NAME $speaker >> demo_train/utt2spk
	echo $speaker $NAME >> demo_train/spk2utt
done



##############################3 MFCC feature extraction of the utterrance given as argument################################################
./utt2spk_to_spk2utt.pl demo_train/utt2spk > demo_train/spk2utt
# MFCC feature extraction of the utterrance given as argument
./make_mfcc.sh --nj $nj --cmd run.pl demo_train/ make_mfcc/log mfcc
./compute_cmvn_stats.sh demo_train/ make_mfcc/log mfcc


echo "Decoding the dev set using monophone models."
  #./mkgraph.sh lang_test mono mono/graph
	
  ./decode.sh --config conf/decode.config --nj $dev_nj --cmd run.pl \
   	tri1/graph demo_train tri1/decode_dev
  echo "Monophone decoding done."

echo "Decoding the dev set using monophone models."
  #./mkgraph.sh lang_test mono mono/graph
	
  ./decode.sh --config conf/decode.config --nj $dev_nj --cmd run.pl \
   	mono/graph demo_train mono/decode_dev
  echo "Monophone decoding done."  

rm -rf mono_dec.txt
rm -rf tri_dec.txt
#touch ../result.txt
for i in "$1"/*
do
	file_name=$(basename $i)
	file_name_without_ext=${file_name%.wav}
	echo $file_name_without_ext
	result=$(grep -m1 $file_name_without_ext  mono/decode_dev/log/decode.1.log)
	if [ ! -z "$result" ]; then
		echo "${result#* }" >> mono_dec.txt
	fi
done

for i in "$1"/*
do
	file_name=$(basename $i)
	file_name_without_ext=${file_name%.wav}
	echo $file_name_without_ext
	result=$(grep -m1 $file_name_without_ext  tri1/decode_dev/log/decode.1.log)
	if [ ! -z "$result" ]; then
		echo "${result#* }"  >> tri_dec.txt
	fi
done