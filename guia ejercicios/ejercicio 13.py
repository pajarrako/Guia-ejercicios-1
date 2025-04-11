def busquedaB(a,B):
  for i in range(len(a)):
    if a[i]==B[0]:
      return i
  print("no esta")
a=[2,5,2,3]
B=[4]
busquedaB(a,B)