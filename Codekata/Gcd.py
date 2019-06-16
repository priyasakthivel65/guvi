c,v=map(int,input().split())
def gcd(c,v):
    if(v==0):
        return c
    else:
        return gcd(v,c%v)
j=gcd(c,v)
print(j)
