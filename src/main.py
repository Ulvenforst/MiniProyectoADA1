################################################################################
# Archivo: main.py                                                             # 
# Autores: Julián Ernesto Puyo Mora 2226905                                    #
#          Laura Camila Betancourt Horta 222____                               #
#          Jhoan Felipe León Correa 2228527                                    #
#          Juan Camilo Narváez Tascón 2140112                                  #
# Fecha de creación: 06/02/2024                                                #
# Fecha de última modificación: 06/02/2024                                     #
# Licencia: GNU-GPL                                                            #
################################################################################

# HISTORIA: 

from classes import Asociacion, Jugador, Equipo, Sede

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
futbolCali = Equipo("Futbol")
futbolCali.agregar_jugadores([jugadores[9], jugadores[1]])
volleyballCali = Equipo("Volleyball")
volleyballCali.agregar_jugadores([jugadores[0], jugadores[8], jugadores[11], jugadores[5]])

futbolMedellin = Equipo("Futbol")
futbolMedellin.agregar_jugadores([jugadores[10], jugadores[7], jugadores[6]])
volleyballMedellin = Equipo("Volleyball")
volleyballMedellin.agregar_jugadores([jugadores[2], jugadores[3], jugadores[4]])

sedeCali = Sede("Cali")
sedeCali.equipos.extend([futbolCali, volleyballCali])
sedeMedellin = Sede("Medellín")
sedeMedellin.equipos.extend([futbolMedellin, volleyballMedellin])

asociacion.sedes.extend([sedeCali, sedeMedellin])
