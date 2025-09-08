# Ver el tipo de dato de una variable
name = " Juan "
last_name = " Sanchez "
caracter  = "J"
print(type(name))

#Hay tres maneras de representar cadenas de texto
# 1. Comillas dobles
# 2. Comillas simples
print('Juan')
# 3. Comillas triples (3 comillas simples) Para escribir con saltos de linea
print('''Juan
Que te parece''')

# La cadena tiene indexacion empezando el primer caracter en la posicion 0
print(name[0]) # Primera letra de la variable name
# Si tratamos de traer un indice que no existe en la cadena saltara error
# print(name[40]) #Error out of the range

#para ir a la ultima letra simpre, vamos hacia atras desde el cero.
print(name[-1]) #Ultima letra de la variable name

# --- CONCATENACION ---
# Con cadenas podemos hacer 2 operacione
# 1. Concatenacion - unir cadenas o sumarlas
print(name + " " + last_name)
# 2. Repeticion o multiplicacion
print(2*(name+" "))

#Una buena practica es usar en todo el codigo o comillas simples o todo con comillas dobles

# --- FUNCION LEN ---
#Tambien podemos consultar la longitud o cuantos caracteres tiene una cadena
print(len(name))
print(len(last_name))
#len() es una funcion, pero tambien hay metodos/funciones propios de string con sintaxis diferente.


# ---- METODO LOWER ---
# Convertimos todos los caracteres de una cadena a minusculas
print(name.lower())

# --- METODO UPPER ---
# Convertimos todos los caracteres de una cadena a mayuscula
print(name.upper())

# --- METODO STRIP ---
# Eliminamos los espacios al inicio y al final de la cadena
print(name.strip())
