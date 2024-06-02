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

