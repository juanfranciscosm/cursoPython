# ----- EJERCICIOS COMPREHENSION LISTS -------

# 1. Doble de los numeros
# Dada una lista de numeros, crea una nueva lista que contenga el doble de cada numero usando una List Comprehension

numbers = [1,2,3,4,5]
doble_num = [x*2 for x in numbers]
print(numbers)
print(doble_num)

# 2. Filtrar y transforar en un solo paso.
# Tienes una lista de palabras y quieres obtener una nueva lista con las palaras que tengan mas de 3 letras y esten en mayuscula

words = ["sol", "mar", "MONTANA", "rio", "estrella"]
words_select = [x for x in words if len(x)> 3 and x == x.upper() ]
print(words)
print(words_select) 

# 3. Crear un Diccionario con List Comprehension
# Tienes dos listas, una de clave ["nombre","edad","ocupado"] y otra de valores ["Juan","30","ingeniero"]. Crea un diccionario combinando ambas listas usando una list comprehension

claves = ["nombre","edad","ocupado"]
valores = ["Juan","25","ingeniero"]
diccionario = [{claves[i]:valores[i]} for i in range(3)]
print(diccionario)

# 4. Anidacion de List Comprehension
# Dada una lista de listas (una matriz) calcula la matriz traspuesta utilizando una List Comprehension anidad
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

trasposed = [[row[i] for row in matriz] for i in range(3)]
print(trasposed)

# 5. Extraer informacion de una lista de diccionarios
# Dada una lista de diccionarios que representan personas. Extraer una lista de personas que viven en "Madrid" y tienen mas de 30 anios

personas = [
    {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"},
    {"nombre": "Ana", "edad": 32, "ciudad": "Madrid"},
    {"nombre": "Pedro", "edad": 35, "ciudad": "Barcelona"},
    {"nombre": "Laura", "edad": 40, "ciudad": "Madrid"}
]

personas_selected = [p["nombre"] for p in personas if p["edad"]>30 and p["ciudad"]=="Madrid"]
print(personas_selected)

# 6. List Comprehension con un else
# Dada una lista de numeros, crea una nueva lista multiplicando por 2 los numeros pares y dejando los impares como estan

numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_num = [x *2 if x%2 == 0 else x for x in numbers2 ]
print(numbers2)
print(list_num)
