# ---------------------------------------------
# Desarrollo de una calculadora de promedios escolares en Python
# utilizando variables, operadores, estructuras de control y funciones básicas.
# ---------------------------------------------


def main():
    print("---------------------------------------------")
    print("CALCULADORA DE PROMEDIOS ESCOLARES CON PYTHON")
    print("---------------------------------------------")

    materias, calificaciones = ingresar_calificaciones()

    if len(materias) == 0:
        print("\n No se ingresaron materias. Programa finalizado.")
        return

    promedio = calcular_promedio(calificaciones)
    aprobadas, reprobadas = determinar_notas(calificaciones)
    idx_max, idx_min = encontrar_nota_max_y_min(calificaciones)

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


def ingresar_calificaciones():
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
        continuar = input("¿Desea ingresar otra materia? (s/n): ").lower()
        if continuar != "s":
            break

    return materias, calificaciones


def calcular_promedio(calificaciones):
    if len(calificaciones) == 0:
        return 0
    return sum(calificaciones) / len(calificaciones)


def determinar_notas(calificaciones, umbral=5.0):
    aprobadas = []
    reprobadas = []

    for valor in range(len(calificaciones)):
        nota = calificaciones[valor]

        if nota >= umbral:
            aprobadas.append(valor)
        else:
            reprobadas.append(valor)

    return aprobadas, reprobadas


def encontrar_nota_max_y_min(calificaciones):
    if len(calificaciones) == 0:
        return None, None

    indice_max = calificaciones.index(max(calificaciones))
    indice_min = calificaciones.index(min(calificaciones))

    return indice_max, indice_min


if __name__ == "__main__":
    main()
