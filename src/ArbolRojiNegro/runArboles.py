################################################################################
# Archivo: runArboles.py                                                       #
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

from .classes import Asociacion, Jugador, Equipo, Sede

def runArboles():
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
    print("-------------------")
    futbolCali = Equipo("Futbol Cali")
    futbolCali.agregar_jugadores([jugadores[9], jugadores[1]])
    for jugador in futbolCali.ranking_jugadores(): print(jugador)
    print("-------------------")
    volleyballCali = Equipo("Volleyball Cali")
    volleyballCali.agregar_jugadores([jugadores[0], jugadores[8], jugadores[11], jugadores[5]])
    for jugador in volleyballCali.ranking_jugadores(): print(jugador)
    print("-------------------")
    sedeCali = Sede("Cali")
    sedeCali.agregar_equipos([futbolCali, volleyballCali])
    for equipo in sedeCali.ranking_equipos(): print(equipo)
    print("-------------------")
    futbolMedellin = Equipo("Futbol Medellin")
    futbolMedellin.agregar_jugadores([jugadores[10], jugadores[7], jugadores[6]])
    for jugador in futbolMedellin.ranking_jugadores(): print(jugador)
    print("-------------------")
    volleyballMedellin = Equipo("Volleyball Medellin")
    volleyballMedellin.agregar_jugadores([jugadores[2], jugadores[3], jugadores[4]])
    for jugador in volleyballMedellin.ranking_jugadores(): print(jugador)
    print("-------------------")
    sedeMedellin = Sede("Medellín")
    sedeMedellin.agregar_equipos([futbolMedellin, volleyballMedellin])
    for equipo in sedeMedellin.ranking_equipos(): print(equipo)
    asociacion.agregar_sede([sedeCali, sedeMedellin])
    print("-------------------")
    print("Jugador con mayor rendimiento:")
    print(asociacion.jugador_mayor_rendimiento())
    print("-------------------")
    print("Jugador con menor rendimiento:")
    print(asociacion.jugador_menor_rendimiento())
    print("-------------------")
    print("Equipo con mayor rendimiento:")
    print(asociacion.equipo_mayor_rendimiento())
    print("-------------------")
    print("Equipo con menor rendimiento:")
    print(asociacion.equipo_menor_rendimiento())
    print("-------------------")
    print("Juagadores con mayor edad:")
    print(asociacion.jugador_mayor_edad())
    print("-------------------")
    print("Juagadores con menor edad:")
    print(asociacion.jugador_menor_edad())
    print("-------------------")
    print("Promedio de rendimiento:")
    print(asociacion.promedio_rendimiento())
    print("-------------------")
    print("Promedio de edad:")
    print(asociacion.promedio_edad())
