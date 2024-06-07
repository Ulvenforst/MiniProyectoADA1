################################################################################
# Archivo: Sede.py                                                             # 
# Autores: Julián Ernesto Puyo Mora 2226905                                    #
#          Laura Camila Betancourt Horta 2223435                               #
#          Jhoan Felipe León Correa 2228527                                    #
#          Juan Camilo Narváez Tascón 2140112                                  #
# Fecha de creación: 06/02/2024                                                #
# Fecha de última modificación: 06/07/2024                                     #
# Licencia: GNU-GPL                                                            #
################################################################################

# CLASE: Sede 
# INTENCIÓN: Representar una sede de la asociación de deportes.
# RELACIONES: Esta clase se relaciona con la clase Equipo; una sede tiene varios equipos.

from utils.decorators import manage_insertions

M = 2      # Número máximo de equipos por sede

class Sede:
    def __init__(self, nombre):
        self._nombre = nombre
        self._list_equipos = []
        self._rendimiento_promedio = 0
        self._numero_jugadores = 0

    @manage_insertions(M, [('rendimiento_promedio', False), ('numero_jugadores', True)], 'equipos')
    def agregar_equipos(self, nuevos_equipos):
        """
        Agrega equipos a la sede.

        Args:
            nuevos_equipos (list): Lista de equipos a agregar.

        Returns:
            None
        """
        self._rendimiento_promedio = sum(e.rendimiento_promedio for e in self._list_equipos) / len(self._list_equipos)

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
            HashTable: Tabla hash de equipos.
        """
        return self._list_equipos

    @property
    def rendimiento_promedio(self):
        """
        Getter del atributo rendimiento_promedio.

        Returns:
            float: Rendimiento promedio de los equipos de la sede.
        """
        return self._rendimiento_promedio
    
    @property
    def numero_jugadores(self):
        """
        Getter del atributo numero_jugadores.

        Returns:
            int: Número de jugadores de la sede.
        """
        return self._numero_jugadores

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @equipos.setter
    def equipos(self, equipos):
        self._list_equipos = equipos
