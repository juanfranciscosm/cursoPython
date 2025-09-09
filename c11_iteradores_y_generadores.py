# ********** ITERADORES **********
# Iteradores iteran en los elementos de una lista, pero sin usar indices

# Ejemplo de iterador

# Crear una lista
my_list = [1,2,3,4]

# Obtener el iterador
my_iter = iter(my_list)

# Usar el iterador
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
# Si se termina la iteracion, no se puede volver volviendo a usar next(), salta un error
# print(next(my_iter))
print("********************")

# -------- ITERAR EN CADENAS ---------
# Asi mismo podemos iterar con cadenas
# Creando la cadena
text = "Hola mundo"
# Creando objeto iterador
iter_text = iter(text)

# Iterar en la cadena
for char in iter_text:
    print(char)
print("********************")

# ----- ITERAR PARA DEVOLVER NUMEROS IMPRARES --------
# Crear un iterador para los numeros impares

# limite
limit = 10
# Crear iterador
odd_itter = iter(range(1,limit+1,2))
# Usar iterador
for num in odd_itter:
    print(num)

print("********************")

# *********** GENERADOR *************
# Es una funcion que genera una secuencia de numeros en los que podemos iterar

# Definimos una funcion que retorna un generador que al iterar devuelve el valor que sigue en el orden de los yield (parecido a un return)
def my_generator():
    yield 1
    yield 2
    yield 3 # el uso de yield es lo que hace que se devuelva un generador y no una funcion
    
# Para poder iterar en los valores del generador debe ser con un for, no se puede imprimir directament llamando la funcion
for value in my_generator():
    print(value)

print("********************")
# CREAR SERIE DE FIBONACCI
# 0 1 1 2 3 5 8 13 21 ...
# El valor es la suma de los 2 valores anteriores

def fibonacci(limit):
    a, b = 0, 1 # forma abreviada de escribir a = 0 y b = 1
    while a < limit:
        yield a 
        a, b = b, a+b
    
for num in fibonacci(10):
    print(num)