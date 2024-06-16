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

from ..data_structures.ArbolRojiNegro import ArbolRojiNegro
from ..data_structures.Nodo import Nodo

N_min = 2  # Número mínimo de jugadores por equipo
N_max = 10  # Número máximo de jugadores por equipo

class Equipo:
    def __init__(self, deporte):
        self._deporte = deporte
        self._jugadores = []
        self._arbol_jugadores = ArbolRojiNegro()
        self._arbol_jugadores_edad = ArbolRojiNegro()

    def agregar_jugadores(self, nuevos_jugadores):
        """
        Agrega nuevos jugadores al equipo.

        Args:
            nuevos_jugadores (list): Lista de jugadores a agregar.

        Returns:
            None
        """
        if len(self._jugadores) + len(nuevos_jugadores) > N_max:
            print(f"El equipo {self._deporte} excederá el tamaño máximo permitido de jugadores.")
            return
        self._jugadores.extend(nuevos_jugadores)

        for jugador in nuevos_jugadores:
            self._arbol_jugadores.insertar(Nodo(jugador, jugador.rendimiento, jugador.edad))
            self._arbol_jugadores_edad.insertar(Nodo(jugador, jugador.edad, jugador.rendimiento))
            
        if len(self._jugadores) < N_min:
            print(f"El equipo {self._deporte} no cumple con el tamaño mínimo requerido de jugadores.")

    @property
    def ranking_jugadores(self):
        """
        Getter para el ranking de jugadores del equipo.

        Returns:
            list: Lista de jugadores ordenados por rendimiento.
        """
        return self._arbol_jugadores.in_orden()

    @property
    def deporte(self):
        """
        Getter para el deporte del equipo.

        Returns:
            str: Deporte del equipo.
        """
        return self._deporte

    @property
    def jugadores(self):
        """
        Getter para los jugadores del equipo.

        Returns:
            list: Lista de jugadores del equipo.
        """
        return self._jugadores

    @deporte.setter
    def deporte(self, deporte):
        self._deporte = deporte

    @jugadores.setter
    def jugadores(self, jugadores):
        self._jugadores = jugadores

    # Métodos mágicos
    def __str__(self):
        return f"Equipo de {self._deporte}"
