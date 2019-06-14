j=input()
j=list(j)
j[::2],j[1::2]=j[1::2],j[::2]
print(*j,sep='')
