# defining root kaldi directory
export KALDI_ROOT=`pwd`/../..

#setting paths to useful tools
export PATH=$PWD/utils/:$KALDI_ROOT/src/bin:$KALDI_ROOT/tools/openfst/bin:$KALDI_ROOT/src/fstbin/:$KALDI_ROOT/src/gmmbin/:$KALDI_ROOT/src/featbin/:$KALDI_ROOT/src/lm/:$KALDI_ROOT/src/sgmmbin/:$KALDI_ROOT/src/sgmm2bin/:$KALDI_ROOT/src/fgmmbin/:$KALDI_ROOT/src/latbin/:$KALDI_ROOT/src/lmbin:$PWD:$PATH

# Defining audio data directory 
export DATA_ROOT="/home/abhishek/Documents/asr/kaldi/egs/digits/digits_audio"

#variable that stores path to MITLM library
#mit language modelling toolkit

# Variable needed for proper data sorting
export LC_ALL=C
