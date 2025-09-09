# -------------- CALCULADORA CON FUNCIONES ---------------

def add(a,b):
    return a+b
# una buena practica es dejar una linea de espacio entre funciones
def substract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def calculator():
    while True:
        print("Seleccione una operacion")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Dividir")
        print("5. Salir")

        option = int(input("Ingrese su opcion(1,2,3,4 o 5): "))

        if option == 5:
            print("Saliendo de la calculadora ...")
            break
        
        if option in [1,2,3,4]:
            num1 = float(input("Ingrese el primer numero: "))
            num2 = float(input("Ingrese el segundo numero: "))
            if option == 1:
                print("La suna es:", add(num1,num2))
                input("Presiona ENTER para continuar >>")
            elif option == 2:
                print("La resta es:",substract(num1,num2))
                input("Presiona ENTER para continuar >>")
            elif option == 3:
                print("La multiplicacion es:", multiply(num1,num2))
                input("Presiona ENTER para continuar >>")
            elif option == 4:
                print("La division es:", divide(num1,num2))
                input("Presiona ENTER para continuar >>")
        else:
            print("Opcion no valida, por favor intenta nuevamente.")
            input("Presiona ENTER para continuar >>")

calculator()