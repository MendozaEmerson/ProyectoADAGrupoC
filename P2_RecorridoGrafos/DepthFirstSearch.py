# DFS, la busqueda primera por profundidad 

def dfs(graph, source):    
       if source is None or source not in graph:
           return "El grafo no se encuentra en la lista!!"
       path = []
       stack = [source]
       while(len(stack) != 0): # Comprueba si los vecinos han sido visitados
           s = stack.pop()
           if s not in path:
               path.append(s)
           if s not in graph:  
               continue
           for neighbor in graph[s]:  # Agrega los vecinos del nodo hoja a la pila
               stack.append(neighbor)
       return " ".join(path)  # Agrega espacios a los elementos de la lista path


