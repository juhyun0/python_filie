infile=open("proverbs.txt","r")
for line in infile:
	line=line.rstrip()
	word_list=line.split() #공백 단어분리
	for word in word_list:
		print(word);

infile.close()

