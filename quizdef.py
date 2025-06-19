turistas = {"001": ["John Doe", "Estados Unidos", "12-01-2024"],
"002": ["Emily Smith", "Estados Unidos", "23-03-2024"],
"012": ["Julian Martinez", "Argentina", "19-09-2023"],
"014": ["Agustin Morales", "Argentina", "28-03-2024"],
"005": ["Carlos Garcia", "Mexico", "10-05-2024"],
"006": ["Maria Lopez", "Mexico", "08-12-2023"],
"007": ["Joao Silva", "Brasil", "20-06-2024"],
"003": ["Michael Brown", "Estados Unidos", "05-07-2023"],
"004": ["Jessica Davis", "Estados Unidos", "15-11-2024"],
"008": ["Ana Santos", "Brasil", "03-10-2023"],
"010": ["Martin Fernandez", "Argentina", "13-02-2023"],
"011": ["Sofia Gomez", "Argentina", "07-04-2024"],
}

def menuPrincipal():
    while True:
        print("*** MENU PRINCIPAL ***")
        print("1.- Turistas por pais.")
        print("2.- Turistas por mes.")
        print("3.- Eliminar turista.")
        print("4.- Salir")

        try:
            opc = int(input("Ingrese la opcion: "))
            if opc < 1 or opc > 4:
                print("Opcion invalida.")
                continue
        except:
            print("Opcion incorrecta. Las opciones son del 1 al 4.")
        if opc == 1:
            pais = input("Ingrese el pais: ")
            turistas_por_pais(pais)
        elif opc == 2:
            while True:
                try:
                    mes = int(input("Ingrese el mes: "))
                    if mes < 1 or mes > 12:
                        print(f"Recuerda que los meses son 1-12")
                    else:
                        break
                except:
                    print("Recuerda que solo puedes ingresar valores numericos en esta opcion.")
            turistas_por_mes(mes)
        elif opc == 3:
            eliminar_turista()
        else:
            print("Programa terminado...")
            break

def turistas_por_pais(pais):
    for n, l in turistas.items():
        if pais not in l[1]:
            print("Pais no existe")
            return
        if l[1] == pais:
            print(l[0])

def turistas_por_mes(mes):
    cantidad_mes = 0
    total_turistas = len(turistas)

    for datos in turistas.values():
        fecha = datos[2]

        mes_turistas = int(fecha.split("-")[1])

        if mes == mes_turistas:
            cantidad_mes += 1
    if total_turistas == 0:
        return 0.0
    elif cantidad_mes == 0:
        print("Este mes no hubieron turistas")
        return
    
    porcentaje = (cantidad_mes / total_turistas) * 100
    resultado = round(porcentaje, 1)  
    print(f"Porcentaje de turistas que vinieron ese mes: {resultado}%")

def eliminar_turista():
    usuario_eliminado = None
    eliminado = input("Ingrese el nombre del turista que desea eliminar: ")
    for c, d in turistas.items():
        if d[0].lower() == eliminado.lower():
            usuario_eliminado = c
            break
    if usuario_eliminado == None:
        print("Usuario no encontrado.")
        return
    elif usuario_eliminado:
        print("Usuario eliminado con exito.")
        del turistas[usuario_eliminado]
