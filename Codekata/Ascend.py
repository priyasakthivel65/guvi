a=int(input())
b=list(map(int,input().split()))
C=b[:]
C.sort()
for V in range(0,len(b)):
  if(b[V]!=c[V]):
    print(V)
    break
