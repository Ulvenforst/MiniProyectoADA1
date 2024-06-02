class Asociacion:
    def __init__(self):
        self._sedes = []

    def ranking_jugadores(self):
        jugadores = []
        for sede in self._sedes:
            for equipo in sede.equipos:
                jugadores.extend(equipo.jugadores)
        # Supongamos que el ranking es simplemente por identificador
        jugadores.sort(key=lambda jugador: jugador.identificador)  # Esto debe implementarse
        return [jugador.identificador for jugador in jugadores]
