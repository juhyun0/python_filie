outfile=open("phones.txt","w")

outfile.write("홍길동 010-0000-0001")

outfile=open("phones.txt","a") #추가
outfile.write("\n강감찬 010-1234-5681\n")
outfile.write("김유신 010-1234-5682\n")
outfile.write("정약용 010-1234-5683\n")

outfile.close()

