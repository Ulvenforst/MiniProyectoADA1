################################################################################
# Archivo: Sede.py                                                             # 
# Autores: Julián Ernesto Puyo Mora 2226905                                    #
#          Laura Camila Betancourt Horta 2223435                               #
#          Jhoan Felipe León Correa 2228527                                    #
#          Juan Camilo Narváez Tascón 2140112                                  #
# Fecha de creación: 06/02/2024                                                #
# Fecha de última modificación: 06/02/2024                                     #
# Licencia: GNU-GPL                                                            #
################################################################################

# CLASE: Sede 
# INTENCIÓN: Representar una sede de la asociación de deportes.
# RELACIONES: Esta clase se relaciona con la clase Equipo; una sede tiene varios equipos.

from .Equipo import Equipo 
from ..data_structures.ArbolRojiNegro import ArbolRojiNegro
from ..data_structures.Nodo import Nodo

M = 2      # Número máximo de equipos por sede

class Sede:
    def __init__(self, nombre):
        self._nombre = nombre
        self._equipos = []
        self._arbol_equipos = ArbolRojiNegro()

    def agregar_equipos(self, nuevos_equipos):
        if len(self._equipos) + len(nuevos_equipos) > M:
            print(f"La sede {self._nombre} excederá el tamaño máximo permitido de equipos.")
            return
        self._equipos.extend(nuevos_equipos)

        for equipo in self.equipos:
            suma_rendimiento_jugadores = sum(jugador.rendimiento for jugador in equipo.jugadores)
            promedio_equipo = suma_rendimiento_jugadores / len(equipo.jugadores)
            self._arbol_equipos.insertar(Nodo(equipo.deporte, promedio_equipo, len(equipo.jugadores)))

    def ranking_equipos(self):
        return self._arbol_equipos.in_orden()

    @property
    def nombre(self):
        return self._nombre
    
    @property
    def equipos(self):
        return self._equipos

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @equipos.setter
    def equipos(self, equipos):
        self._equipos = equipos
