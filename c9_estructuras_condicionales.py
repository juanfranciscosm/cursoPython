# ***** ESTRUCTURAS CONDICIONALES *****

# --- USO DE IF ---
x = 4
if x > 5 :
    print("Dentro del if: X es mayor que 5") # Siguiente nivel de identacion es lo que ejecuta el if si se cumple la condicion

print("Afuera del if")

# --- USO DE ELSE ---
# Else se usa para el caso en el que la condicion del if sea falsa, se ejecuta lo que este en esta seccion
y = 6
if y > 5 :
    print("Dentro del if: Y es mayor que 5")
else:
    print("Dentro del else: Y NO es mayor que 5")

# --- USO DE ELIF ---
# ELIF va despues del if y se evalua en caso de que el if o elif anterior sea falso.
# A diferencia del else, este evalua otra condicion para ejecutar el codigo de su seccion, else ejecuta en caso de que el if y los elif anteriores sean falsos todos.
z = 5
if z > 5 :
    print("Dentro del if: Z es mayor que 5")
elif z == 5:
    print("Dentro del elif: Z es igual que 5")
else:
    print("Dentro del else: Z NO es mayor que 5")


# --- EVALUAR MAS DE UNA CONDICION --
x = 15
y = 20
# AND (ambas condiciones deben ser verdadera, para ser verdadera)
if x > 10 and y < 25:
    print("X es mayor que 10 y Y es mayor que 15")

# OR (aunque sea una debe ser verdadera, para ser verdadera)
if x > 10 or y > 25:
    print("X es mayor que 10 o Y es Mayor que 25")

# NOT (niega el valor de verdad de la condicion)
if not x > 10:
    print("X no es mayor que 10")

# --- IFs ANIDADOS ---
# ifs dentro de otro if
is_member = True
age = 14

if is_member: #La variable directamente da el valor de verdad que queremos como condicion, por eso no se compara
    if age >= 15:
        print("Tienes acceso ya que eres miembro y eres mayor o igual a 15 anios")
    else:
        print("No tienes acceso ya que eres miembro, pero menor a 15 anios")
else:
    print("No eres miembro y NO TIENES ACCESO")