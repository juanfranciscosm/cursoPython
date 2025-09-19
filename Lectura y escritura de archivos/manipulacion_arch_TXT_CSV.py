# ------------ MANIPULACION DE ARCHIVOS TXT Y CSV CON PYTHON ---------------

# Abrimos el archivo en modo lectura r
archivo_lectura = open('Lectura y escritura de archivos/sources/cuento.txt','r')
# archivo_anexar = open('Lectura y escritura de archivos/sources/cuento.txt','a') #agregar texto despues de la ultima linea
# archivo_escritura = open('Lectura y escritura de archivos/sources/cuento.txt','w') 

# METODOS PARA LEER ARCHIVOS
# - Leer todo el archivo: read()
# - Leer una linea a la vez: readline()
# - Leer todas las lineas y almacenarlas en una lista: readlines()

# Leer archivo linea por linea
"""with archivo_lectura as file: # Al usar with, el archivo se cierra automaticamente despues de finalizar las operaciones
    for lineas in file:
        print(lineas.strip()) # Con el metodo strip() se eliminan las espacios en blanco al inicio y final una cadena de texto, en este caso, de cada linea."""


# Leer un archivo y guardar las lineas en una lista
"""with archivo_lectura as file:
    lines = file.readlines()
    print(lines)"""

# Agregar texto al final del archivo
"""with archivo_escritura as file:
    file.write("\n\nBy: ChatGPT again")"""

# Sobreescribir el texto (esto elimina lo que hay y escribe lo que le digamos)
"""with archivo_escritura as file:
    file.write("Se fue todo")"""

# ----------- RETO --------------
#  ¿Cuántas líneas tiene el cuento de Caperucita Roja?
with archivo_lectura as file:
    lines = file.readlines()
    
print("El cuento de caperucita tiene",len(lines), "lineas")
    
