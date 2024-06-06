################################################################################
# Archivo: TablaHash.py                                                       #
# Autores: Julián Ernesto Puyo Mora 2226905                                    #
#          Laura Camila Betancourt Horta 2223435                               #
#          Jhoan Felipe León Correa 2228527                                    #
#          Juan Camilo Narváez Tascón 2140112                                  #
# Fecha de creación: 06/05/2024                                                #
# Fecha de última modificación: 06/05/2024                                     #
# Licencia: GNU-GPL                                                            #
################################################################################

# CLASE: TablaHash
# INTENCIÓN: Representar una asociación de deportes.
# RELACIONES: Esta clase se relaciona con la clase Sede; una asociación tiene varias sedes.


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [LinkedList() for _ in range(size)]

    def hash_function(self, key):
        return hash(key) % self.size

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


class LinkedList:
    def __init__(self):
        self.head = None

    def find(self, key):
        current = self.head
        while current:
            if current.key == key:
                return current
            current = current.next
        return None

    def insert(self, key, value):
        new_node = Node(key, value)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
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


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

if __name__ == "__main__":
    hash_table = HashTable(10)  # Crear una tabla hash de tamaño 10

    # Insertar valores
    hash_table.insert("apple", 10)
    hash_table.insert("banana", 20)
    hash_table.insert("cherry", 30)

    # Buscar valores
    print(hash_table.search("banana"))  # Salida: 20
    print(hash_table.search("apple"))   # Salida: 10

    # Eliminar un valor
    hash_table.delete("banana")
    print(hash_table.search("banana"))  # Salida: None
