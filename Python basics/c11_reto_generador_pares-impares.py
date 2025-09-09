# ----------- RETO GENERADOR DE NUMEROS PARES E IMPARES -------------
def gen_pares(limite):
    a = 0
    while a < limite:
        yield a
        a += 2

def gen_impares(limite):
    a = 1
    while a < limite:
        yield a
        a += 2

print("Pares:")
for p in gen_pares(10):
    print(p)

print("Impares:")
for i in gen_impares(10):
    print(i)