class Persona:

    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido

class Cliente(Persona):

    def __init__(self, nombre, apellido,numero_cuenta,balance=0):
        super().__init__(nombre,apellido)
        self.numero_cuenta=numero_cuenta
        self.balance=balance

    

    def __str__(self):
        return f"Nombre: {self.nombre} {self.apellido} Numero de cuenta: {self.numero_cuenta} Balance: {self.balance}"

    def deposito(self,cantidad_deposito):
        self.balance+=cantidad_deposito
        print("Deposito aceptado")

    def retirar(self,cantidad_retiro):
        if self.balance>=cantidad_retiro:
            self.balance-=cantidad_retiro
            print("Retiro exitoso")
        else:
            print("Fondos insuficientes")
    
def crear_cliente():
    nombre_cliente=input("Ingrese su nombre: ")
    apellido_cliente=input("Ingrese su apellido: ")
    numero_cuenta=input("Ingrese numero de cuenta: ")
    cliente=Cliente(nombre_cliente,apellido_cliente,numero_cuenta)
    return cliente

