# ******* FUNCION PRINT ************
# Las formas de usar la funcion print
 
# --- 1. Uso basico ---
# Mostrar una cadena de texto
print("hola mundo")

# --- 2. Usando coma para separar argumentos ---
# Al usar comas, python anade un espacion entre argumentos, cosa que no hace + al concatenar
print("hola","mundo","con","espacios")
print("hola"+"mundo"+"SIN"+"espacios")
# Para incluir un espacio al concatenar hay que hacerlo explicitamente
print("hola"+" "+"mundo"+" "+"CON"+" "+"espacios")

# --- 3. Uso de sep para asignar un separador ---
# sep es un parametro que permite especifica como separar los elementos a imprimir
print("hola","mundo","con","separador", sep=",")

# --- 4. Uso de end como salto de linea ---
# El paramtero end cambia lo que se imprime al final de la llamada a print
# Ademas, hace que el siguiente mensaje se imprima justo despues y no en otra linea
print("hola", end=" ")
print("mundo")

# --- 5. Impresion de variables ---
# Puedes usar print para mostrar el valor de las variables.
frase = "Hola mundo"
print ("Frase:", frase)

# --- 6. Uso de formato con f-string ---
# Las f-string permiten insertar expresiones dentro de cadenas de texto. 
# Al anteponer una f a la cadena de texto, puedes incluir variable directamente dentro de las llaves {}
print(f"Frase: {frase}")

# --- 7. Uso de formato con format ---
# Usando {} como marcadores de posicion, puedes pasar los valores que quieres insertar como argumentos de format
saludo = "Hola"
nombre = "Juan"
print("{}, como estas {}?".format(saludo, nombre))

# --- 8.Impresion con formato especifico ---
# Puedes controlar el formato de los numeros al imprimir.
valor = 3.14159
print("Valor: {:.2f}".format(valor))

# --- 9. Saltos de linea y caracteres especiales ---
# se usa la secuencia de escape \n para un salto de linea
print("Hola\nmundo")

# Para imprimir cadena que contenga comillas simples o dobles dentro de ellas
# Se usa la secuencia de escape para evitar confusiones con la sintaxis de Python
print("Hola soy \"Juan\"")

# Para imprimir una ruta de archivo, tambien se usa la secuencias de escape
print("La ruta de archivo es: C:\\Users\\Usuario\\Desktop\\archivo.txt")
