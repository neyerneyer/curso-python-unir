# -------------------------------------------------------
# Menú Principal
# -------------------------------------------------------
from Inventario import Inventario
from Producto import Producto


def menu_principal(inventario: Inventario):
    """
    Gestiona el menú interactivo del sistema de inventario.

    Permite al usuario:
        1. Agregar productos
        2. Buscar productos
        3. Listar productos
        4. Calcular valor total
        5. Salir del programa

    Args:
        inventario (Inventario): Instancia del inventario a manipular.
    """
    while True:
        print("\n=========== SISTEMA DE INVENTARIO ===========")
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Listar productos")
        print("4. Calcular valor total del inventario")
        print("5. Salir")
        print("==============================================")

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                agregar_producto_desde_menu(inventario)

            elif opcion == "2":
                nombre = input("Ingrese el nombre del producto a buscar: ")
                producto = inventario.buscar_producto(nombre)

                if producto:
                    print("\nProducto encontrado:")
                    print(producto)
                else:
                    print("\nProducto no encontrado.")

            elif opcion == "3":
                inventario.listar_productos()

            elif opcion == "4":
                valor = inventario.calcular_valor_inventario()
                print(f"\nValor total del inventario: ${valor:.2f}")

            elif opcion == "5":
                print("\n¡Gracias por usar el sistema de inventario!")
                break

            else:
                print("Opción inválida, intenta nuevamente.")

        except ValueError as e:
            print(f"\n Error: {str(e)}")

        except Exception as e:
            print(f"\n Error inesperado: {str(e)}")

# -------------------------------------------------------
# Función de apoyo para crear productos desde el menú
# -------------------------------------------------------

def agregar_producto_desde_menu(inventario: Inventario):
    """
    Solicita al usuario los datos necesarios para crear un producto y lo agrega al inventario.

    Maneja excepciones por entradas inválidas (precio, cantidad o nombre incorrectos).

    Args:
        inventario (Inventario): Inventario donde se agregará el nuevo producto.
    """
    print("\n--- AGREGAR NUEVO PRODUCTO ---")
    try:
        nombre = input("Nombre del producto: ").strip()
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))

        producto = Producto(nombre, precio, cantidad)
        inventario.agregar_producto(producto)

        print("\n✅ Producto agregado correctamente.")

    except ValueError as e:
        print(f"❌ Error al agregar producto: {e}")

# -------------------------------------------------------
# Ejecución del Programa
# -------------------------------------------------------

if __name__ == "__main__":
    inv = Inventario()
    menu_principal(inv)