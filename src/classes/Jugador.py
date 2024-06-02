class Jugador:
    contador = 0  # Contador automático
    def __init__(self, nombre, edad, rendimiento):
        Jugador.contador += 1
        self._identificador = Jugador.contador
        self._nombre = nombre
        self._edad = edad
        self._rendimiento = rendimiento
