
# Ordenamiento por el metodo insertion sort ideal para arreglos cortos

def insertion_sort(array):    
    j = 0
    while j < len(array):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] > key:
            array[i + 1] = array[i]
            i -= 1  
        array[i + 1] = key
        j += 1  
    return array

numbers = [10, 4, 5, 8, 7, 2]
numbers1 = [0,0,1,78,3,4]
print("Primer Arreglo: ")
print(numbers)
print(insertion_sort(numbers))
print("   ")
print("Segundo Arreglo: ")
print(numbers1)
print(insertion_sort(numbers1))