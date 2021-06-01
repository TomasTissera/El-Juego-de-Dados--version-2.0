
"""
    °a. Enunciado y consignas
    °Cantidad de jugadores: 2
    °Final del juego: Gana el jugador que alcance los x puntos o más,siendo x un valor que se ingresa por teclado (validar que x sea mayor a 10)
    -->Desarrollo del juego:
    cada jugador solo apuesta por par o impar.
    -echo-Si acierta gana el puntaje equivalente al dado de mayor valor,y adicionalmente este puntaje se duplica si todos los dados son de dicha paridad. Si pierde, resta el dado de menor valor (puede quedar con puntaje negativo). 
    
    -parcial de que!-Se debe mostrar por cada turno el valor de los dados y el puntaje parcial del jugador.

    -echo-Al terminar el turno de ambos jugadores, se verifica si alguno de ellos alcanzó el puntaje objetivo. Si no es así, vuelven a jugar ambos (cada uno debe completar su turno) hasta finalizar el juego.
    
    -echo-Al terminar el juego, se debe mostrar el nombre y puntaje total obtenido de cada jugador e informar el nombre del ganador.

    -echo-Si ambos jugadores llegaran a tener el mismo puntaje final, gana aquel jugador que tenga la mayor cantidad de jugadas ganadas. Si coinciden también en cantidad de jugadas, entonces es un empate.
    
    Por último, se pide elaborar y mostrar las siguientes estadísticas:
    -echo-->La cantidad de jugadas realizadas (recordando que una jugada consiste en los turnos de ambos jugadores).
    
    -echo-->Si hubo al menos una jugada con puntaje empatado entre ambos jugadores.        
    
    -!promedio a que?-->El puntaje promedio obtenido por jugada por cada jugador.
    
    -echo-->El porcentaje de aciertos para cada jugador (considerando acierto si la suma de los dados coincidió con la paridad apostada). 
    Indicar también si el ganador es el que tuvo mayor porcentaje de aciertos.
    
    -revisar->Si algún jugador ganó en al menos 3 turnos seguidos.
"""
import random
print("--------------------------------------")
print("|            Beinvenido              |")
print("--------------------------------------")

nombre1=str(input("Ingrese el nombre del 'Jugador N°1'\n->"))
nombre2=str(input("Ingrese el nombre del 'Jugador N°2'\n->"))

x = int(input("Ingrese el puntaje a lograr:\n->"))

nronda = 1

rondas_empatadas = 0

aciertos1 = 0
aciertos2 = 0

jugadas_ganadas1 = 0
jugadas_ganadas2 = 0

jugada_ganada_ronda_anterior = ""
contador_jugadas_ganadas_seguidas = 1
ganador_ronda = ""
while True:
    ganador = ""
    nombre_ganador= ""

    jugador1_n1 = random.randint(1, 6)
    jugador1_n2 = random.randint(1, 6)
    jugador1_n3 = random.randint(1, 6)

    jugador2_n1 = random.randint(1, 6)
    jugador2_n2 = random.randint(1, 6)
    jugador2_n3 = random.randint(1, 6)

    puntaje1 = 0
    puntaje2 = 0

    dados1 = [jugador1_n1,jugador1_n2,jugador1_n3]
    dados2 = [jugador2_n1,jugador2_n2,jugador2_n3]

    print("|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|")
    print("Ronda N°",nronda)
    print("|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|")

    print("**************************************")
    print("*****     Momento de Apostar     *****")
    print("**************************************")
    print("Jugador",nombre1,"haga su apuesta")
    apuesta1 = str(input("Ingrese su apuesta:\n°Ingrese 'par' si desea apostar al Par\n°Ingrese 'impar' si desea apostar a impar\n-->"))
    
    print("Jugador",nombre2,"haga su apuesta")
    apuesta2 = str(input("Ingrese su apuesta:\n°Ingrese 'par' si desea apostar al Par\n°Ingrese 'impar' si desea apostar a impar\n-->"))

    print("**************************************")
    print("***** Momento de tirar los dados *****")
    print("**************************************")
    print("--------------------------------------")
    print("->Turno del jugador",nombre1,"de tirar los dados")
    Enter = str(input("-->Presione enter para tirar el primer dado"))
    print("->Se ha tirado el primer dado!")
    Enter = str(input("-->Presione enter para tirar el segundo dado"))
    print("->Se ha tirado el segundo dado!")
    Enter = str(input("-->Presione enter para tirar el tercer dado"))
    print("->Se ha tirado el tercer dado!")
    print("!Los dados que le tocaron son:",dados1)
    print("--------------------------------------")
    print("->Turno del jugador",nombre2,"de tirar los dados")
    Enter = str(input("-->Presione enter para tirar el primer dado"))
    print("->Se ha tirado el primer dado!")
    Enter = str(input("-->Presione enter para tirar el segundo dado"))
    print("->Se ha tirado el segundo dado!")
    Enter = str(input("-->Presione enter para tirar el tercer dado"))
    print("->Se ha tirado el tercer dado!")
    print("Los dados que le tocaron son:",dados2)
    print("--------------------------------------")

    
    mayor1 = max(dados1)
    mayor2 = max(dados2)
    menor1 = min(dados1)
    menor2 = min(dados2)
    pares1 = 0

    for parimpar1 in dados1:
        if parimpar1 % 2 == 0:
            pares1  += 1

    if pares1 ==3 :
        dados1 = "pares"
    else:
        dados1 = "impares"

    for parimpar2 in dados2:
        if parimpar2 % 2 == 0:
            pares2 = 0
            pares2  += 1

    if pares1 == 3:
        dados2 = "pares"
    else:
        dados2 = "impares"

    suma1 = jugador1_n1 + jugador1_n2 + jugador1_n3
    suma2 = jugador2_n1 + jugador2_n2 + jugador2_n3

    if suma1 %2 == 0:
        #print inceserario
        print("La suma es par")
        p1_par_impar_resultado = "par"
        
    else:
        #print inceserario
        print("La suma es impar")
        p1_par_impar_resultado = "impar"

    if suma2 %2 == 0:
        #print inceserario
        print("La suma es par")
        p2_par_impar_resultado = "par"
    else:
        #print inceserario
        print("La suma es impar")
        p2_par_impar_resultado = "impar"

    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("Resultados de la puesta:")
    if apuesta1 == p1_par_impar_resultado:
        print("*El Jugador",nombre1,"acerto a su apuesta")
        aciertos1 +=1
        puntaje1 += mayor1
        if dados1 == apuesta1:
            print("Ademas todos sus dados tambien son",apuesta1,"asi que se duplica su puntaje")
            puntaje1 = puntaje1 * 2
    else:
        print("*El Jugador",nombre1,"no acerto a su apuesta")
        puntaje1 -= menor1

    if apuesta2 == p2_par_impar_resultado:
        print("*El Jugador",nombre2,"acerto a su apuesta")
        aciertos2 +=1
        puntaje2 += mayor2
        if dados2 == apuesta2:
            print("Ademas todos sus dados tambien son",apuesta2,"asi que se duplica su puntaje")
            puntaje2 = puntaje2 * 2
    else:
        print("*El Jugador",nombre2,"no acerto a su apuesta")
        puntaje2 -= menor2
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")



    if puntaje1 > puntaje2 and puntaje1!=puntaje2:
        jugadas_ganadas1 += 1
        ganador_ronda = nombre1
        jugada_ganada_ronda_anterior = nombre1
    elif puntaje2 > puntaje1 and puntaje2!=puntaje1:
        jugadas_ganadas2 += 1
        ganador_ronda = nombre2
        jugada_ganada_ronda_anterior = nombre1
        ganador_ronda = "empate"
        rondas_empatadas += 1

    if jugada_ganada_ronda_anterior == ganador and ganador != "empate":
        contador_jugadas_ganadas_seguidas += 1


    if puntaje1 >= x or puntaje2 >= x:
        print("->!Algun jugador llego o supero al puntaje deseado")

        
        
        if puntaje2 >= x and puntaje1 < x:
            ganador = "El Ganador es "+ nombre2
            nombre_ganador = nombre2

        elif puntaje1 >= x and puntaje2 < x:
            ganador = "El Ganador es "+ nombre1
            nombre_ganador = nombre1

        else :
            if jugadas_ganadas1 > jugadas_ganadas2:
                ganador = "El Ganador es "+ nombre1
                nombre_ganador = nombre1
            elif jugadas_ganadas2 > jugadas_ganadas1:
                ganador = "El Ganador es "+ nombre2
                nombre_ganador = nombre2
            else:
                ganador = "El resultado final es un EMPATE"
                nombre_ganador = "empate"
        break
    else:
        print("->!Ningun Jugador llego al puntaje establecido se vuelve a jugar")
        nronda += 1

print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
print("**************************************")
print("*****          Puntajes          *****")
print("**************************************")
print("El Jugador",nombre1,"termino con un puntaje de",puntaje1,"y una cantidad de",jugadas_ganadas1,"de jugadas ganadas")
print("El Jugador",nombre2,"termino con un puntaje de",puntaje2,"y una cantidad de",jugadas_ganadas2,"de jugadas ganadas")
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
print("**************************************")
print("*****          Resultado         *****")
print("**************************************")
print("--->",ganador,"<--")

print("**************************************")
print("*****            Datos           *****")
print("**************************************")
print("°La cantidad de jugadas realizadas fueron:",nronda)

if rondas_empatadas > 0:
    print("°hubo una cantidad de",rondas_empatadas,"rondas empatadas")
else:
    print("°No hubo rondas empatadas")

porsentaje1 = (aciertos1/nronda)*100
porsentaje2 = (aciertos2/nronda)*100
print("°El jugador",nombre1,"tuvo una cantidad de",porsentaje1,"% de aciertos respecto a la cantidad de rondas jugadas")
print("°El jugador",nombre2,"tuvo una cantidad de",porsentaje2,"% de aciertos respecto a la cantidad de rondas jugadas")


if porsentaje1 > porsentaje2:
    porsentaje_ganador = nombre1
elif porsentaje2 > porsentaje1:
    porsentaje_ganador = nombre2
else:
    porsentaje_ganador = "empate"
#print("El porcentaje ganado es",porsentaje_ganador)

if porsentaje_ganador != "empate":
    if porsentaje_ganador == nombre_ganador:
        print("°el ganador es el que tuvo mayor porcentaje de aciertos")
    elif porsentaje_ganador != nombre_ganador:
        print("°el ganador no es el que tuvo mayor porcentaje de aciertos")
else:
    print("°Los porcentajes son iguales")

if contador_jugadas_ganadas_seguidas >= 3:
    print("°algún jugador ganó en al menos 3 turnos seguidos")