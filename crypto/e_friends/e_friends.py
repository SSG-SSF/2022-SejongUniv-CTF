from sympy import *
from Crypto.Util.number import long_to_bytes, bytes_to_long
from secret import flag
from gmpy import invert

p = randprime(2**511,2**512)
q = randprime(2**511,2**512)
phi = (p-1)*(q-1)
while True:
    #print("new d...")
    d = randprime(0,2**32)
    if gcd(phi,d)==1 and gcd(phi,d**2+2)==1:
        break

print("p =",p)
print("q =",q)
print("d =",d)

e1 = invert(d,phi)
e2 = invert(d**2+2,phi)

n = p*q
c = pow(bytes_to_long(flag.encode()),e1,n)
print(long_to_bytes(pow(c,d,n)).decode()==flag)
with open("output.txt","w") as f:
    f.write("e1 = "+str(e1)+"\n")
    f.write("e2 = "+str(e2)+"\n")
    f.write("n = "+str(n)+"\n")
    f.write("c = "+str(c)+"\n")