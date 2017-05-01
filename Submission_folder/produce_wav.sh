rm -rf tempdir
mkdir tempdir
cp /run/user/1000/gvfs/mtp:host=%5Busb%3A002%2C064%5D/Phone/Sounds/*.* /home/lakshya/kaldi-trunk/egs/Music_Player/Submission_folder/tempdir/
avconv -i ./tempdir/*.m4a ./tempdir/rec.wav
cp ./tempdir/rec.wav ./wavdir/