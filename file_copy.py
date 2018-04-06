infilename=input("입력 파일 이름:");
outfilename=input("출력 파일 이름: ");

#입력과 출력을 위한 파일을 연다
infile=open(infilename,"r")
outfile=open(outfilename,"w")

#전체 파일 읽음
s=infile.read()

#전체 파일 씀
outfile.write(s)

infile.close()
outfile.close()

