import math
G,H=input().split()
G=int(G)
H=int(H)
M=math.gcd(G,H)
print((G*H)//M)
