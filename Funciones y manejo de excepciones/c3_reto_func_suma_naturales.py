# ---------- RETO RECURSIVIDAD SUMA DE NUMEROS NATURALES ---------------
# Si queremos la suma de numeros naturales del 4 seria 4 + 3 + 2 + 1 = 10
# Caso base -> s(0) = 0 , s(1) = 1
# Caso recursivo -> s(n) = n + s(n-1)

def sumaNatural(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + sumaNatural(n-1)

print(sumaNatural(8))