# ------- FUNCIONES ----------
# Las funciones nos permiten almacenar porciones de logica que tienen una tarea especifica
# Las funciones deben crearse antes de llamarse.

def greet(name, las_name):
    print("Hola",name,las_name)

greet("Juan","Sanchez")

# Las funciones pueden recibir mas de un argumento como variables dentro de la logica de la funcion
# Si no hay un valor predeterminado para algun parametro, no se podra llamar la funcion sin pasarle el argumento faltante

def call(number, name = "uknown" ): #no puede haber un argumento sin valor por defecto despues de uno con valor por defecto.
    print("llamando a {} al {}".format(name, number))

call(593990427750)

#Se puede dar los valores de lor argumentos en diferente orden indicando el valor de cada variable
call(name = 'Juan', number=593990427750)





