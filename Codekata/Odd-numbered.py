n,m=map(int,input().split())
s=[int(i) for i in input().split()]
h=[]
for j in s:
  if(j%2!=0):
    h.append(j)
print(h[m-1])
