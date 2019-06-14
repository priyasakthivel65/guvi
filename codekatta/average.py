c=int(input())
t=[int(j) for j in input().split()]
sum=0
for i in t:
  sum=sum+i
  n=sum//c
print(n)
