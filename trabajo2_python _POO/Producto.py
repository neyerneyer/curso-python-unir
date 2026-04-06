class Producto:
    """Representa un producto con nombre, precio y cantidad."""

    def __init__(self, nombre:str, precio:float, cantidad:int) -> None:
        """
            Inicializa un objeto Producto con nombre, precio y cantidad.
            Args:
                nombre (str): Nombre del producto. No puede estar vacío.
                precio (float): Precio del producto. Debe ser mayor o igual a 0.
                cantidad (int): Cantidad disponible. Debe ser mayor o igual a 0.

            Raises:
                TypeError: Si los tipos de datos no son correctos.
                ValueError: Si el nombre está vacío, el precio es negativo o la cantidad es negativa.
        """
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser una cadena de texto.")

        if not isinstance(precio, (int, float)):
            raise TypeError("El precio debe ser un número.")

        if not isinstance(cantidad, int):
            raise TypeError("La cantidad debe ser un número entero.")

        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError('El nombre no puedo ser vacio.')
        if nombre.strip().isdigit():
            raise ValueError("El nombre no puede ser solo números.")
        if precio < 0:
            raise ValueError('El precio no puede ser negativo.')
        if cantidad < 0:
            raise ValueError('La cantidad no puede ser menor que 0.')

        self.nombre = nombre.strip()
        self.precio = float(precio)
        self.cantidad = int(cantidad)

    def actualizar_precio(self, nuevo_precio: float) -> None:
        """
           Actualiza el precio del producto con validación.
           Args:
               nuevo_precio (float): Nuevo precio del producto. Debe ser mayor o igual a 0.
           Raises:
               ValueError: Si el nuevo precio es negativo.
           """
        if nuevo_precio < 0:
            raise ValueError('El precio no puede ser negativo.')
        self.precio = nuevo_precio

    def actualizar_cantidad(self, nueva_cantidad: int) -> None:
        """
           Actualiza la cantidad disponible del producto.
           Args:
               nueva_cantidad (int): Nueva cantidad del producto. Debe ser mayor o igual a 0.
           Raises:
               ValueError: Si la nueva cantidad es negativa.
           """
        if nueva_cantidad < 0:
            raise ValueError('El cantidad no puede ser negativo.')
        self.cantidad = nueva_cantidad

    def calcular_valor_total(self) -> float:
        """
           Calcula el valor total del producto.
           Returns:
               float: Valor total calculado como precio × cantidad.
        """
        return self.precio * self.cantidad

    def __str__(self) -> str:
        """
            Devuelve una representación legible del producto.
            Returns:
                str: Cadena formateada con nombre, precio, cantidad y valor total.
        """
        return f"Producto: {self.nombre} | Precio: ${self.precio:.2f} | Cantidad: {self.cantidad} | Valor: {self.calcular_valor_total():.2f}"