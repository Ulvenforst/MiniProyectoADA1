################################################################################
# Archivo: Equipo.py                                                           #
# Autores: Julián Ernesto Puyo Mora 2226905                                    #
#          Laura Camila Betancourt Horta 2223435                               #
#          Jhoan Felipe León Correa 2228527                                    #
#          Juan Camilo Narváez Tascón 2140112                                  #
# Fecha de creación: 06/02/2024                                                #
# Fecha de última modificación: 06/02/2024                                     #
# Licencia: GNU-GPL                                                            #
################################################################################

# CLASE: Equipo 
# INTENCIÓN: Representar un equipo de un deporte en una sede.
# RELACIONES: Esta clase se relaciona con la clase Jugador; un equipo tiene varios jugadores.
from TablaHash import HashTable
# Make an absolute import to the counting_sort function in ../algorithms/

from algorithms.counting_sort import counting_sort


M = 2      # Número máximo de equipos por sede
K = 2      # Número máximo de sedes en la asociación
N_min = 2  # Número mínimo de jugadores por equipo
N_max = 4  # Número máximo de jugadores por equipo

class Equipo:
    def __init__(self, deporte):
        self._deporte = deporte
        self._jugadores = []
        self._hash_jugadores = HashTable(N_max)

    def agregar_jugadores(self, nuevos_jugadores):
        if len(self._jugadores) + len(nuevos_jugadores) > N_max:
            print(f"El equipo {self._deporte} excederá el tamaño máximo permitido de jugadores.")
            return
        self._jugadores.extend(nuevos_jugadores)

        max_rendimiento = max(jugador.rendimiento for jugador in nuevos_jugadores)
        max_edad = max(jugador.edad for jugador in nuevos_jugadores)
        nuevos_jugadores = counting_sort(nuevos_jugadores, max_edad, key=lambda x: x.edad)
        nuevos_jugadores = counting_sort(nuevos_jugadores, max_rendimiento, key=lambda x: x.rendimiento)

        orden_rendimiento = 0
        for jugador in nuevos_jugadores:
            self._hash_jugadores.insert(orden_rendimiento, jugador)
            orden_rendimiento += 1

        if len(self._jugadores) < N_min:
            print(f"El equipo {self._deporte} no cumple con el tamaño mínimo requerido de jugadores.")

    @property
    def deporte(self):
        return self._deporte

    @property
    def jugadores(self):
        # return self._jugadores
        return self._hash_jugadores

    @deporte.setter
    def deporte(self, deporte):
        self._deporte = deporte

    @jugadores.setter
    def jugadores(self, jugadores):
        self._jugadores = jugadores


if __name__ == "__main__":
    from Jugador import Jugador

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

    # print(futbolCali.jugadores.search(futbolCali.jugadores.len()-1).nombre)

    # volleyballCali = Equipo("Volleyball")
    # volleyballCali.agregar_jugadores([jugadores[0], jugadores[8], jugadores[11], jugadores[5]])
    
    # futbolMedellin = Equipo("Futbol")
    # futbolMedellin.agregar_jugadores([jugadores[10], jugadores[7], jugadores[6]])
    # volleyballMedellin = Equipo("Volleyball")
    # volleyballMedellin.agregar_jugadores([jugadores[2], jugadores[3], jugadores[4]])
    
