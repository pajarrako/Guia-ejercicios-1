def intercalar(a, b):
    a.append(b) 
    i = len(a) - 2
    while i >= 0 and a[i] > b:
        a[i + 1] = a[i]
        i -= 1
    a[i + 1] = b 
    print(a)
a = [4, 5, 6, 8]
b = 7
intercalar(a, b)
