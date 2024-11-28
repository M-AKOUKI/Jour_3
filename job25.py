
for i in range(2,1001):
    x = 0
    for n in range(2,10):
        if i%n == 0:
            x += 1
    if x==1:
        print(i)
