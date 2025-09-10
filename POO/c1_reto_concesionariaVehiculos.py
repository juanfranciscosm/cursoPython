# ------------------ RETO CONCESIONARIA DE VEHICULOS ----------------------
'''
Desarrolla una concesionaria de vehículos en la cual se puedan gestionar las compras y ventas de vehículos. 
Un usuario podrá ver los vehículos disponibles, su precio y realizar la compra de uno. 
Aplica los conceptos de programación orientada a objetos vistos en este ejercicio.
'''

class Cars:
    def __init__(self, model, chasis_id, pvp=0, buy_price=0):
        self.model = model
        self.chasis_id = chasis_id
        self.pvp = pvp
        self.buy_price = buy_price
        self.is_available = True

    def sale(self, amount):
        if self.is_available and amount == self.pvp:
            self.is_available = False
            print(f"Se vendio el vehiculo {self.model} con chasis numero {self.chasis_id} a {self.pvp}.")
        elif amount != self.pvp:
            print(f"No se puede vender. Monto ofertado es inferiro al precio de venta")
        else:
            print(f"No se puede vender. Vehiculo no disponible")

    def buy(self, amount):
        self.buy_price = amount
        self.pvp = self.buy_price + (self.buy_price*0.4)
        self.is_available = True
        print(f"Se compro el vehiculo {self.model} con chasis numero {self.chasis_id} por {self.buy_price}")

class Customer:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.cars_buyed = []
        self.cars_saled = []

    def buy_car(self, car, amount):
        if car.is_available:
            car.sale(amount)
            print(f"El usuario {self.name} ha comprado el vehiculo {car.model} por {car.pvp}")
        else:
            print(f"El vehiculo no esta disponible")
    
    def sale_car(self, car, amount):
        car.buy(amount)
        print(f"El vehiculo {self.model} ha sido vendido a la concesionaria por {car.buy_price}")
        

