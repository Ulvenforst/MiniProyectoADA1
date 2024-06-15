################################################################################
# Archivo: TablaHash.py                                                        #
# Autores: Julián Ernesto Puyo Mora 2226905                                    #
#          Laura Camila Betancourt Horta 2223435                               #
#          Jhoan Felipe León Correa 2228527                                    #
#          Juan Camilo Narváez Tascón 2140112                                  #
# Fecha de creación: 06/05/2024                                                #
# Fecha de última modificación: 06/06/2024                                     #
# Licencia: GNU-GPL                                                            #
################################################################################

# CLASE: TablaHash
# INTENCIÓN: Representar una tabla hash.
# RELACIONES: Esta clase se relaciona con la clase LinkedList; una tabla hash tiene varias listas enlazadas.

from .LinkedList import LinkedList

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [LinkedList() for _ in range(size)]

    def hash_function(self, key):
        """
        Función hash que retorna el índice de la tabla hash donde se debe insertar o buscar un elemento.

        Args:
            key (any): Clave del elemento a insertar o buscar.

        Returns:
            int: Índice de la tabla hash.
        """
        return key % self.size

    def insert(self, key, value):
        """
        Inserta un elemento en la tabla hash.
        
        Args:
            key (any): Clave del elemento a insertar.
            value (any): Valor del elemento a insertar.

        Returns:
            None
        """
        index = self.hash_function(key)
        node = self.table[index].find(key)
        if node:
            node.value = value
        else:
            self.table[index].insert(key, value)

    def search(self, key):
        """
        Busca un elemento en la tabla hash.

        Args:
            key (any): Clave del elemento a buscar.

        Returns:
            any: Valor del elemento encontrado.
        """
        index = self.hash_function(key)
        node = self.table[index].find(key)
        return node.value if node else None

    def delete(self, key):
        """
        Elimina un elemento de la tabla hash.

        Args:
            key (any): Clave del elemento a eliminar.

        Returns:
            bool: True si el elemento fue eliminado, False en caso contrario.
        """
        index = self.hash_function(key)
        return self.table[index].delete(key)

    def len(self):
        """
        Retorna la cantidad de elementos en la tabla hash.

        Args:
            None

        Returns:
            int: Cantidad de elementos en la tabla hash.
        """
        count = 0
        for linked_list in self.table:
            current = linked_list.head
            while current:
                count += 1
                current = current.next
        return count

    # Método mágicos:
    def __str__(self):
        result = ""
        for linked_list in self.table:
            current = linked_list.head
            while current:
                result += f"\t{current.value}\n"
                current = current.next
        return result

    def __iter__(self):
        for linked_list in self.table:
            current = linked_list.head
            while current:
                yield current.key, current.value
                current = current.next
