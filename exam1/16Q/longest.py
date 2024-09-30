f=open('exam/exam1/16Q/exam.txt','r')
l=f.readlines()
f.seek(0)
word=0
for i in range(len(l)):
    a=f.readline().strip()
    for i in a:
        if i !=' ':
            word+=1
print(word)