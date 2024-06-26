################################################################################
# Archivo: Equipo.py                                                           #
# Autores: Julián Ernesto Puyo Mora 2226905                                    #
#          Laura Camila Betancourt Horta 2223435                               #
#          Jhoan Felipe León Correa 2228527                                    #
#          Juan Camilo Narváez Tascón 2140112                                  #
# Fecha de creación: 06/02/2024                                                #
# Fecha de última modificación: 06/07/2024                                     #
# Licencia: GNU-GPL                                                            #
################################################################################

# CLASE: Equipo 
# INTENCIÓN: Representar un equipo de un deporte en una sede.
# RELACIONES: Esta clase se relaciona con la clase Jugador; un equipo tiene varios jugadores.

from ..utils.decorators import manage_insertions

N_min = 2  # Número mínimo de jugadores por equipo
N_max = 10  # Número máximo de jugadores por equipo

class Equipo:
    def __init__(self, deporte):
        self._deporte = deporte
        self._list_jugadores = []
        self._rendimiento_promedio = 0
        self._numero_jugadores = 0

    @manage_insertions(N_max, [('edad', True), ('rendimiento', False)], 'jugadores')
    def agregar_jugadores(self, nuevos_jugadores):
        """
        Agrega jugadores al equipo.

        Args:
            nuevos_jugadores (list): Lista de jugadores a agregar.

        Returns:
            None
        """
        self._rendimiento_promedio = sum(j.rendimiento for j in self._list_jugadores) / len(self._list_jugadores)

    @property
    def deporte(self):
        """
        Getter del atributo deporte.

        Returns:
            str: Deporte del equipo.
        """
        return self._deporte

    @property
    def ranking_jugadores(self):
        """
        Getter del atributo jugadores.

        Returns:
            HashTable: Tabla hash de jugadores.

        """
        return self._list_jugadores

    @property
    def rendimiento_promedio(self):
        """
        Getter del atributo rendimiento_promedio.

        Returns:
            float: Rendimiento promedio de los jugadores del equipo.
        """
        return self._rendimiento_promedio

    @property
    def numero_jugadores(self):
        """
        Getter del atributo numero_jugadores.

        Returns:
            int: Número de jugadores del equipo.
        """
        return self._numero_jugadores

    @deporte.setter
    def deporte(self, deporte):
        self._deporte = deporte

    @ranking_jugadores.setter
    def ranking_jugadores(self, jugadores):
        self._list_jugadores = jugadores
    
    # Métodos mágicos:
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
