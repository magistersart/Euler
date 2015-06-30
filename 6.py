__author__ = 'myatsko'
sqrsum = 0
sumsqr = 0
for i in range(101):
    sumsqr += i**2
    sqrsum += i
sqrsum = sqrsum * sqrsum

print sqrsum-sumsqr
