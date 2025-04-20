def estrictamenteCreciente(a):
    b = 0
    for i in range(1, len(a)):
        if a[i] != a[i - 1]+1: 
            b += 1
    return b

a = [7,8,10,12,13,20]
print(estrictamenteCreciente(a)) 
