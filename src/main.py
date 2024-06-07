################################################################################
# Archivo: main.py                                                             # 
# Autores: Julián Ernesto Puyo Mora 2226905                                    #
#          Laura Camila Betancourt Horta 2223435                               #
#          Jhoan Felipe León Correa 2228527                                    #
#          Juan Camilo Narváez Tascón 2140112                                  #
# Fecha de creación: 06/02/2024                                                #
# Fecha de última modificación: 06/02/2024                                     #
# Licencia: GNU-GPL                                                            #
################################################################################

# HISTORIA: Este programa está diseñado para la "Asociación de Deportes" que busca 
# optimizar el rendimiento y la distribución de recursos entre sus equipos y jugadores. 
# La asociación administra múltiples sedes a nivel nacional, cada una con varios 
# equipos deportivos. Los jugadores de estos equipos son evaluados en base a su 
# rendimiento y edad para organizar y optimizar los equipos dentro de cada sede. 
# El programa prioriza los jugadores y equipos con mejor rendimiento para la asignación 
# de recursos, mientras identifica aquellos que necesitan mejoras. Se implementan 
# algoritmos para clasificar sedes, equipos y jugadores de acuerdo a su rendimiento 
# y otros criterios. Se entrega con informe, código fuente y documentación detallada 
# sobre su ejecución y estructura de archivos.

from classes import Asociacion, Jugador, Equipo, Sede

if __name__ == "__main__":
    asociacion = Asociacion()

    # Crear jugadores
    jugadores = [
            Jugador("Sofia García", 21, 66), Jugador("Alejandro Torres", 27, 24),
            Jugador("Valentina Rodriguez", 19, 15), Jugador("Juan López", 22, 78),
            Jugador("Martina Martinez", 30, 55), Jugador("Sebastián Pérez", 25, 42),
            Jugador("Camila Fernández", 24, 36), Jugador("Mateo González", 29, 89),
            Jugador("Isabella Díaz", 21, 92), Jugador("Daniel Ruiz", 17, 57),
            Jugador("Luciana Sánchez", 18, 89), Jugador("Lucas Vásquez", 26, 82)
    ]
    
    # Crear equipos y sedes
    futbolCali = Equipo("Futbol Cali")
    futbolCali.agregar_jugadores([jugadores[9], jugadores[1]])
    volleyballCali = Equipo("Volleyball Cali")
    volleyballCali.agregar_jugadores([jugadores[0], jugadores[8], jugadores[11], jugadores[5]])
    
    futbolMedellin = Equipo("Futbol Medellín")
    futbolMedellin.agregar_jugadores([jugadores[10], jugadores[7], jugadores[6]])
    volleyballMedellin = Equipo("Volleyball Medellín")
    volleyballMedellin.agregar_jugadores([jugadores[2], jugadores[3], jugadores[4]])
    
    sedeCali = Sede("Cali")
    sedeCali.agregar_equipos([futbolCali, volleyballCali])
    sedeMedellin = Sede("Medellín")
    sedeMedellin.agregar_equipos([futbolMedellin, volleyballMedellin])

    asociacion.agregar_sedes([sedeCali, sedeMedellin])
    
    # # Imprimir los jugadores del equipo de futbol de medellin
    # print("Jugadores del equipo de futbol de Medellín:")
    # for jugador in futbolMedellin.jugadores:
    #     print(jugador[1].identificador)

    # print()
    # # Imprimir los jugadores del equipo de volleyball de medellin
    # print("Jugadores del equipo de volleyball de Medellín:")
    # for jugador in volleyballMedellin.jugadores:
    #     print(jugador[1].identificador)

    # print()
    # # Imprimir los jugadores del equipo de futbol de cali
    # print("Jugadores del equipo de futbol de Cali:")
    # for jugador in futbolCali.jugadores:
    #     print(jugador[1].identificador)

    # print()
    # # Imprimir los jugadores del equipo de volleyball de cali
    # print("Jugadores del equipo de volleyball de Cali:")
    # for jugador in volleyballCali.jugadores:
    #     print(jugador[1].identificador)

    # print()
    # # Imprimir el ranking de jugadores de la asociacion
    # print("Ranking de jugadores de la asociación:")
    # for jugador in asociacion.ranking_jugadores():
    #     print(jugador[1].identificador)

    # print()
    # Imprimir el equipo con mayor rendimiento
    print("Equipo con menor rendimiento promedio:")
    print(asociacion.equipo_con_mayor_rendimiento().deporte)


    # print()
    # Imprimir el equipo con menor rendimiento
    print("Equipo con mayor rendimiento promedio:")
    print(asociacion.equipo_con_menor_rendimiento().deporte)

    # print()
    # Imprimir el jugador con mayor rendimiento
    print("Jugador con mejor rendimiento:")
    print(asociacion.jugador_con_mejor_rendimiento().identificador)

    # print()
    # Imprimir el jugador con menor rendimiento
    print("Jugador con peor rendimiento:")
    print(asociacion.jugador_con_peor_rendimiento().identificador)

    # print()
    # Imprimir el jugador con menor edad
    print("Jugador más joven:")
    print(asociacion.jugador_mas_joven().identificador)

    # print()
    # Imprimir el jugador con mayor edad
    print("Jugador más viejo:")
    print(asociacion.jugador_mas_viejo().identificador)

    # print()
    # Imprimir el promedio de edad de los jugadores
    print("Promedio de edad de los jugadores:")
    print(asociacion.promedio_edad_jugadores())

    # print()
    # Imprimir el promedio de rendimiento de los jugadores
    print("Promedio de rendimiento de los jugadores:")
    print(asociacion.promedio_rendimiento_jugadores())

