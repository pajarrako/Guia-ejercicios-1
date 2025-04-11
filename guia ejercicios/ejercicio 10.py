def productoEscalar(a,b):
  res=0
  binv=b[::-1]
  if len(a)==len(b):
    for i in range(len(a)):
      res += a[i] * binv[i]
    return res
  else:
    print("a y b tienen que tener la misma cantidad de numeros")
a=[6,7,4,2]
b=[8,6,4,2]
print (productoEscalar(a,b))
