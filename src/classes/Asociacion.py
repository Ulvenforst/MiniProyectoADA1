################################################################################
# Archivo: Asociacion.py                                                       #
# Autores: Julián Ernesto Puyo Mora 2226905                                    #
#          Laura Camila Betancourt Horta 2223435                               #
#          Jhoan Felipe León Correa 2228527                                    #
#          Juan Camilo Narváez Tascón 2140112                                  #
# Fecha de creación: 06/02/2024                                                #
# Fecha de última modificación: 06/02/2024                                     #
# Licencia: GNU-GPL                                                            #
################################################################################

# CLASE: Asociacion
# INTENCIÓN: Representar una asociación de deportes.
# RELACIONES: Esta clase se relaciona con la clase Sede; una asociación tiene varias sedes.

from .TablaHash import HashTable
from algorithms.sorting import bucket_sort, counting_sort

K = 2      # Número máximo de sedes en la asociación

class Asociacion:
    def __init__(self):
        self._sedes = []
        self._hash_sedes = HashTable(K)
        self._hash_jugadores = HashTable(100)

    def agregar_sedes(self, nuevas_sedes):
        if len(self._sedes) + len(nuevas_sedes) > K:
            print("La asociación excederá el tamaño máximo permitido de sedes.")
            return
        
        nuevas_sedes = bucket_sort(nuevas_sedes, key=lambda x: x.rendimiento_promedio)
        nuevas_sedes = counting_sort(nuevas_sedes, key=lambda x: x.numero_jugadores, reverse=True)

        for orden_rendimiento, sede in enumerate(nuevas_sedes):
            self._hash_sedes.insert(orden_rendimiento, sede)

    def ranking_jugadores(self):
        jugadores = self.obtener_jugadores()
        jugadores = self.ordenar_entidades(jugadores, key='rendimiento')
        for orden_rendimiento, jugador in enumerate(jugadores):
            self._hash_jugadores.insert(orden_rendimiento, jugador)
        return self._hash_jugadores

    def equipo_con_menor_rendimiento(self):
        equipos = self.obtener_equipos()
        equipos = self.ordenar_entidades(equipos, key='rendimiento_promedio')
        return equipos[0]

    def equipo_con_mayor_rendimiento(self):
        equipos = self.obtener_equipos()
        equipos = self.ordenar_entidades(equipos, key='rendimiento_promedio', reverse=True)
        return equipos[0]

    def jugador_con_mejor_rendimiento(self):
        jugadores = self.ranking_jugadores()
        return jugadores.search(jugadores.len() - 1)

    def jugador_con_peor_rendimiento(self):
        jugadores = self.ranking_jugadores()
        return jugadores.search(0)

    def jugador_mas_viejo(self):
        jugadores = self.obtener_jugadores()
        jugadores = self.ordenar_entidades(jugadores, key='edad', reverse=True)
        return jugadores[0]
    
    def jugador_mas_joven(self):
        jugadores = self.obtener_jugadores()
        jugadores = self.ordenar_entidades(jugadores, key='edad')
        return jugadores[0]

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

