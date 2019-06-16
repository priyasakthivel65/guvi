s,d=map(int,input().split())
b=s*d
for j in range(0,b+1):
  if(j**2==b):
    print('yes')
    break
else:
  print('no')
