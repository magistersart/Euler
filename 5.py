__author__ = 'myatsko'
i = 232792500
while i > 0:
    count = 0
    for j in range(1,21):
        if i%j == 0:
            count += 1
    if count == 20:
        break
    else:
        i += 1
        print i
print i