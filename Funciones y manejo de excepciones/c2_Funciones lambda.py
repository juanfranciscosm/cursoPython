# ******** FUNCIONES LAMBDA *********
# Usadas para operaciones sencillas. Funcion anonima

add = lambda a, b: a + b
print(add(10,4))

multiply = lambda a,b : a*b
print(multiply(5,6))


# *** MAP() + LAMBDA EN LISTAR ***
# Cuando trabajamos con listas y queremos aplicar una funcion a cada uno de los elementos de la lista usamos la funcion map y lambda

# Ejmplo> cuadrado de cada numero
numbers = range(11)
squared_numbers = list(map(lambda x: x**2, numbers))
print("Cuadrador:", squared_numbers)

# Uso de funcion filter() para discriminar los datos que quiero sacar de una lista
# Obtener pares 
even_numbers = list(filter(lambda x: x%2 == 0, numbers))
print("Pares:", even_numbers)