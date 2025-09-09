# ------ COMPREHENSION LISTS -------
# El expreso de python con las que podemos crear listas de manera mas eficiente con una sola linea de codigo
# Estructura: list comprehensions> [expresion for iten in iterable if condicion]

# Lista de cuadrados de un rango
squares = [x**2 for x in range(1,11)]
print("Cuadrados:",squares)

# Lista de transformacion de grados celcius a fahrenheit
celsius = [0, 10, 20, 30, 40]
fahrenheit = [(temp * 9/5)+32 for temp in celsius]
print("Temperatura en F:", fahrenheit)

# Lista para hallar los numeros pares
evens = [x for x in range(1,21) if x % 2 ==0]
print(evens)

# Hacer la transpuesta de una matriz
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

transposed = [[row[i] for row in matrix] for  i in range(len(matrix[0]))]

print(matrix)
print(transposed)