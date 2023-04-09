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
        return f"\nCliente: {self.nombre} {self.apellido}\nNumero de cuenta: {self.numero_cuenta}\nBalance: {self.balance}"

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

def inicio():
    mi_cliente=crear_cliente()
    print(mi_cliente)

    opcion=0

    while opcion != 3:
        
        print("\n(1)= Depositar")
        print("(2)= Retirar")
        print("(3)=Salir")
        print()
        opcion=int(input("Elija una opcion: "))

        if opcion==1:
            monto=int(input("Monto a depositar: "))
            mi_cliente.deposito(monto)

        elif opcion==2:
            monto_r=int(input("Monto a retirar: "))
            mi_cliente.retirar(monto_r)
        print(mi_cliente)

    print("Gracias por contar con nuestros servicios")

inicio()