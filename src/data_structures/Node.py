################################################################################
# Archivo: Node.py                                                             #
#          Jhoan Felipe León Correa 2228527                                    #
#          Juan Camilo Narváez Tascón 2140112                                  #
# Fecha de creación: 06/06/2024                                                #
# Fecha de última modificación: 06/06/2024                                     #
# Licencia: GNU-GPL                                                            #
################################################################################

# CLASE: Node
# INTENCIÓN: Representar un nodo de una lista enlazada.
# RELACIONES: Esta clase se relaciona con la clase LinkedList; un nodo pertenece a una lista enlazada.

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
