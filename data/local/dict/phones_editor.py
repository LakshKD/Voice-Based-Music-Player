f = open('lexicon.txt',"r")
f1 = open('nonsilence_phones.txt',"r")
final_phones_dict = {}
for l in f1:
	 p = l.strip()
	 if p not in final_phones_dict.keys():
	 	final_phones_dict[p] = 1
for line in f:
	phones = line.split(' ')
	for i in range(len(phones)):
		if i != 0:
			phn = phones[i].strip()
			if phn not in final_phones_dict.keys():
				final_phones_dict[phn] = 1
f1.close()
f2 = open('new_nonsilence_phones.txt',"w")
for key in final_phones_dict:
	f2.write(key)
	f2.write("\n")

f2.close()
