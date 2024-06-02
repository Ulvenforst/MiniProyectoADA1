################################################################################
# Archivo: Jugador.py                                                          #
# Autores: Julián Ernesto Puyo Mora 2226905                                    #
#          Laura Camila Betancourt Horta 2223435                               #
#          Jhoan Felipe León Correa 2228527                                    #
#          Juan Camilo Narváez Tascón 2140112                                  #
# Fecha de creación: 06/02/2024                                                #
# Fecha de última modificación: 06/02/2024                                     #
# Licencia: GNU-GPL                                                            #
################################################################################

# CLASE: Jugador
# INTENCIÓN: Representar un jugador de un equipo.
# RELACIONES: Esta clase no tiene relaciones con otras clases.

class Jugador:
    contador = 0  # Contador automático
    def __init__(self, nombre, edad, rendimiento):
        Jugador.contador += 1
        self._identificador = Jugador.contador
        self._nombre = nombre
        self._edad = edad
        self._rendimiento = rendimiento

    @property
    def identificador(self):
        return self._identificador

    @property
    def nombre(self):
        return self._nombre

    @property
    def edad(self):
        return self._edad

    @property
    def rendimiento(self):
        return self._rendimiento

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    @rendimiento.setter
    def rendimiento(self, rendimiento):
        self._rendimiento = rendimiento


