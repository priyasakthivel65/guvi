G=input()
m=[]
for i in G:
    if(i.isdigit())==True:
        m.append(i)
print(*m,sep="")
