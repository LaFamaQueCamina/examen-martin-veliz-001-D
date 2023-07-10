import os
import time

concierto = [[j + i*10 for j in range(1, 11)] for i in range(10)]

entradas_vendidas = {}
ganancias_totales = 0

precios = {
    "TarifaPlatinum": {
        "precio": 120000,
        "rango": range(1, 21)
    },
    "TarifaGold": {
        "precio": 80000,
        "rango": range(21, 51)
    },
    "TarifaSilver": {
        "precio": 50000,
        "rango": range(51, 101)
    }
}

def mostrar_estado_concierto():
    for fila in concierto:
        for lugar in fila:
            if lugar in entradas_vendidas:
                print("X", end=" ")
            else:
                print(lugar, end=" ")
        print()

def mostrar_menu_precios():
    os.system("cls")  
    print("----- Menú de Precios -----")
    for precio, info in precios.items():
        print(f"{precio}: ${info['precio']}")
        print("Ubicaciones Disponibles:", end=" ")
        entradas_disponibles = []
        for entradas in info["rango"]:
            if entradas not in entradas_vendidas:
                entradas_disponibles.append(str(entradas))
        print(", ".join(entradas_disponibles))
        print()

def comprar_entrada():
    global ganancias_totales

    mostrar_menu_precios()
    entradas = int(input("Ingrese el número de ubicación que desea comprar: "))

    run = input("Ingrese el RUN del pasajero (sin guiones ni puntos): ")
    if run in entradas_vendidas.values() and sum(1 for v in entradas_vendidas.values() if v == run) >= 3:
        print("Este RUN ya ha alcanzado el límite de compra (3 entradas).")
        time.sleep(2)
        return

    if entradas in entradas_vendidas:
        print("La ubicación no está disponible.")
    else:
        tarifa = None
        for precio, info in precios.items():
            if entradas in info["rango"]:
                tarifa = info["precio"]
                break
        if tarifa is None:
            print("Ubicación no se encuentra disponible.")
            return

        entradas_vendidas[entradas] = run
        ganancias_totales += tarifa
        print("Ubicación comprada correctamente.")
        time.sleep(2)


def mostrar_lugares_disponibles():
    os.system("cls")  
    print("Ubicaciones disponibles:")
    mostrar_estado_concierto()
    time.sleep(2)  

def mostrar_listado_personas():
    os.system("cls") 
    print("Listado de personas que asistiran al concierto:")
    for lugar, run in sorted(entradas_vendidas.items()):
        run_con_separaciones = f"{run[:2]}.{run[2:5]}.{run[5:8]}-{run[8:]}"
        print(f"RUN: {run_con_separaciones} - Ubicacion: {lugar}")
    time.sleep(2) 

def mostrar_ganancias_totales():
    os.system("cls")
    print("Ganancias totales por tipo de entrada:")
    for tipo, info in precios.items():
        cantidad_vendida = sum(1 for v in entradas_vendidas.values() if v in info["rango"])
        total = cantidad_vendida * info["precio"]
        print(f"{tipo}: Cantidad vendida: {cantidad_vendida}, Total: ${total}")

    print("------")
    total_general = sum(1 for _ in entradas_vendidas)
    total_precios = sum(precio["precio"] for precio in precios.values() for _ in entradas_vendidas if _ in precio["rango"])
    print(f"Total general: Cantidad vendida: {total_general}, Total: ${total_precios}")
    time.sleep(2)

def main():
    while True:
        os.system("cls")  
        print("***Bienvenidos al concierto de Michael Jam***")
        print("")
        print("----- MENÚ -----")
        print("Eliga una opción:")
        print("1. Comprar Entradas")
        print("2. Mostrar Ubicaciones Disponibles ")
        print("3. Ver Listado De Asistentes")
        print("4. Mostrar Ganancias Totales")
        print("5. Salir")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            comprar_entrada()
        elif opcion == 2:
            mostrar_lugares_disponibles()
        elif opcion == 3:
            mostrar_listado_personas()
        elif opcion == 4:
            mostrar_ganancias_totales()
        elif opcion == 5:
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
        time.sleep(2)  

main()
