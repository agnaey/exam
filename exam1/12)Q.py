l=[1,2,3,3,4,5,5]

l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
print(l1)