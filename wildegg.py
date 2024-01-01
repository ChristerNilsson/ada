from fractions import Fraction as F
import time

# ada är cirka 80 ggr snabbare än wildegg.
# Dock, räknar ada inte ut polynomen, bara Bernoulli-talen.

TS = [[1]]
SS = [[1]]

def nextT(TS):
	T = TS[-1]
	last = T[-1]
	res = [0] * (len(T)+1)
	res[0] = -T[0]
	res[len(T)] = last + 1
	for i in range(1,len(T)):
		res[i] = T[i-1] - T[i]
	TS.append(res)
	return res

# assert nextT(TS) == [-1,2]
# assert nextT(TS) == [1,-3,3]
# assert nextT(TS) == [-1,4,-6,4]

def add(p1,p2): # adderar två polynom
	n = max(len(p1),len(p2))
	res = [0] * n
	for i in range(n):
		a = 0 if i>=len(p1) else p1[i]
		b = 0 if i>=len(p2) else p2[i]
		res [i] = a+b
	return res

assert add([1],[1,1]) == [2,1]
assert add([1,1],[1]) == [2,1]
assert add([1,2],[3,4]) == [4,6]

def mul(p,k): # multiplicerar ett polynom med en konstant. k kan vara en Fraction
	return [item * k for item in p]

assert mul([1,2],3) == [3,6]

def nextS(T):
	n = len(T)
	p = [0] * (n-1)
	p.append(1)
	for i in range(n-1):
		p1 = mul(SS[i],-T[i])
		p = add(p,p1)
	p = mul(p,F(1,n))
	SS.append(p)
	return p

start = time.time_ns()
for i in range(100):
	nextT(TS)
	item = nextS(TS[-1])
	print(i+1,':', ' '.join([str(fr) for fr in item]))
print((time.time_ns() - start)/10**6)
