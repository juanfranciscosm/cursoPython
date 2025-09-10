# ---------- EJEMPLO MANEJO DE CUENTA BANCARIA CON POO -------------

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True #Esta variable no necesita recibirse commo variable en el constructor
    
    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print(f"Se ha depositado {amount}. Saldo actual {self.balance}")
        else:
            print("No se puede depositar. La cuenta esta incactiva")
    
    def withdraw(self, amount):
        if self.active:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Se ha retirado {amount}. Saldo actual {self.balance}")
            else:
                print(f"No hay fondos suficientes. Tu saldo actual es {self.balance}")
        else:
            print("No se puede retirar. La cuenta esta incactiva")
    
    def desactivate_account(self):
        self.is_active = False
        print(f"La cuenta ha sido desactivada")
    
    def activate_account(self):
        self.is_active = True
        print(f"La cuenta ha sido activada")


# Creamos los objetos de esta clase y llamamos a los metodos

account1 = BankAccount("Ana", 500)
account2 = BankAccount("Luis", 1000)

# Llamada a los metodos
account1.deposit(200)
account2.deposit(100)

# Si se desactiva la cuenta, no deberia permitir depositar dinero
account1.desactivate_account()
account1.deposit(500)

# Luego de activarla deberia depositarse
account1.activate_account()
account1.deposit(50)