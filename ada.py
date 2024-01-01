from fractions import Fraction as F
import time

# Imponerande snabbt jmf med matrisinversion.
# v20 är en array som innehåller de tidigare Bernouillitalen.

def f(v20):
    n = len(v20) - 1             # indicates which Bernoulli number is being calculated
    v13 = F(n,6) - F(2*n-1, 4*n+2)                     # 6
    v06 = 2 * n      # 1
    v07 = 2                       # 8
    v11 = n                       # 9

    for i in range(2, n):
        v11 *= F(v06-1, v07+1) * F(v06-2, v07+2)        # 15-16
        v06 -= 2
        v07 += 2
        v13 += v20[i] * v11                 # 22

    print('e',n,v13)

    v20[n] -= v13                 # 24
    n += 1                       # 25

def bn(n):
    v20 = [0]
    for i in range(n):
        v20.append(0)
        f(v20)
    print(v20)

start = time.time_ns()
bn(10)
print((time.time_ns()-start)/10**6)