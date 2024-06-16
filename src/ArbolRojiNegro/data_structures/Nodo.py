################################################################################
# Archivo: Nodo.py                                                             #
# Autores: Julián Ernesto Puyo Mora 2226905                                    #
#          Laura Camila Betancourt Horta 2223435                               #
#          Jhoan Felipe León Correa 2228527                                    #
#          Juan Camilo Narváez Tascón 2140112                                  #
# Fecha de creación: 06/04/2024                                                #
# Fecha de última modificación: 06/15/2024                                     #
# Licencia: GNU-GPL                                                            #
################################################################################

# CLASE: Nodo
# INTENCIÓN: Representar un nodo de un arbol rojinegro.
# RELACIONES: No tiene.

class Nodo(object):
    def __init__(self, entidad, dato, factor_desempate):
        self.entidad = entidad
        self.dato = dato
        self.factor_desempate = factor_desempate
        self.color = 0
        self.izq = None
        self.der = None
        self.padre = None

    @property
    def ranking_equipos(self):
        """
        Getter para el ranking de equipos de la sede. Funciona como By-pass.

        Returns:
            list: Lista de equipos ordenados por rendimiento.
        """
        if self.entidad.ranking_equipos is None:
            return self.entidad
        else:
            return self.entidad.ranking_equipos

    @property
    def ranking_jugadores(self):
        """
        Getter para el ranking de jugadores de la sede. Funciona como By-pass.

        Returns:
            list: Lista de jugadores ordenados por rendimiento.
        """
        if self.entidad.ranking_jugadores is None:
            return self.entidad
        else:
            return self.entidad.ranking_jugadores

    @property
    def nombre(self):
        """
        Getter del atributo nombre.

        Returns:
            str: Nombre de la entidad.
        """
        if self.entidad.nombre is None:
            return self.entidad
        else:
            return self.entidad.nombre

    # Métodos mágicos
    def __str__(self):
        return f"{self.entidad}"
