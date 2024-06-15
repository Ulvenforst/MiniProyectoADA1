################################################################################
# Archivo: LinkedList.py                                                       #
# Autores: Julián Ernesto Puyo Mora 2226905                                    #
#          Laura Camila Betancourt Horta 2223435                               #
#          Jhoan Felipe León Correa 2228527                                    #
#          Juan Camilo Narváez Tascón 2140112                                  #
# Fecha de creación: 06/06/2024                                                #
# Fecha de última modificación: 06/06/2024                                     #
# Licencia: GNU-GPL                                                            #
################################################################################

# CLASE: LinkedList
# INTENCIÓN: Representar una lista enlazada.
# RELACIONES: Esta clase se relaciona con la clase Node; una lista enlazada tiene varios nodos.

from .Node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def find(self, key):
        """
        Busca un nodo en la lista enlazada.

        Args:
            key (any): Clave del nodo a buscar.

        Returns:
            Node: Nodo encontrado.
        """
        current = self.head
        while current:
            if current.key == key:
                return current
            current = current.next
        return None

    def insert(self, key, value):
        """
        Inserta un nodo en la lista enlazada.

        Args:
            key (any): Clave del nodo a insertar.
            value (any): Valor del nodo a insertar.
        """
        new_node = Node(key, value)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        """
        Elimina un nodo de la lista enlazada.

        Args:
            key (any): Clave del nodo a eliminar.

        Returns:
            bool: True si el nodo fue eliminado, False en caso contrario.
        """
        current = self.head
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False
