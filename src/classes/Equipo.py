M = 2      # Número máximo de equipos por sede
K = 2      # Número máximo de sedes en la asociación
N_min = 2  # Número mínimo de jugadores por equipo
N_max = 4  # Número máximo de jugadores por equipo

class Equipo:
    def __init__(self, deporte):
        self.deporte = deporte
        self.jugadores = []

    def agregar_jugadores(self, nuevos_jugadores):
        if len(self.jugadores) + len(nuevos_jugadores) > N_max:
            print(f"El equipo {self.deporte} excederá el tamaño máximo permitido de jugadores.")
            return
        self.jugadores.extend(nuevos_jugadores)
        if len(self.jugadores) < N_min:
            print(f"El equipo {self.deporte} no cumple con el tamaño mínimo requerido de jugadores.")
