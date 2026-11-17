from inventory import Inventario
from exceptions import ErrorInventario

def main():
    inventario=Inventario()
    codigo=input("Codigo del producto: ")
    try:
        cantidad=int(input("Cantidad a retirar: "))
        inventario.retirar(codigo, cantidad)
    except ValueError:
        print("La cantidad debe ser un numero entero.")
    except ErrorInventario as error:
        print(f"No se pudo realizar la operacion: {error}")
    else:
        print(
            "Retiro realizado. Stock restante:",
            inventario.productos[codigo].stock
        )

if __name__=="__main__":
    main()