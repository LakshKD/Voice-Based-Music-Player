import os
import time
import vlc

genre_list = [] #contains list of genres

genre_file = open("genre_list","r")

for line in genre_file:
    line = line.replace("\n","")
    genre_list.append(line)
    
genre_song_dict = {}

songs = []

genre_song_file = open("genre_with_songs","r")

for line in genre_song_file:
    line = line.replace("\n","")
    line = line.split(" ")
    genre = line[0]
    song = line[1]
    if genre in genre_song_dict:
        genre_song_dict[genre].append(song)
    else:
        genre_song_dict[genre] = [song]
    songs.append(song)



def get_transcription_from_wav(wavdir):
    bashCommand = './asr.sh '+wavdir
    os.system(bashCommand)
    f = open('mono_dec.txt',"r")
    f1 = open('tri_dec.txt',"r")
    ret_mono = ""
    ret_tri  = "" 
    for l in f:
        ret_mono = l

    for l1 in f1:
        ret_tri = l1
    
    decoding = []
    decoding.append(ret_mono)
    decoding.append(ret_tri)
    return decoding


def editDistDP(str1,str2):

    m = len(str1)
    n = len(str2)

    dp = [[0 for x in range(n+1)] for x in range(m+1)]
 
    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i  
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1],        # Insert
                                   dp[i-1][j],        # Remove
                                   dp[i-1][j-1])    # Replace
 
    return dp[m][n]
    
def check_if_genre_keyword(str):
    if(editDistDP(str,"genre") <= 3):
        return 1
    else:
        return 0
        
def check_if_genre(str):
    min = 10
    ret = ""
    for genre in genre_list:
        ed = editDistDP(str,genre)
        if(ed <= min):
            min = ed
            ret = genre
    if(min < len(str)/2): 
        return ret
    else:
        return ""
            
def check_if_song(str):
    min = 20
    ret = ""
    for song in songs:
        ed = editDistDP(str,song)
        if(ed <= min):
            min = ed
            ret = song
    if(min < len(str)/2): 
        return ret
    else:
        return ""
    
def display_genre_list():
    print "\n"
    print "YOU SAID GENRE, now here is list - "
    for genre in genre_list:
        print genre
    print "\n"
        
def display_songs_under_genre(str):
    print "\n"
    print "YOU SAID ",str," Now here is list of songs under it"
    for song in genre_song_dict[str]:
        print song
    print "\n"
            
def play_song(str):
    print "You asked to play song ",str
    print "ENJOY THE SONG"
    path = "songs/" + str + ".mp3"
    p = vlc.MediaPlayer(path)
    p.play()
    time.sleep(60)
    p.stop()
    print str
    print "\n"
    
while(1):


    time.sleep(12)
    bashCommand = './testing.sh'
    os.system(bashCommand)
    
    if(os.listdir("wavdir") != []):
        
        decoding = get_transcription_from_wav("wavdir") 
        #str = "sathiya"
        str_mono = decoding[0].strip()
        str_tri = decoding[1].strip()
        str_mono = str_mono.replace(" ","_")
        str_tri = str_tri.replace(" ","_")

	print " Mono transcription is ",str_mono
    	print " Tri transcription is " ,str_tri 
        
        song1 = check_if_song(str_mono)
        song2 = check_if_song(str_tri)
        genre1 = check_if_genre(str_mono)
        genre2 = check_if_genre(str_tri)
        
        song = song1
        if (song == ""):
            song = song2
        genre = genre1
        if (genre == ""):
            genre = genre2

        if(check_if_genre_keyword(str_mono)):
            display_genre_list()
        elif(len(genre)>0):
            display_songs_under_genre(genre)
        elif(len(song)>0):
            play_song(song)
        else:
            print "Please say clearly"
             
        


        
                 
    
