################################################################################
# Archivo: Asociacion.py                                                       #
# Autores: Julián Ernesto Puyo Mora 2226905                                    #
#          Laura Camila Betancourt Horta 2223435                               #
#          Jhoan Felipe León Correa 2228527                                    #
#          Juan Camilo Narváez Tascón 2140112                                  #
# Fecha de creación: 06/02/2024                                                #
# Fecha de última modificación: 06/07/2024                                     #
# Licencia: GNU-GPL                                                            #
################################################################################

# CLASE: Asociacion
# INTENCIÓN: Representar una asociación de deportes.
# RELACIONES: Esta clase se relaciona con la clase Sede; una asociación tiene varias sedes.

from ..utils.sorting_algorithms import counting_sort, bucket_sort
from ..utils.decorators import extraer_y_ordenar, manage_insertions
from .Jugador import Jugador

K = 10      # Número máximo de sedes en la asociación

class Asociacion:
    def __init__(self):
        self._list_sedes = []
        self._list_jugadores = []

    @manage_insertions(K, [('rendimiento_promedio', True), ('numero_jugadores', False)], 'sedes')
    def agregar_sedes(self, nuevas_sedes):
        """
        Agrega sedes a la asociación.

        Args:
            nuevas_sedes (list): Lista de sedes a agregar.

        Returns:
            None
        """
        self.ranking_jugadores()

    def ranking_jugadores(self) -> list:
        """
        Obtiene el ranking de jugadores de la asociación.

        Returns:
            TablaHash: Ranking de jugadores.
        """
        self._list_jugadores = self.obtener_jugadores()
        self._list_jugadores = self.ordenar_entidades(self._list_jugadores, key='rendimiento')
        return self._list_jugadores
    
    def resetear_datos():
        """
        Reinicia los datos de la asociación.

        Returns:
            None
        """
        Jugador.reset_contador()

    def jugador_con_mejor_rendimiento(self):
        """
        Obtiene el jugador con mejor rendimiento de la asociación.

        Returns:
            Jugador: Jugador con mejor rendimiento.
        """
        return self._list_jugadores[-1]

    def jugador_con_peor_rendimiento(self):
        """
        Obtiene el jugador con peor rendimiento de la asociación.

        Returns:
            Jugador: Jugador con peor rendimiento.
        """
        return self._list_jugadores[0]

    def promedio_edad_jugadores(self):
        """
        Calcula el promedio de edad de los jugadores de la asociación.

        Returns:
            float: Promedio de edad de los jugadores.
        """
        return sum([jugador.edad for jugador in self._list_jugadores]) / len(self._list_jugadores)

    def promedio_rendimiento_jugadores(self):
        """
        Calcula el promedio de rendimiento de los jugadores de la asociación.

        Returns:
            float: Promedio de rendimiento de los jugadores.
        """
        return sum([jugador.rendimiento for jugador in self._list_jugadores]) / len(self._list_jugadores)

    @extraer_y_ordenar(tipo_entidad='equipos', clave='rendimiento_promedio')
    def equipo_con_menor_rendimiento(self, equipos):
        """
        Obtiene el equipo con menor rendimiento de la asociación.

        Args:
            equipos (list): Lista de equipos de la asociación.

        Returns:
            Equipo: Equipo con menor rendimiento.
        """
        return equipos[0]

    @extraer_y_ordenar(tipo_entidad='equipos', clave='rendimiento_promedio', reverse=True)
    def equipo_con_mayor_rendimiento(self, equipos):
        """
        Obtiene el equipo con mayor rendimiento de la asociación.

        Args:
            equipos (list): Lista de equipos de la asociación.

        Returns:
            Equipo: Equipo con mayor rendimiento.
        """
        return equipos[0]

    @extraer_y_ordenar(tipo_entidad='jugadores', clave='edad', reverse=True)
    def jugador_mas_viejo(self, jugadores):
        """
        Obtiene el jugador más viejo de la asociación.

        Args:
            jugadores (list): Lista de jugadores de la asociación.

        Returns:
            Jugador: Jugador más viejo.
        """
        return jugadores[0]
    
    @extraer_y_ordenar(tipo_entidad='jugadores', clave='edad')
    def jugador_mas_joven(self, jugadores):
        """
        Obtiene el jugador más joven de la asociación.

        Args:
            jugadores (list): Lista de jugadores de la asociación.

        Returns:
            Jugador: Jugador más joven.
        """
        return jugadores[0]

    @property
    def ranking_sedes(self):
        """
        Getter de la propiedad sedes.

        Returns:
            TablaHash: Sedes de la asociación.
        """
        return self._list_sedes

    # Funciones auxiliares:
    def obtener_jugadores(self):
        """
        Obtiene los jugadores de la asociación.

        Returns:
            list: Lista de jugadores de la asociación.
        """
        jugadores = []
        for sede in self._list_sedes:
            for equipo in sede.equipos: jugadores.extend([jugador for jugador in equipo.ranking_jugadores])
        return jugadores

    def obtener_equipos(self):
        """
        Obtiene los equipos de la asociación.

        Returns:
            list: Lista de equipos de la asociación.
        """
        equipos = []
        for sede in self._list_sedes: equipos.extend([equipo for equipo in sede.equipos])
        return equipos

    def ordenar_entidades(self, entidades, key, reverse=False):
        """
        Ordena las entidades de la asociación.

        Args:
            entidades (list): Lista de entidades a ordenar.
            key (str): Clave por la que se ordenarán las entidades.
            reverse (bool): Indica si el ordenamiento es descendente.

        Returns:
            list: Lista de entidades ordenadas.
        """
        if key in ['rendimiento', 'edad']:
            return counting_sort(entidades, key=lambda x: getattr(x, key), reverse=reverse)
        return bucket_sort(entidades, key=lambda x: getattr(x, key), reverse=reverse)
