################################################################################
# Archivo: Asociacion.py                                                       #
# Autores: Julián Ernesto Puyo Mora 2226905                                    #
#          Laura Camila Betancourt Horta 2223435                               #
#          Jhoan Felipe León Correa 2228527                                    #
#          Juan Camilo Narváez Tascón 2140112                                  #
# Fecha de creación: 06/02/2024                                                #
# Fecha de última modificación: 06/06/2024                                     #
# Licencia: GNU-GPL                                                            #
################################################################################

# CLASE: Asociacion
# INTENCIÓN: Representar una asociación de deportes.
# RELACIONES: Esta clase se relaciona con la clase Sede; una asociación tiene varias sedes.

from data_structures.TablaHash import HashTable
from utils.sorting_algorithms import bucket_sort, counting_sort
from utils.decorators import extraer_y_ordenar, manage_insertions

K = 2      # Número máximo de sedes en la asociación
MAX_JUGADORES = 100

class Asociacion:
    def __init__(self):
        self._sedes = []
        self._hash_sedes = HashTable(K)
        self._hash_jugadores = HashTable(MAX_JUGADORES)

    @manage_insertions(K, [('rendimiento_promedio', False), ('numero_jugadores', True)], 'sedes')
    def agregar_sedes(self, nuevas_sedes):
        """
        Agrega sedes a la asociación.

        Args:
            nuevas_sedes (list): Lista de sedes a agregar.

        Returns:
            None
        """
        pass

    def ranking_jugadores(self):
        """
        Obtiene el ranking de jugadores de la asociación.

        Returns:
            TablaHash: Ranking de jugadores.
        """
        jugadores = self.obtener_jugadores()
        jugadores = self.ordenar_entidades(jugadores, key='rendimiento')
        for orden_rendimiento, jugador in enumerate(jugadores):
            self._hash_jugadores.insert(orden_rendimiento, jugador)
        return self._hash_jugadores

    def jugador_con_mejor_rendimiento(self):
        """
        Obtiene el jugador con mejor rendimiento de la asociación.

        Returns:
            Jugador: Jugador con mejor rendimiento.
        """
        jugadores = self.ranking_jugadores()
        return jugadores.search(jugadores.len() - 1)

    def jugador_con_peor_rendimiento(self):
        """
        Obtiene el jugador con peor rendimiento de la asociación.

        Returns:
            Jugador: Jugador con peor rendimiento.
        """
        jugadores = self.ranking_jugadores()
        return jugadores.search(0)

    def promedio_edad_jugadores(self):
        """
        Calcula el promedio de edad de los jugadores de la asociación.

        Returns:
            float: Promedio de edad de los jugadores.
        """
        jugadores = self.ranking_jugadores()
        return sum([jugador[1].edad for jugador in jugadores]) / jugadores.len()

    def promedio_rendimiento_jugadores(self):
        """
        Calcula el promedio de rendimiento de los jugadores de la asociación.

        Returns:
            float: Promedio de rendimiento de los jugadores.
        """
        jugadores = self.ranking_jugadores()
        return sum([jugador[1].rendimiento for jugador in jugadores]) / jugadores.len()

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
    def sedes(self):
        """
        Getter de la propiedad sedes.

        Returns:
            TablaHash: Sedes de la asociación.
        """
        return self._hash_sedes

    # Funciones auxiliares:
    def obtener_jugadores(self):
        """
        Obtiene los jugadores de la asociación.

        Returns:
            list: Lista de jugadores de la asociación.
        """
        jugadores = []
        for sede in self._hash_sedes:
            for equipo in sede[1].equipos:
                jugadores.extend([jugador[1] for jugador in equipo[1].jugadores])
        return jugadores

    def obtener_equipos(self):
        """
        Obtiene los equipos de la asociación.

        Returns:
            list: Lista de equipos de la asociación.
        """
        equipos = []
        for sede in self._hash_sedes:
            equipos.extend([equipo[1] for equipo in sede[1].equipos])
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
