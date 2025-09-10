# ************** PROGRAMACION ORIENTADA A OBJETOS CON PYTHON ******************
# POO es un paradigma de la programacion que dice que el software debe organizar en objetos que son instancias de clases
# Las clases son una plantilla genericas y los objetos son muestras particulares de las clases

# Creacion de una clase (inicia con mayuscula el nombre de las clases)
class Person:
    # Dentro de la clase se crea la funcion constructor que es una funcion propia y especial de las clases en la que se definen los atributos principales.
    # El constructor en su estructura debe recibir como parametro a si mismo
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Creamos los metodos que son funciones propias de la clase
    def greet(self):
        print(f"Hola, mi nombre es {self.name} y tengo {self.age}")


# Para usar la clase debemos crear un objeto y almacenarlo en una variable
person1 = Person("Ana",30)
person2 = Person("Luis", 25)
person1.greet()
person2.greet()