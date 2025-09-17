# ------------- HERENCIA Y POLIMORFISMO ------------------

# ---- PILARES DE LA PROGRAMACION ORIENTADA A OBJETOS --------
# - Abstraccion
# - Encapsulamiento
# - Polimorfismo

# Herencia 
# Tenemos objetos que heredan propiedades de una super clase o de una clase padre

class Vehicle:
    def __init__(self, brand, model, price):
        # ENCAPSILACION:
        # Variables de instancias que contienen los datos primados del objeto
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True

    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f"El vehiculo {self.brand}. Ha sido vendido")
        else:
            print(f"El vehiculo {self.brand}. No esta disponible")
    
    # ABSTRACCION > A las variables privadas podemos acceder solo por metodos
    def check_available(self):
        return self.is_available
    
    def get_price(self):
        return self.price
    
    # Metodos que deben personalizarse en la clase hija
    def start_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado por la subclase")
    
    def stop_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado por la subclase")

# HERENCIA
# Creacion de la clase que hereda de una super clase
class Car(Vehicle):
    # POLIMORFISMO > CADA HIJO PUEDE SER DE FORMA DIFERENTE CON UN COMPORTAMIENTO DIFERENTE
    # Esta clase tiene los mismos metodos y atributos que la clase padre Vehicle
    # Pero deben personalizarse los metodos:
    def start_engine(self):
        if not self.is_available:
            return f"El motor del coche {self.brand} esta en marcha"
        else:
            return f"El coche {self.brand} no esta disponible"
        
    def stop_engine(self):
        if self.is_available:
            return f"El motor del coche {self.brand} se ha detenido"
        
        else:
            return f"El coche {self.brand} no esta disponible"

# Creacion de otra clase hija
class Bike(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f"La bicicleta {self.brand} esta en marcha"
        else:
            return f"La bicicleta {self.brand} no esta disponible"
        
    def stop_engine(self):
        if self.is_available:
            return f"La bicicleta {self.brand} se ha detenido"
        
        else:
            return f"La bicicleta {self.brand} no esta disponible"
        
# Creacion de otra clase hija 
class Truck(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f"El motor del camion {self.brand} esta en marcha"
        else:
            return f"El motor del camion  {self.brand} no esta disponible"
        
    def stop_engine(self):
        if self.is_available:
            return f"El motor del camion {self.brand} se ha detenido"
        
        else:
            return f"El motor del camion {self.brand} no esta disponible"
        
# Creamos la clase comprador
class Customer:
    def __init__(self, name):
        self.name = name
        self.purchased_vehicles = []

    # Creamos un metodo para que  el cliente compre el vehiculo
    # Indicamos de que clase es uno de los parametros 
    def buy_vehicle(self, vehicle: Vehicle):
        if vehicle.check_available(): #usamos un metodo de la clase Vehicle
            vehicle.sell()
            self.purchased_vehicles.append(vehicle)
        else:
            print(f"Lo siento, {vehicle.brand} no esta disponible")
    
    # Metodo para que un cliente consulte informacion sobre un vehiculo
    def inquire_vehicle(self, vehicle: Vehicle):
        if vehicle.check_available():
            availability = "Disponible"
        else:
            availability = "No disponible"
        
        print(f"El {vehicle.brand} esta {availability} y cuesta {vehicle.price}")
    

# Creamos la clase de la consesionaria
class Dealership:
    def __init__(self):
        self.inventory = []
        self.customers = []

    def add_vehicles(self, vehicle: Vehicle):
        self.inventory.append(vehicle)
        print(f"El {vehicle.brand} ha sido agregado al inventario")

    def regiter_customer(self, customer: Customer):
        self.customers.append(customer)
        print(f"El cliente {customer.name} ha sido agregado")

    def show_available_vehicle(self):
        print("Vehiculos disponibles en la tienda")
        for vehicle in self.inventory:
            if vehicle.check_available():
                print(f"- {vehicle.brand} por {vehicle.get_price()}")


# ------ POLIMORFISMO ---------
# Creamos instancias
car1 = Car("Toyota", "Cororla", 20000)
bike1 = Bike("Yamaha", "MT-07", 7000)
truck1 = Truck("Volvo", "FH16", 80000)

customer1 = Customer("Carlos")

dealership = Dealership()
dealership.add_vehicles(car1)
dealership.add_vehicles(bike1)
dealership.add_vehicles(truck1)

# Mostrar vehiculos disponibles
dealership.show_available_vehicle()

# Cliente consultar un vehiculo
customer1.inquire_vehicle(car1)

# Cliente comprar un vehiculo
customer1.buy_vehicle(car1)

# Mostrar vehiculos disponibles
dealership.show_available_vehicle()

