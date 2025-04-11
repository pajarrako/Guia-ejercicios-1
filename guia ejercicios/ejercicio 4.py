def productoBooleanos(a):
  aP=0
  aIP=0
  for i in range(len(a)):
    if i % 2 == 0 and a[i] == True:
      aP+=1
    elif i % 2 ==1 and a[i] == False:
      aIP +=1
  return aP * aIP  


a=[True,True,True,False]
print(productoBooleanos(a))