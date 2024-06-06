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

M = 2      # Número máximo de equipos por sede

from classes.TablaHash import HashTable
from algorithms.counting_sort import counting_sort, bucket_sort

class Sede:
    def __init__(self, nombre):
        self._nombre = nombre
        self._equipos = []
        self._hash_equipos = HashTable(M)
        self._rendimiento_promedio = 0

    def agregar_equipos(self, nuevos_equipos):
        if len(self._equipos) + len(nuevos_equipos) > M:
            print(f"El equipo {self._deporte} excederá el tamaño máximo permitido de equipos.")
            return
        
        nuevos_equipos = counting_sort(nuevos_equipos, key=lambda x: x.numero_jugadores, reverse=True)
        nuevos_equipos = bucket_sort(nuevos_equipos, key=lambda x: x.rendimiento_promedio)

        for orden_rendimiento, equipo in enumerate(nuevos_equipos):
            self._hash_equipos.insert(orden_rendimiento, equipo)

        for equipo in self._hash_equipos:
            self._rendimiento_promedio += equipo[1].rendimiento_promedio

        self._rendimiento_promedio /= self._hash_equipos.len()

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
