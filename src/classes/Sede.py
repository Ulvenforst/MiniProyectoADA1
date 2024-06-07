################################################################################
# Archivo: Sede.py                                                             # 
# Autores: Julián Ernesto Puyo Mora 2226905                                    #
#          Laura Camila Betancourt Horta 2223435                               #
#          Jhoan Felipe León Correa 2228527                                    #
#          Juan Camilo Narváez Tascón 2140112                                  #
# Fecha de creación: 06/02/2024                                                #
# Fecha de última modificación: 06/06/2024                                     #
# Licencia: GNU-GPL                                                            #
################################################################################

# CLASE: Sede 
# INTENCIÓN: Representar una sede de la asociación de deportes.
# RELACIONES: Esta clase se relaciona con la clase Equipo; una sede tiene varios equipos.

from data_structures.TablaHash import HashTable
from utils.decorators import manage_insertions

M = 2      # Número máximo de equipos por sede

class Sede:
    def __init__(self, nombre):
        self._nombre = nombre
        self._equipos = []
        self._hash_equipos = HashTable(M)
        self._rendimiento_promedio = 0
        self._numero_jugadores = 0

    @manage_insertions(M, [('rendimiento_promedio', False), ('numero_jugadores', True)], 'equipos')
    def agregar_equipos(self, nuevos_equipos):
        self._rendimiento_promedio = sum(e[1].rendimiento_promedio for e in self._hash_equipos) / self._hash_equipos.len()

    @property
    def nombre(self):
        return self._nombre
    
    @property
    def equipos(self):
        return self._hash_equipos

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @equipos.setter
    def equipos(self, equipos):
        self._equipos = equipos

    @property
    def rendimiento_promedio(self):
        return self._rendimiento_promedio
    
    @property
    def numero_jugadores(self):
        return self._numero_jugadores

