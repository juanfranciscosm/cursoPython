# --- OPERACIONES MATEMATICAS AVANZADAS ----

# Operadores numericos
a = 20
b = 6
print("Suma:", a+b)
print("Resta:", a-b)
print("Multiplicacion:", a*b)
print("Division:", a/b)

# --- MODULO ---
# Lo que resta de una division
print("Modulo:", a%b) #cuidado al dividirlo a 0

# --- PARTE ENTERA DE UNA DIVISION ---
print("Parte entera de {} entre {} es".format(a,b), a//b)

# --- POTENCIA ---
print("Potenciacion:", a ** b )

# --- Shortcuts ---
# Se hace la operacion y reasigna el valor a una variable
a += 2 # lo mismo que a = a +2
print(a)
a -= 2
print(a)
a *= 2
print(a)
a /= 2
print(a)
a %= 3
print(a)

# Si se utiliza multiples operadores matematicos se sigue la regla PEMDAS
# 1. Parentesis
# 2. Exponenciacion
# 3. Matematicas
# 4. Division
# 5. Adicion
# 6. Sustraccion

# ejemplo 1 PEMBAS
operation_1 = 2 + 3 * 4
operation_2 = 2 + (3 * 4)
operation_3 = (2 + 3) * 4
print(operation_1)
print(operation_2)
print(operation_3)

# ejemplo  2 PEMBAS
operation_4 = (2+3) * (4**2)/8-1
print(operation_4)


# ---- OPERADORES BOOLEANOS ----
a = 10
b = 10.0
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
print(a == b) #igualdad
print(a != b) #diferente
#Aunque sea valores de diferente tipo, si puede afirmar que son iguales por el valor