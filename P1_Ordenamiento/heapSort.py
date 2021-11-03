# Para agrupar el subárbol arraigado en el índice i.
# n es el tamaño del montón
def heapify(arr, n, i):
    largest = i  
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
  
    # Vea si el hijo izquierdo de la raíz existe y es mayor que la raíz.
    if l < n and arr[i] < arr[l]:
        largest = l
  
    # Vea si el hijo derecho de la raíz existe y es mayor que la raíz.
    if r < n and arr[largest] < arr[r]:
        largest = r
  
    # Cambie la raíz, si es necesario 
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]  # intercambio 
  
        heapify(arr, n, largest)
  
# La función principal para ordenar una matriz de tamaño dado. 
def heapSort(arr):
    n = len(arr)
  
    # Dado que el último nodo padre estará en ((n // 2) -1), podemos comenzar en esa ubicación. 
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
  
    # Elementos extraídos uno por uno 
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   # intercambio
        heapify(arr, i, 0)
  
arr = [ 12, 11, 13, 5, 6, 7]
heapSort(arr)
n = len(arr)
print ("La matriz ordenada es: ")
for i in range(n):
    print ("%d" %arr[i]),