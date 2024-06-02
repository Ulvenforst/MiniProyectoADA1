M = 2      # Número máximo de equipos por sede
K = 2      # Número máximo de sedes en la asociación
N_min = 2  # Número mínimo de jugadores por equipo
N_max = 4  # Número máximo de jugadores por equipo

class Equipo:
    def __init__(self, deporte):
        self._deporte = deporte
        self._jugadores = []

    def agregar_jugadores(self, nuevos_jugadores):
        if len(self._jugadores) + len(nuevos_jugadores) > N_max:
            print(f"El equipo {self._deporte} excederá el tamaño máximo permitido de jugadores.")
            return
        self._jugadores.extend(nuevos_jugadores)
        if len(self._jugadores) < N_min:
            print(f"El equipo {self._deporte} no cumple con el tamaño mínimo requerido de jugadores.")

    @property
    def deporte(self):
        return self._deporte

    @property
    def jugadores(self):
        return self._jugadores

    @deporte.setter
    def deporte(self, deporte):
        self._deporte = deporte

    @jugadores.setter
    def jugadores(self, jugadores):
        self._jugadores = jugadores
