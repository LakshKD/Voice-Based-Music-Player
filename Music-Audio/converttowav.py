import re, glob, os

def convert(files):
    for pathname in glob.glob(files):
	filename= os.path.basename(pathname)
        basename= filename.split('.')[0].strip()
	#bashCommand = "oggdec -o ./wav/"+basename+".wav "+pathname
	#bashCommand = "sox "+pathname+" "+pathname
	bashCommand = "ffmpeg -i "+pathname+" -ar 44100 "+pathname
	#print (bashCommand)
	os.system(bashCommand)
	#oggdec -o ./wav/basename.wav pathname

convert("./train/abhishek1/rock/*.wav")


###### m4a to wav -> avconv -i input.m4a output.wav ####
