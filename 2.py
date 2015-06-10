__author__ = "myatsko"
res = 2
arr = [1, 2, 3]
while arr[2] < 4000000:
    i = arr[1] + arr[2]
    arr.append(i)
    print arr
    if i % 2 == 0:
        res += i
    del arr[0]
print res