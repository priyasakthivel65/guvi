g=input()
d=0
for i in g:
  if((i=='0')|(i=='1')):
    d=d+1
if(d==len(t)):
  print('yes')
else:
  print('no')
