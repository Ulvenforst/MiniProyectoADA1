################################################################################
# Archivo: Nodo.py                                                             #
# Autores: Julián Ernesto Puyo Mora 2226905                                    #
#          Laura Camila Betancourt Horta 2223435                               #
#          Jhoan Felipe León Correa 2228527                                    #
#          Juan Camilo Narváez Tascón 2140112                                  #
# Fecha de creación: 06/04/2024                                                #
# Fecha de última modificación: 06/04/2024                                     #
# Licencia: GNU-GPL                                                            #
################################################################################

# CLASE: Nodo
# INTENCIÓN: Representar un nodo de un arbol rojinegro.
# RELACIONES: No tiene.

class Nodo(object):
    def __init__(self, identificador, dato, factor_desempate):
        self.identificador = identificador
        self.dato = dato
        self.factor_desempate = factor_desempate
        self.color = 0
        self.izq = None
        self.der = None
        self.padre = None