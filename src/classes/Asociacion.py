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

    def agregar_sedes(self, nuevas_sedes):
        if len(self._sedes) + len(nuevas_sedes) > K:
            print("La asociación excederá el tamaño máximo permitido de sedes.")
            return
        
        nuevas_sedes = bucket_sort(nuevas_sedes, key=lambda x: x.rendimiento_promedio)
        nuevas_sedes = counting_sort(nuevas_sedes, key=lambda x: x.numero_jugadores, reverse=True)

        for orden_rendimiento, sede in enumerate(nuevas_sedes):
            self._hash_sedes.insert(orden_rendimiento, sede)

    def ranking_jugadores(self):
        jugadores = []
        for sede in self._hash_sedes:
            for equipo in sede[1].equipos:
                for jugador in equipo[1].jugadores:
                    jugadores.append(jugador[1])

        jugadores = counting_sort(jugadores, key=lambda x: x.rendimiento)
        return jugadores

    @property
    def sedes(self):
        return self._hash_sedes

