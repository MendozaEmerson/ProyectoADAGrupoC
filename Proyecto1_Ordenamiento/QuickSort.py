# Emerson Danny Mendoza Hilasaca

# La funcion divide los elementos del arreglo en dos subarreglos de menores y mayores con respecto a un pivote
# donde el arreglo de menores sera el subarreglo de la izquierda, el pivote como centro y los mayores a la derecha.
# esto se repite para cada subarreglo de manera recursiva.
def sort(lista):
    izquierda = []
    centro = []
    derecha = []
    if len(lista) > 1:
        pivote = lista[0]
        for i in lista:
            if i < pivote:
                izquierda.append(i)
            elif i == pivote:
                centro.append(i)
            elif i > pivote:
                derecha.append(i)
        print(izquierda+["-"]+centro+["-"]+derecha) # Imprime las iteraciones
        return sort(izquierda)+centro+sort(derecha)
    else:
      return lista

miLista = [34,93,19,58,12,28,95,37,23,80,57,82,55,48,21,39,53,65,30,32,84,64,44,68,36]
array = [23,0,456,1,89,2,1,79,23,13,15,19,20,34,56,65,78,89,90,120]

print(miLista)
print(sort(miLista))

print("/n")

print(array)
print(sort(array))