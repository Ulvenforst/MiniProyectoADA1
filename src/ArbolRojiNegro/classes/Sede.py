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

from ..data_structures.ArbolRojiNegro import ArbolRojiNegro
from ..data_structures.Nodo import Nodo

M = 10      # Número máximo de equipos por sede

class Sede:
    def __init__(self, nombre):
        self._nombre = nombre
        self._equipos = []
        self._arbol_equipos = ArbolRojiNegro()

    def agregar_equipos(self, nuevos_equipos):
        """
        Agrega nuevos equipos a la sede.

        Args:
            nuevos_equipos (list): Lista de equipos a agregar.

        Returns:
            None
        """
        if len(self._equipos) + len(nuevos_equipos) > M:
            print(f"La sede {self._nombre} excederá el tamaño máximo permitido de equipos.")
            return
        self._equipos.extend(nuevos_equipos)

        for equipo in self.equipos:
            suma_rendimiento_jugadores = sum(jugador.rendimiento for jugador in equipo.jugadores)
            promedio_equipo = suma_rendimiento_jugadores / len(equipo.jugadores)
            self._arbol_equipos.insertar(Nodo(equipo, promedio_equipo, len(equipo.jugadores)))

    @property
    def ranking_equipos(self):
        """
        Getter para el ranking de equipos de la sede.

        Returns:
            list: Lista de equipos ordenados por rendimiento.
        """
        return self._arbol_equipos.in_orden()

    @property
    def nombre(self):
        """
        Getter del atributo nombre.

        Returns:
            str: Nombre de la sede.
        """
        return self._nombre
    
    @property
    def equipos(self):
        """
        Getter del atributo equipos.

        Returns:
            list: Lista de equipos de la sede.
        """
        return self._equipos

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @equipos.setter
    def equipos(self, equipos):
        self._equipos = equipos
