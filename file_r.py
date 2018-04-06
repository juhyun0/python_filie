#전체 텍스트 읽어서 화면에 출력
infile=open("phones.txt","r")
lines=infile.read()
print(lines)

#파일에서 전체 데이터 읽는 함수
infile=open("phones.txt","r")
lines=infile.readlines() #한 번에 파일의 모든 줄 읽는다
print(lines)

infile.close()


infile=open("phones.txt","r")
line=infile.readline().rstrip()
while line != "":
	print(line)
	line=infile.readline().rstrip()
infile.close()

infile=open("phones.txt","r")
for line in infile:
	line=line.rstrip()
	print(line)

infile.close()



