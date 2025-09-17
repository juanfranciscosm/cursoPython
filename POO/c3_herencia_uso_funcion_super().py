# ----------- HERENCIA Y USO DE FUNCION SUPER() ------------

# FUNCION Super()
# Es una herramienta para acceder y llamar a metodos de la super clase (la clase padre), pero desde la sub-clase (clase hija)
# Facilita la extension de funcionalidades y acceso a metodos y atributos de la super clase sin tener que nombrarlas explicitamente

# RECORDAR
# - Metodos son acciones o cosas que sabe hacer la clase
# - Atributos son caracteristicas que tiene la clase
# - Constructor es la funcion en la que indicamos la informacio con la que queremos iniciar (atributos)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print('Hello! I am a person')

# Estudiante hereda de la clase persona
class Student(Person):
    # Si usamos un constructor, se deben pedir los mismos atributos del padre y podemos agregar otros atributos que solo tendra la clase hija
    def __init__(self, name, age, student_id):
        # con super() podemos llamar al constructor de la clase padre
        # Al contructor de la clase padre le pandamos los parametros que solo se toman en cuenta en la clase super (padre)
        super().__init__(name, age)
        self.student_id = student_id # Este es un atributo que solo pertence a los estudiantes y no a todas las personas

    # Modificamos el comportamiento del estudiante al saludar
    def greet(self):
        super().greet()
        print(f"Hello, my student ID is {self.student_id}")


# Creamos a la estudiante 
student = Student("Ana", 20, "S123")
# Hacemos que la estudiante salude
student.greet()
