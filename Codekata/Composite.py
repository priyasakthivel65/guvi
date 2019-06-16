b=int(input())
if b>0:
  for i in range(2,b):
    if(b%i==0):
      print("yes")
      break
  else:
      print("no")
else:
  print("no")
