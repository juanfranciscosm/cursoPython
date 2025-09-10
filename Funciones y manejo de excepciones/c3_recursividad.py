# *********** RECURSIVIDAD ******************
# La recursividad es una tecnica de la programacion, donde un programa se llama a si mismo para poder resolver un problema

# Ejercicio> Hallar el factorial de un numero
# factorial(N) = N * factorial(N-1)
# Caso base N = 0 porque no se puede obtener el factorial de 0
# Caso recursivo N > 0 

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
factorial_5 = factorial(5)

print(factorial_5)

# Uso en la serie de Fibonacci
# Fibonacci -> Caso base F(0) = 0, F(1) = 1
# -> Caso recursivo F(N) = F(N-1) + F(N-2)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

number = 3
print(fibonacci(number))

''' Diferencia principal:
- Recursivo → la función se llama a sí misma hasta llegar al caso base.
- Iterativo → usamos un bucle for o while para acumular el resultado paso a paso.

Ambas dan el mismo resultado, pero:
- El iterativo suele ser más eficiente en Python (consume menos memoria).
- El recursivo es más elegante para entender la definición matemática.'''