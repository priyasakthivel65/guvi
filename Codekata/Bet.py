m=int(input()
v=0
b,r=map(int,input().split())
for j in range(b+1,r):
  if(j==m):
    v=1
if(v==1):   
  print("yes")
else:
  print("no")
