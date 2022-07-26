from random import *
from sympy import *
from Crypto.Util.number import long_to_bytes, bytes_to_long

while True:
	p = nextprime(randint(10**399,10**400))
	if len(str(p)) != 400:
		continue

	q = int(str(p)[200:] + str(p)[:200])
	if isprime(q):
		break;

n = p*q
e = 65537

f = open('./flag','r')
flag = f.readline()
m = bytes_to_long(flag.encode())
c = pow(m,e,n)


with open('./output.txt','w') as f:
	f.write("N : "+str(n)+'\n')
	f.write("C : "+str(c)+'\n')



