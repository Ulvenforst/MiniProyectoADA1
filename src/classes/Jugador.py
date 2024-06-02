class Jugador:
    contador = 0  # Contador automático
    def __init__(self, nombre, edad, rendimiento):
        self.identificador = Jugador.contador + 1
        Jugador.contador += 1
        self.nombre = nombre
        self.edad = edad
        self.rendimiento = rendimiento
