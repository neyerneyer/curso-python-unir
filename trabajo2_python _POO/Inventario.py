from Producto import Producto
class Inventario:
    """Gestiona una colección de productos."""

    def __init__(self):
        """
        Inicializa un inventario vacío para almacenar productos.
        """
        self.productos = []

    def agregar_producto(self, producto: Producto):
        """
            Agrega un producto al inventario.
            Args:
                producto (Producto): Objeto Producto a agregar.
            Raises:
                TypeError: si 'producto' no es instancia de Producto.
        """
        if not isinstance(producto, Producto):
            raise TypeError("Solo se pueden agregar objetos de tipo Producto.")
        self.productos.append(producto)

    def buscar_producto(self, nombre: str):
        """
            Busca un producto por su nombre (insensible a mayúsculas/minúsculas).
            Args:
                nombre (str): Nombre del producto a buscar.
            Returns:
            Producto | None: El producto encontrado o None si no existe.
        """
        nombre = nombre.strip().lower()
        for producto in self.productos:
            if producto.nombre.lower() == nombre:
                return producto
        return None

    def calcular_valor_inventario(self) -> float:
        """
            Calcula el valor total del inventario sumando el valor de todos los productos.
            Returns:
                float: Valor total del inventario.
        """
        return sum(p.calcular_valor_total() for p in self.productos)

    def listar_productos(self):
        """
            Muestra en consola todos los productos del inventario.
            Si el inventario está vacío, informa al usuario.
        """
        if not self.productos:
            print("\nNo hay productos en el inventario.")
            return []
        resultado = []
        print("\n------ LISTA DE PRODUCTOS ------")
        for prod in self.productos:
            texto = str(prod)
            print(texto)
            resultado.append(texto)
        return resultado