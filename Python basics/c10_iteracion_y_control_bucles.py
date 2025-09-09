# ***** BUCLES ******

# -- FOR ---
numbers = [1, 2, 3, 4, 5, 6]
for i in numbers: # Por cada elemeneto en la lista se ejecuta el codigo dentro del for
    print(i)

# *************RANGE *************
# Tambien podemos asignar un rango de datos a recorrer con for con RANGE
print(type(range(10))) # Este es una nueva clase llamada range
# range (start, stop, step) recibe como parametros el numero desde el cual iniciar
# hasta donde debe llegar sin incluir el final y el numero de saltos 

for i in range(0,110,10): 
    print(i)

fruits = ['Manzanas', 'Pera', 'Uva', 'Naranja', 'Tomate' ]
for fruta in fruits:
    print(fruta)
    if fruta == 'Naranja':
        print('Naranja encontrada')
# en est ejemplo el ciclo continua aunque ya se encontro la fruta que se buscaba
# para detener el ciclo cuando se cumpla una condicion, se usa while

#********** WHILE *************
# Mientras (while) se cumple una condicion, se ejecuta el codigo dentro del while varias veces.
x = 0 #La condicional debe modificarse en cada ciclo, o podemos caer en un bucle infinito.
while x<5 : 
    print("Aqui x es igual a",x)
    x += 1 #se suma 1 a x en cada ciclo

# **********BREAK***********
# Si queremos parar el ciclo while en cualquier punto de la ejecucion se usa break
# En este caso cuando se cumple una condicion, se ejecuta break
y = 0
while y<5 :
    if y == 3:
        break # usamos break para detener el while tambien 
    print("Aqui y es igual a",y)
    y += 1