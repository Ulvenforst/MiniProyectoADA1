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
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        node = self.table[index].find(key)
        if node:
            node.value = value
        else:
            self.table[index].insert(key, value)

    def search(self, key):
        index = self.hash_function(key)
        node = self.table[index].find(key)
        return node.value if node else None

    def delete(self, key):
        index = self.hash_function(key)
        return self.table[index].delete(key)

    def __iter__(self):
        for linked_list in self.table:
            current = linked_list.head
            while current:
                yield current.key, current.value
                current = current.next

    def len(self):
        count = 0
        for linked_list in self.table:
            current = linked_list.head
            while current:
                count += 1
                current = current.next
        return count

    def __str__(self):
        result = ""
        for linked_list in self.table:
            current = linked_list.head
            while current:
                result += f"\t{current.value}\n"
                current = current.next
        return result

    
