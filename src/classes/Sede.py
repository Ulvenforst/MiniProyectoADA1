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

class Sede:
    def __init__(self, nombre):
        self._nombre = nombre
        self._equipos = []

    @property
    def nombre(self):
        return self._nombre
    
    @property
    def equipos(self):
        return self._equipos

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @equipos.setter
    def equipos(self, equipos):
        self._equipos = equipos
