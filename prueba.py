import datetime
import locale


locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")




def calcular_estacion(mes):
    if mes in (1, 2, 12):
        return "Invierno"
    elif mes in (3, 4, 5):
        return "Primavera"
    elif mes in (6, 7, 8):
        return "Verano"
    elif mes in (9, 10, 11):
        return "Otoño"
    else:
        return "Mes inválido"




def calcular_fecha(mes, dia):
    try:
        fecha = datetime.date(2000, mes, dia)
        fecha_str = fecha.strftime("%d de %B")
        return fecha_str.capitalize()
    except ValueError:
        return "Fecha inválida"



mes = int(input("Ingresa el número de mes (1-12): "))
dia = int(input("Ingresa el número de día (1-31): "))


estacion = calcular_estacion(mes)
fecha = calcular_fecha(mes, dia)


if estacion == "Mes inválido":
    print("El número de mes ingresado no es válido.")
else:
    print(
        f"La fecha es el {fecha} y corresponde a la estación del {estacion}.")
