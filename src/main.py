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
    # asociacion = Asociacion()

    jugadores = [
        Jugador("Sofia García", 21, 66), Jugador("Alejandro Torres", 27, 24),
        Jugador("Valentina Rodriguez", 19, 15), Jugador("Juan López", 22, 78),
        Jugador("Martina Martinez", 30, 55), Jugador("Sebastián Pérez", 25, 42),
        Jugador("Camila Fernández", 24, 36), Jugador("Mateo González", 29, 89),
        Jugador("Isabella Díaz", 21, 92), Jugador("Daniel Ruiz", 17, 57),
        Jugador("Luciana Sánchez", 18, 89), Jugador("Lucas Vásquez", 26, 82)
    ]
    
    # Crear equipos y sedes
    futbolCali = Equipo("Futbol")
    futbolCali.agregar_jugadores([jugadores[0], jugadores[1], jugadores[2], jugadores[3]])

    for jugador in futbolCali.jugadores:
        print(jugador[0], jugador[1].nombre, jugador[1].rendimiento)

    print(futbolCali.rendimiento_promedio)
    
    sedeCali = Sede("Cali")
    sedeCali.agregar_equipos([futbolCali])

    for equipo in sedeCali.equipos:
        print(equipo[0], equipo[1].deporte, equipo[1].rendimiento_promedio)

    print(sedeCali.rendimiento_promedio)
    # # Crear jugadores
    # jugadores = [
    #     Jugador("Sofia García", 21, 66), Jugador("Alejandro Torres", 27, 24),
    #     Jugador("Valentina Rodriguez", 19, 15), Jugador("Juan López", 22, 78),
    #     Jugador("Martina Martinez", 30, 55), Jugador("Sebastián Pérez", 25, 42),
    #     Jugador("Camila Fernández", 24, 36), Jugador("Mateo González", 29, 89),
    #     Jugador("Isabella Díaz", 21, 92), Jugador("Daniel Ruiz", 17, 57),
    #     Jugador("Luciana Sánchez", 18, 89), Jugador("Lucas Vásquez", 26, 82)
    # ]
    
    # # Crear equipos y sedes
    # futbolCali = Equipo("Futbol")
    # futbolCali.agregar_jugadores([jugadores[9], jugadores[1]])
    # volleyballCali = Equipo("Volleyball")
    # volleyballCali.agregar_jugadores([jugadores[0], jugadores[8], jugadores[11], jugadores[5]])
    
    # futbolMedellin = Equipo("Futbol")
    # futbolMedellin.agregar_jugadores([jugadores[10], jugadores[7], jugadores[6]])
    # volleyballMedellin = Equipo("Volleyball")
    # volleyballMedellin.agregar_jugadores([jugadores[2], jugadores[3], jugadores[4]])
    
    # sedeMedellin = Sede("Medellín")
    # sedeMedellin.agregar_equipos([futbolMedellin, volleyballMedellin])
    
    # asociacion.sedes.extend([sedeCali, sedeMedellin])

    # print(futbolCali._hash_jugadores)

