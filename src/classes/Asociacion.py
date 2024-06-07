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

class Asociacion:
    def __init__(self):
        self._sedes = []
        self._hash_sedes = HashTable(K)
        self._hash_jugadores = HashTable(100)

    @manage_insertions(K, [('rendimiento_promedio', False), ('numero_jugadores', True)], 'sedes')
    def agregar_sedes(self, nuevas_sedes):
        pass

    def ranking_jugadores(self):
        jugadores = self.obtener_jugadores()
        jugadores = self.ordenar_entidades(jugadores, key='rendimiento')
        for orden_rendimiento, jugador in enumerate(jugadores):
            self._hash_jugadores.insert(orden_rendimiento, jugador)
        return self._hash_jugadores

    @extraer_y_ordenar(tipo_entidad='equipos', clave='rendimiento_promedio')
    def equipo_con_menor_rendimiento(self, equipos):
        return equipos[0]

    @extraer_y_ordenar(tipo_entidad='equipos', clave='rendimiento_promedio', reverse=True)
    def equipo_con_mayor_rendimiento(self, equipos):
        return equipos[0]

    @extraer_y_ordenar(tipo_entidad='jugadores', clave='edad', reverse=True)
    def jugador_mas_viejo(self, jugadores):
        return jugadores[0]
    
    @extraer_y_ordenar(tipo_entidad='jugadores', clave='edad')
    def jugador_mas_joven(self, jugadores):
        return jugadores[0]

    def jugador_con_mejor_rendimiento(self):
        jugadores = self.ranking_jugadores()
        return jugadores.search(jugadores.len() - 1)

    def jugador_con_peor_rendimiento(self):
        jugadores = self.ranking_jugadores()
        return jugadores.search(0)

    def promedio_edad_jugadores(self):
        jugadores = self.ranking_jugadores()
        return sum([jugador[1].edad for jugador in jugadores]) / jugadores.len()

    def promedio_rendimiento_jugadores(self):
        jugadores = self.ranking_jugadores()
        return sum([jugador[1].rendimiento for jugador in jugadores]) / jugadores.len()

    @property
    def sedes(self):
        return self._hash_sedes

    def obtener_jugadores(self):
        jugadores = []
        for sede in self._hash_sedes:
            for equipo in sede[1].equipos:
                jugadores.extend([jugador[1] for jugador in equipo[1].jugadores])
        return jugadores

    def obtener_equipos(self):
        equipos = []
        for sede in self._hash_sedes:
            equipos.extend([equipo[1] for equipo in sede[1].equipos])
        return equipos

    def ordenar_entidades(self, entidades, key, reverse=False):
        if key in ['rendimiento', 'edad']:
            return counting_sort(entidades, key=lambda x: getattr(x, key), reverse=reverse)
        return bucket_sort(entidades, key=lambda x: getattr(x, key), reverse=reverse)
