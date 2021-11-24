
from DepthFirstSearch import dfs
from BreadthFirstSearch import bfs

# Importacion de la libreria openCV
import cv2

# Cargar imagen y lo muestra en escala de grises
img = cv2.imread('images/dory.jpg',0)
#cv2.imshow('imagen de dory',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

graph = {"A":["D","C","B"],
    "B":["E"],
    "C":["G","F"],
    "D":["H"],
    "E":["I"],
    "F":["J"]}

grafo = {'a': [('p',4), ('j',15), ('b',1)],
         	'b': [('a',1), ('d',2), ('e',2), ('c',3)],
			'j': [('a',15)],
			'p': [('a', 4)],
			'd': [('b',2), ('g',3)],
			'e': [('b',2), ('g',4), ('f',5), ('c',2)],
			'c': [('b',3), ('e',2), ('f',5), ('i',20)],
			'g': [('d',3), ('e',4), ('f',10), ('h',1)],
			'f': [('g',10), ('e',5), ('c',5)],
			'i': [('c',20)],
			'h': [('g',1)] 
		}
print("Recorrido por Profundidad \n")
print(dfs(graph,"B"))
print("\n")
print(bfs(grafo,"d"))
