# ----- LISTAS ----
# Las listas son otra clase en python al igual que los string, int, float, etc
to_do = ["Dirigirnos al hotel", 
         "Ir a almorzar",
         "Visitar un museo",
         "Volver al hotel"]

print(to_do)

# Las listas pueden almacenar diferentes tipos de datos

numbers = [1,2,3,4, "cinco"]
print(type(numbers))

mix = ["uno", 2, 3.14, True, [1,2,3]]
print(mix)

# Al igual que con las cadenas, podemos consultar el numero de datos almacenados
print(len(mix))

#Tambien podemos hacer uso de la indexacion
print("Primer elemento: ", mix[0])
print("Segundo elemento: ", mix[1])
print("Ulitmo elemento: ", mix[1])

# Al igual que con las cademas, podemos hacer slicing (partir)
string = "Hola mundo"
print("Corte desde el primer al tercer elemento:", string[0:3])
# En el slicing, se escribe desde donde hasta donde sin incluir el final
# Tambien podemos dejar vacio la primera parte y se sobre entiende que parte del inicio
print("Corte desde el primer al tercer elemento:", mix[:3])
# Asi mismo, para dar a entender que se llega hasta el final, tambien se puede dejar vacio
print("Corte desde el primer al tercer elemento:", mix[:])


# *** METODOS DE LAS LISTAS ***

# --- APPEND ---
# Anadir elementos a una lista al final
mix.append(False)
print(mix)
# Para anadir un elemento a una lista que esta dentro de otra lista
# primero hay que acceder al elemento que es una lista
mix[-2].append(4)
print(mix)

# --- INSERT ---
# Con insert podemos agregar un elemento a la lista, pero podemos escoger la posicion tambien
mix.insert(2,["a","b"])
print(mix)

# --- INDEX ---
# Consultar el indice de un elemento dentro de una lista
# Pero solo devuelve la primera aparicion del elemento dentro de la lista
mix.append(["a","b"])
print(mix)
print(mix.index(["a","b"]))

# **** FUNCIONES *****

# ---  MAX / MIN ----
# Devolver el numero mayor o menor de la lista
numbers2 = [1, 5, 90, 89, 25, 78]
print("El numero mayor de la lista:", max(numbers2))
print("El numero menor de la lista:", min(numbers2))

# --- del ---
# Eliminar un elemento de una lista
del numbers2[-1]
print(numbers2)
# O tambien una porcion de los datos
del numbers2[:2]
print(numbers2)
# O toda la lista
del numbers2
print(numbers2)