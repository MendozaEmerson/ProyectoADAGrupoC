# BFS, la busqueda primera por anchura

import os


def bfs(grafo, origen):

		print("Muestra el grafo antes del recorrido: \n") #Muestra el grafo a recorrer
		for key, lista in grafo.items():
			print(key)
			print(lista)

		print()
		os.system("pause")
				
		visitados = []
		cola = []

		print("\nLista de recorrido en anchura\n")
		cola.append(origen)

		while cola:
			actual = cola.pop(0)

			if actual not in visitados:
				print("Vertice actual -> ", actual)
				visitados.append(actual)

			for key, lista in grafo[actual]:
				if key not in visitados:
					cola.append(key)


