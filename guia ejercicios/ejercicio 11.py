def busquedaL(a,L):
  pv=[]
  if L not in a:
     print("No se encuentra L")


  for i in range(len(a)):
 
    if L == a[i]:
   
      pv.append(i)
      print (pv)
     
   




a=[1,4,2,3]
L=0
busquedaL(a,L)