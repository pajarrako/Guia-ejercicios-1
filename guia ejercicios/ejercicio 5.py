def mezclarArreglos(arreglo1,arreglo2)
resultado = []
if len(arreglo1)==len(arreglo2):

    for i in range(len(arreglo1)):
        if i % 2 != 0:
            resultado.append(arreglo1[i])
    
    for i in range(len(arreglo2)):
            if i % 2 == 0:
                    resultado.append(arreglo2[i])
    print (resultado)
    
else: print ("error")
