class ErrorInventario(Exception):
    pass

#Happens if the code introduced does not correspond with a product
class ProductoNoEncontrado(ErrorInventario):
    def __init__(self, mensaje="Producto no encontrado"):
        super().__init__(mensaje)

#Happens if the user introduces a quantity lesser than or equal to 0
class CantidadInvalida(ErrorInventario):
    def __init__(self, mensaje="Cantidad invalida"):
        super().__init__(mensaje)

#Happens if the user introduces a quantity greater than the stock available
class StockInsuficiente(ErrorInventario):
    def __init__(self, mensaje="Stock insuficiente"):
        super().__init__(mensaje)