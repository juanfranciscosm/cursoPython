# *** DICCIONARIOS ***
# Los diccionarios son una estructura que almacena 2 datos: clave + valor
numbers = {1:"uno",2:"dos",3:"tres"}
print(numbers)

# Aqui, para acceder a la informacion se usan las claves, no el indice como en las listas
print(numbers[2])

# Para eliminar un elemento de un diccionario es igual que con las listas, pero usando la clave
information = {"nombre":"Juan",
               "apellido":"Sanchez",
               "altura":1.70,
               "edad":25}

print(information)
del information["edad"]
print(information)


# Metodo para sacar un diccionario de las claves
claves = information.keys()
print(claves)
print(type(claves))

# Metodo para sacar los valores en el diccionario
values = information.values()
print(values)

# Metodo para extraer los pares de clave-valor, separado en duplas
items = information.items()
print(items)


# Diccionario de diccionarios para hacer una agenda de contactos
contacts = { "Juan": { "apellido":"Sanchez",
                      "altura":1.70,
                      "edad":25},
             "Xavier": {"apellido":"Sanchez",
                        "altura":1.70,
                        "edad":22}
               }

print(contacts["Juan"])