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
