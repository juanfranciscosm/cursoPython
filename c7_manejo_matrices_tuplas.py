# *** MATRICES Y TUPLAS ***
# Las matrices son listas de listas
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

print(matrix) 

# Para llamar datos se hace primero llamando a la fila y luego a la columna.
print("Posicion de fila 1, columna 2:", matrix[1][2]) #6
# Las matrices tienen las mismas propiedades de las listas (datos mutables)

# Las tuplas son un tipo de dato inmutable
numbers = (1,2,3,4,5)
print(numbers)
print(type(numbers))
print(numbers[0])
#Intentamos modificar un elemento de la tupla, pero lanzara un error
#numbers[0] = "unos"
#print(numbers)

# Si creamos la tupla sin los parentesis, python sobrentiende que se trata de una tupla
letters = "a","b","c","d"
print(type(letters))
