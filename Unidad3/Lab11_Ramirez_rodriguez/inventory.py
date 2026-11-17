from product import TV, Laptop, Telefono
from exceptions import ProductoNoEncontrado

class Inventario:
    def __init__(self):
        self.productos = {
            "P01": TV("P01",5),
            "P02": Laptop("P02",10),
            "P03": Telefono("P03",15)
        }

    def retirar(self, codigo, cantidad):
        if codigo in self.productos:
            self.productos[codigo].retirar(cantidad)
        else:
            #If code is invalid this exception will activate
            raise ProductoNoEncontrado()