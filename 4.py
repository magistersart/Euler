__author__ = 'myatsko'
pal = 0
for i in range(100,999):
    for j in range(100,999):
        num = str(i * j)
        if num[0] == num[len(num)-1]:
            if num[1] == num[len(num)-2]:
                if num[2] == num[len(num)-3]:
                    if pal < int(num):
                        pal = int(num)
print pal
