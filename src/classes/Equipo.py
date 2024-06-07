################################################################################
# Archivo: Equipo.py                                                           #
# Autores: Julián Ernesto Puyo Mora 2226905                                    #
#          Laura Camila Betancourt Horta 2223435                               #
#          Jhoan Felipe León Correa 2228527                                    #
#          Juan Camilo Narváez Tascón 2140112                                  #
# Fecha de creación: 06/02/2024                                                #
# Fecha de última modificación: 06/06/2024                                     #
# Licencia: GNU-GPL                                                            #
################################################################################

# CLASE: Equipo 
# INTENCIÓN: Representar un equipo de un deporte en una sede.
# RELACIONES: Esta clase se relaciona con la clase Jugador; un equipo tiene varios jugadores.


from data_structures.TablaHash import HashTable
from utils.decorators import manage_insertions

N_min = 2  # Número mínimo de jugadores por equipo
N_max = 4  # Número máximo de jugadores por equipo

class Equipo:
    def __init__(self, deporte):
        self._deporte = deporte
        self._jugadores = []
        self._hash_jugadores = HashTable(N_max)
        self._rendimiento_promedio = 0
        self._numero_jugadores = 0

    @manage_insertions(N_max, [('edad', True), ('rendimiento', False)], 'jugadores')
    def agregar_jugadores(self, nuevos_jugadores):
        self._rendimiento_promedio = sum(j[1].rendimiento for j in self._hash_jugadores) / self._hash_jugadores.len()

    def __str__(self):
        return f"Equipo de {self._deporte} - Rendimiento promedio: {self._rendimiento_promedio}"

    def __lt__(self, other):
        return self._rendimiento_promedio < other._rendimiento_promedio

    def __le__(self, other):
        return self._rendimiento_promedio <= other._rendimiento_promedio

    def __gt__(self, other):
        return self._rendimiento_promedio > other._rendimiento_promedio

    def __ge__(self, other):
        return self._rendimiento_promedio >= other._rendimiento_promedio

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

    @property
    def rendimiento_promedio(self):
        return self._rendimiento_promedio

    @property
    def numero_jugadores(self):
        return self._numero_jugadores
    
