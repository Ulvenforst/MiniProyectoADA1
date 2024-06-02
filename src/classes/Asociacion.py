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

class Asociacion:
    def __init__(self):
        self._sedes = []

    def ranking_jugadores(self):
        """
        Retorna una lista con los identificadores de los jugadores de la asociación, ordenados por ranking.

        Returns:
            list: Lista con los identificadores de los jugadores de la asociación, ordenados por ranking.
        """
        jugadores = []
        for sede in self._sedes:
            for equipo in sede.equipos:
                jugadores.extend(equipo.jugadores)
        # Supongamos que el ranking es simplemente por identificador
        jugadores.sort(key=lambda jugador: jugador.identificador)  # Esto debe implementarse
        return [jugador.identificador for jugador in jugadores]

    @property
    def sedes(self):
        return self._sedes

