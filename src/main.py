################################################################################
# Archivo: main.py                                                             # 
# Autores: Julián Ernesto Puyo Mora 2226905                                    #
#          Laura Camila Betancourt Horta 2223435                               #
#          Jhoan Felipe León Correa 2228527                                    #
#          Juan Camilo Narváez Tascón 2140112                                  #
# Fecha de creación: 06/02/2024                                                #
# Fecha de última modificación: 06/07/2024                                     #
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

from classes import Jugador, Equipo, Sede, Asociacion

if __name__ == "__main__":
    asociacion = Asociacion()

    # Crear jugadores
    # jugadores = [
    #         Jugador("Sofia García", 21, 66), Jugador("Alejandro Torres", 27, 24),
    #         Jugador("Valentina Rodriguez", 19, 15), Jugador("Juan López", 22, 78),
    #         Jugador("Martina Martinez", 30, 55), Jugador("Sebastián Pérez", 25, 42),
    #         Jugador("Camila Fernández", 24, 36), Jugador("Mateo González", 29, 89),
    #         Jugador("Isabella Díaz", 21, 92), Jugador("Daniel Ruiz", 17, 57),
    #         Jugador("Luciana Sánchez", 18, 89), Jugador("Lucas Vásquez", 26, 82)
    # ]
    
    # # Crear equipos y sedes
    # futbolCali = Equipo("Futbol Cali")
    # futbolCali.agregar_jugadores([jugadores[9], jugadores[1]])
    # volleyballCali = Equipo("Volleyball Cali")
    # volleyballCali.agregar_jugadores([jugadores[0], jugadores[8], jugadores[11], jugadores[5]])

    # futbolMedellin = Equipo("Futbol Medellín")
    # futbolMedellin.agregar_jugadores([jugadores[10], jugadores[7], jugadores[6]])
    # volleyballMedellin = Equipo("Volleyball Medellín")
    # volleyballMedellin.agregar_jugadores([jugadores[2], jugadores[3], jugadores[4]])
    
    # sedeCali = Sede("Cali")
    # sedeCali.agregar_equipos([futbolCali, volleyballCali])
    # sedeMedellin = Sede("Medellín")
    # sedeMedellin.agregar_equipos([futbolMedellin, volleyballMedellin])

    # asociacion.agregar_sedes([sedeCali, sedeMedellin])
    
    # print("-------------------")
    # print("Jugadores del equipo de futbol de Medellín:")
    # for jugador in futbolMedellin.jugadores: print(jugador)
    # print("-------------------")
    # print("Jugadores del equipo de volleyball de Medellín:")
    # for jugador in volleyballMedellin.jugadores: print(jugador)
    # print("-------------------")
    # print("Jugadores del equipo de futbol de Cali:")
    # for jugador in futbolCali.jugadores: print(jugador)
    # print("-------------------")
    # print("Jugadores del equipo de volleyball de Cali:")
    # for jugador in volleyballCali.jugadores: print(jugador)
    # print("-------------------")
    # print("Ranking de jugadores de la asociación:")
    # for jugador in asociacion.ranking_jugadores(): print(jugador)
    # print("-------------------")
    # print("Equipo con mayor rendimiento promedio:")
    # print(asociacion.equipo_con_mayor_rendimiento())
    # print("-------------------")
    # print("Equipo con menor rendimiento promedio:")
    # print(asociacion.equipo_con_menor_rendimiento())
    # print("-------------------")
    # print("Jugador con mejor rendimiento:")
    # print(asociacion.jugador_con_mejor_rendimiento())
    # print("-------------------")
    # print("Jugador con peor rendimiento:")
    # print(asociacion.jugador_con_peor_rendimiento())
    # print("-------------------")
    # print("Jugador más joven:")
    # print(asociacion.jugador_mas_joven())
    # print("-------------------")
    # print("Jugador más viejo:")
    # print(asociacion.jugador_mas_viejo())
    # print("-------------------")
    # print("Promedio de edad de los jugadores:")
    # print(asociacion.promedio_edad_jugadores())
    # print("-------------------")
    # print("Promedio de rendimiento de los jugadores:")
    # print(asociacion.promedio_rendimiento_jugadores())

    j1 = Jugador("Juan", 20, 94)
    j2 = Jugador("Maria", 21, 94)
    j3 = Jugador("Pedro", 22, 21)
    j4 = Jugador("Ana", 23, 25)
    j5 = Jugador("Carlos", 24, 66)
    j6 = Jugador("Laura", 25, 52)
    j7 = Jugador("Jose", 26, 48)
    j8 = Jugador("Luis", 27, 73)
    j9 = Jugador("Sara", 28, 92)
    j10 = Jugador("Jorge", 29, 51)
    j11 = Jugador("Lorena", 30, 90)
    j12 = Jugador("Raul", 31, 100)
    
    e1 = Equipo("Futbol" )
    e1.agregar_jugadores([j1, j2, j3])
    e2 = Equipo("Volleyball")
    e2.agregar_jugadores([j4, j5, j6])
    e3 = Equipo("Futbol")
    e3.agregar_jugadores([j7, j8, j9])
    e4 = Equipo("Volleyball")
    
    s1 = Sede("Sede Cali")
    s1.agregar_equipos([e1, e2])
    s2 = Sede("Sede Medellin")
    s2.agregar_equipos([e3, e4])

    print("-------------------")
    print("Sede cali rendimiento promedio:")
    print(s1.rendimiento_promedio)

    print("-------------------")
    print("Rendimiento de Volleyball:")
    print(e2.rendimiento_promedio)

    print("-------------------")
    print("Rendimiento de Futbol:")
    print(e1.rendimiento_promedio)
    

