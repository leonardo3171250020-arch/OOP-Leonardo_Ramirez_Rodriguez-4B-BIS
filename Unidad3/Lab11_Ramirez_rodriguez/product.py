from exceptions import CantidadInvalida, StockInsuficiente

class Producto:
    def __init__(self, codigo, stock):
        self.codigo=codigo
        self.stock=stock

    def retirar(self, cantidad):
        if cantidad>0:
            print("")
        else:
            #If the quantity is invalid (lesser than or equal to 0) this exception will happen
            raise CantidadInvalida()
        if cantidad<=self.stock:
            self.stock-=cantidad 
        else:
            #If the stock is greater than the product's stock available this exception will happen
            raise StockInsuficiente()

class TV(Producto):
    pass

class Laptop(Producto):
    pass

class Telefono(Producto):
    pass    
