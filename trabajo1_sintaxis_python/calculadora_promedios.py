# ---------------------------------------------
# Desarrollo de una calculadora de promedios escolares en Python
# utilizando variables, operadores, estructuras de control y funciones básicas.
# ---------------------------------------------


def main():
    """
    Función principal del programa.

    Controla el flujo general: solicita datos al usuario, calcula el promedio,
    determina materias aprobadas/reprobadas, encuentra las notas extremas y
    muestra un resumen completo por consola.
    """
    print("---------------------------------------------")
    print("CALCULADORA DE PROMEDIOS ESCOLARES CON PYTHON")
    print("---------------------------------------------")

    materias, calificaciones = ingresar_calificaciones()

    if len(materias) == 0:
        print("\n No se ingresaron materias. Programa finalizado.")
        return

    promedio = calcular_promedio(calificaciones)

    if promedio is None:
        print("\nNo fue posible calcular el promedio (no hay datos).")
        return

    aprobadas, reprobadas = determinar_estado(calificaciones)
    idx_max, idx_min = encontrar_extremos(calificaciones)

    print("\n=========== RESUMEN DE NOTAS ===========\n")

    print("Materias ingresadas:")
    for item in range(len(materias)):
        print(f"  - {materias[item]}: {calificaciones[item]}")

    print(f"\nPromedio general: {promedio:.2f}")

    print("\nMaterias aprobadas:")
    if aprobadas:
        for i in aprobadas:
            print(f" {materias[i]} ({calificaciones[i]})")
    else:
        print("  Ninguna")

    print("\nMaterias reprobadas:")
    if reprobadas:
        for i in reprobadas:
            print(f" {materias[i]} ({calificaciones[i]})")
    else:
        print("  Ninguna")

    print("\nMejor calificación:")
    print(f" {materias[idx_max]} ({calificaciones[idx_max]})")

    print("\nCalificación más baja:")
    print(f" {materias[idx_min]} ({calificaciones[idx_min]})")

    print("\n¡Gracias por usar la calculadora!")


def ingresar_calificaciones():
    """
    Solicita al usuario ingresar materias y sus calificaciones.

    Retorna:
        tuple: (materias, calificaciones)
            - materias (list[str]): nombres de las materias ingresadas
            - calificaciones (list[float]): notas respectivas (0 a 10)
    """
    materias = []
    calificaciones = []

    print("\n=== INGRESO DE MATERIAS Y CALIFICACIONES ===")

    while True:
        nombre = input("Ingrese el nombre de la materia: ").strip()

        # Validación del nombre
        if nombre == "":
            print("El nombre no puede estar vacío.")
            continue

        # Validar calificación
        while True:
            try:
                nota = float(input(f"Ingrese la calificación para {nombre} (0 - 10): "))
                if 0 <= nota <= 10:
                    break
                else:
                    print("La calificación debe estar entre 0 y 10.")
            except ValueError:
                print("Debe ingresar un número válido.")

        materias.append(nombre)
        calificaciones.append(nota)

        # Preguntar para continuar
        while True:
            continuar = input("¿Desea ingresar otra materia? (s/n): ").lower()
            if continuar in ("s","n"):
                break
            print("Respuesta incorrecta. Por favor ingrese 's' or 'n'.\n")
        if continuar == "n":
            break

    return materias, calificaciones


def calcular_promedio(calificaciones):
    """
    Calcula el promedio aritmético de una lista de calificaciones.

    Parámetros:
        calificaciones (list[float]): lista de notas.

    Retorna:
        float: promedio calculado. Si la lista está vacía, retorna 0.
    """
    if len(calificaciones) == 0:
        return 0
    return sum(calificaciones) / len(calificaciones)


def determinar_estado(calificaciones, umbral=5.0):
    """
    Determina qué materias están aprobadas y cuáles reprobadas según un umbral.

    Parámetros:
        calificaciones (list[float]): lista de notas.
        umbral (float): nota mínima para aprobar (por defecto 5.0).

    Retorna:
        tuple: (aprobadas, reprobadas)
            - aprobadas (list[int]): índices de notas >= umbral
            - reprobadas (list[int]): índices de notas < umbral
    """
    aprobadas = []
    reprobadas = []

    for valor, nota in enumerate(calificaciones):
        if nota >= umbral:
            aprobadas.append(valor)
        else:
            reprobadas.append(valor)

    return aprobadas, reprobadas


def encontrar_extremos(calificaciones):
    """
    Encuentra los índices de la calificación más alta y más baja.

    Parámetros:
        calificaiones (list[float]): lista de notas.

    Retorna:
        tuple: (indice_max, indice_min)
            - indice_max (int): índice de la nota mayor
            - indice_min (int): índice de la nota menor

        Si la lista está vacía, retorna (None, None).
    """
    if len(calificaciones) == 0:
        return None, None

    indice_max = calificaciones.index(max(calificaciones))
    indice_min = calificaciones.index(min(calificaciones))

    return indice_max, indice_min


if __name__ == "__main__":
    main()
