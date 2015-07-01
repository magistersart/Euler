__author__ = 'myatsko'
from math import sqrt
def sundaram(x):
    ilim = (sqrt(2*x+1) - 1) / 2
    a = range(1,x+1)
    for i in range(1,int(ilim)):
        jlim = (x - i) / (2 * i + 1)
        for j in range(i,jlim):
            if i+j+2*i*j in a:
                a.remove(i+j+2*i*j)
    for c in range(len(a)-1):
        a[c] = 2*a[c] + 1
    a.insert(0,2)
    return a

summ = 0
for z in sundaram(2000000):
    summ += z
    print z, summ
