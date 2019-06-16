s,p,d=list(map(int,input().split()))
c=0
for i in range(1,d+1):
  v+=s+(i-1)*p
print(v)
