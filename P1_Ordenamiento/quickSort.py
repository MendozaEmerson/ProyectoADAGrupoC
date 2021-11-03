# Archivo actual quickSort.py

# insertionSort.py
# insertionSort()
from insertionSort import insertion_sort

# Segun la pagina https://es.wikipedia.org/wiki/Quicksort    
# Habitualmente se aplica el algoritmo de inserción para secuencias de tamaño menores de 8-15 elementos.
limite = 8

def quick_sort(lista):
    izquierda = []
    centro = []
    derecha = []
    n = len(lista)
    if n > 1:
        pivote = lista[0]
        for i in lista:
            if i < pivote:
                izquierda.append(i)
            elif i == pivote:
                centro.append(i)
            elif i > pivote:
                derecha.append(i)
        print(izquierda+["-"]+centro+["-"]+derecha) # Imprime las iteraciones
        return quick_sort(izquierda)+centro+quick_sort(derecha)
    else:
        if n <= limite:
            insertion_sort(lista)
        else:
            return lista

miLista = [34,93,19,58,12,28,95,37,23,80,57,82,55,48,21,39,53,65,30,32,84,64,44,68,36]
array = [23,0,456,1,89,2,1,79,23,13,15,19,20,34,56,65,78,89,90,120]
arreglo = [78,34,2,1,4]

print(miLista)
print(quick_sort(miLista))
print("    ")
print(array)
print(quick_sort(array))
print("    ")
print(arreglo)
print(quick_sort(arreglo))