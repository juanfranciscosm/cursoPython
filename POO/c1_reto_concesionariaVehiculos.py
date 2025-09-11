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
        if car.is_available and amount >= car.pvp:
            car.sale(amount)
            self.cars_buyed.append(car)
            print(f"El usuario {self.name} ha comprado el vehiculo {car.model} por {car.pvp}")
        elif car.is_available and amount < car.pvp:
            print("El vehiculo no esta disponible por USD $", amount)
        else: 
            print("El vehiculo no esta disponible")
    
    def sale_car(self, car, amount):
        car.buy(amount)
        self.cars_saled.append(car)
        print(f"El vehiculo {self.model} ha sido vendido a la concesionaria por {car.buy_price}")
        
class Concesionaria:
    def __init__(self):
        self.cars = []
        self.customers = []
    
    def add_car(self, car):
        self.cars.append(car)
        print(f"El vehiculo {car.model} con chasis {car.chasis_id} ha sido añadido al catalogo")

    def register_customer(self, customer):
        self.customers.append(customer)
        print(f"El cliente {customer.name} ha sido registrado")

    def show_available_cars(self):
        print("Vehiculos disponibles para la venta")
        for car in self.cars:
            if car.is_available:
                print(f"{car.model} a USD ${car.pvp}")


# ------------------ DEMO DE USO ------------------

# 1) Crear la concesionaria
dealer = Concesionaria()

# 2) Ingresar vehículos al inventario (la concesionaria "compra" y define PVP=buy*1.4)
v1 = Cars("Toyota Corolla 2022", "CH-1001")
v1.buy(12000)   # PVP = 16800
dealer.add_car(v1)

v2 = Cars("Hyundai Tucson 2021", "CH-1002")
v2.buy(18000)   # PVP = 25200
dealer.add_car(v2)

v3 = Cars("Chevrolet Onix 2023", "CH-1003")
v3.buy(10000)   # PVP = 14000
dealer.add_car(v3)

# Mostrar inventario disponible
print("\n--- Inventario inicial ---")
dealer.show_available_cars()

# 3) Registrar clientes
c1 = Customer("Juan Sánchez", "C001")
c2 = Customer("Ana Torres", "C002")
dealer.register_customer(c1)
dealer.register_customer(c2)

# 4) Venta exitosa: Juan compra el Corolla (pago EXACTO al PVP)

print("\n--- Venta exitosa: Juan compra el Corolla ---")
c1.buy_car(v1, 16800)  # 16800 exactos

# Reintento de vender el mismo auto: debe fallar por no disponible
print("\n--- Intento de vender vehículo ya vendido ---")
c2.buy_car(v1, 16800)

# 5) Intento de compra con monto inferior al PVP: debe fallar
print("\n--- Venta fallida: Ana intenta comprar la Tucson con monto inferior ---")
c2.buy_car(v2, 20000)  # PVP 25200

# 6) Venta exitosa: Ana compra el Onix (pago EXACTO al PVP)
print("\n--- Venta exitosa: Ana compra el Onix ---")
c2.buy_car(v3, 14000)  # 14000 exactos

# 7) Entra un usado al inventario
# (Usamos car.buy() para fijar buy_price y PVP, y lo añadimos al catálogo)
print("\n--- Retoma simulada: entra un Kia Rio usado ---")
usado = Cars("Kia Rio 2016", "CH-7777")
usado.buy(5000)  # PVP 7000
dealer.add_car(usado)

# 8) Venta del usado
print("\n--- Venta del usado: Juan compra el Kia Rio ---")
c1.buy_car(usado, 7000)  # pago exacto

# 9) Resumen final
print("\n--- Resumen de clientes ---")
for cliente in dealer.customers:
    print(f"Cliente: {cliente.name} ({cliente.id})")
    if cliente.cars_buyed:
        for car in cliente.cars_buyed:
            print(f"  * Compró: {car.model} ({car.chasis_id}) por ${car.pvp}")
    else:
        print("  * Sin compras registradas.")

print("\n--- Inventario disponible al final ---")
dealer.show_available_cars()