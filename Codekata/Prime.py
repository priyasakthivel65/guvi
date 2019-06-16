n=int(input())
if k>0:
  for i in range(2,n):
    if(k%i==0):
      print("no")
      break
  else:
      print("yes")
else:
  print("no")
