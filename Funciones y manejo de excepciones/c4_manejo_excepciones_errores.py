# ************* MANEJO DE EXCEPCIONES Y ERRORES **************

# Codigo para mostrar la jerarquia de excepciones y errores
def print_exception_hierarchy(exception_class, indent=0):
    print(' ' * indent + exception_class.__name__)
    for subclass in exception_class.__subclasses__():
        print_exception_hierarchy(subclass, indent + 4)

# Imprimir la jerarquía comenzando desde la clase base Exception
print_exception_hierarchy(Exception)

# Para capturar estas excpciones se usa la estructura try - except
try:
    divisor = int(input("Ingresa un numero divisor:"))
    result = 100 / divisor
    print(result)
except ZeroDivisionError as e: # Captura las excepciones que se presenten
    print("Error: El divisor no puede ser cero")
    print("Ha ocurrido un error", e)
# Pueden haber mas de una excepcion
except ValueError as e:
    print("Error: Debes introducir un numero valido")
    print("Ha ocurrido un error", e)

# Al tratar una clase de error padre en la jerarquia, se estaria tratando todos los errore hijo tambien
# Mientras mas abajo en la jerarquia se es mas especifico en el error y es lo que se busca.
