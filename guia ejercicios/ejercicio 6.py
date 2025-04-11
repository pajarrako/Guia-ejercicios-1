def ProductoDeArreglos(a,b):   
    N=len(a)
    c=[None]*N
    for i in range(N):
        c[i]= a[i] * b[N-(i+1)]
        
    return c
a = [2, 5, 3, 4]
b = [20, 13, 9, 24]

resultado = ProductoDeArreglos(a, b)
print(resultado)
