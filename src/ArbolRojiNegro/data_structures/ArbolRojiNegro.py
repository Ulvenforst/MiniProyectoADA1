################################################################################
# Archivo: ArbolRojiNegro.py                                                   #
# Autores: Julián Ernesto Puyo Mora 2226905                                    #
#          Laura Camila Betancourt Horta 2223435                               #
#          Jhoan Felipe León Correa 2228527                                    #
#          Juan Camilo Narváez Tascón 2140112                                  #
# Fecha de creación: 06/04/2024                                                #
# Fecha de última modificación: 06/04/2024                                     #
# Licencia: GNU-GPL                                                            #
################################################################################

# CLASE: ArbolRojiNegro
# INTENCIÓN: Representar un arbol rojinegro.
# RELACIONES: Esta clase se relaciona con la clase Nodo; un arbol rojinegro tiene varios nodos.

class ArbolRojiNegro(object):
    def __init__(self):
        self.raiz = None

    def rotar_izq(self, x):
        """
        Hace una rotación a la izquierda del nodo x en el árbol rojinegro.

        Args:
            x (Nodo): Nodo a rotar.

        Returns:
            None
        """
        y = x.der               # y es el hijo derecho de x
        x.der = y.izq           # el hijo derecho de x sera el hijo izquierdo de y
        if y.izq:               # comprobar si y.izq no es None
            y.izq.padre = x     # el padre del hijo izquierdo de y ahora sera x
        y.padre = x.padre       # el padre de y sera el padre de x
        if x.padre is None:     # si x es la raiz
            self.raiz = y       # y sera la nueva raiz
        elif x == x.padre.izq:  # si x es el hijo izquierdo
            x.padre.izq = y     # y sera el hijo izquierdo
        else:                   # si x es el hijo derecho
            x.padre.der = y     # y sera el hijo derecho
        y.izq = x               # x es el hijo izquierdo de y
        x.padre = y             # y es el padre de x

    def rotar_der(self, y):
        """
        Hace una rotación a la derecha del nodo y en el árbol rojinegro.

        Args:
            y (Nodo): Nodo a rotar.

        Returns:
            None
        """
        x = y.izq               
        y.izq = x.der           
        if x.der:               
            x.der.padre = y         
        x.padre = y.padre       
        if y.padre is None:     
            self.raiz = x         
        elif y == y.padre.izq:  
            y.padre.izq = x     
        else:                   
            y.padre.der = x     
        x.der = y               
        y.padre = x             

    def insertar(self, nodo):
        """
        Inserta un nodo en el árbol rojinegro y ajusta el árbol.

        Args:
            nodo (Nodo): Nodo a insertar.

        Returns:
            None
        """
        if self.raiz is None:
            self.raiz = nodo
            nodo.color = 1
            return

        y = None
        x = self.raiz
        while x is not None:
            y = x
            if nodo.dato < x.dato or (nodo.dato == x.dato and nodo.factor_desempate > x.factor_desempate):
                x = x.izq
            else:
                x = x.der
        nodo.padre = y
        if y is None:
            self.raiz = nodo
        elif nodo.dato < y.dato or (nodo.dato == y.dato and nodo.factor_desempate > y.factor_desempate):
            y.izq = nodo
        else:
            y.der = nodo

        # Ajustar el árbol
        nodo.color = 0
        while nodo != self.raiz and nodo.padre.color == 0:
            if nodo.padre == nodo.padre.padre.izq:
                y = nodo.padre.padre.der
                if y and y.color == 0:
                    nodo.padre.color = 1
                    y.color = 1
                    nodo.padre.padre.color = 0
                    nodo = nodo.padre.padre
                else:
                    if nodo == nodo.padre.der:
                        nodo = nodo.padre
                        self.rotar_izq(nodo)
                    nodo.padre.color = 1
                    nodo.padre.padre.color = 0
                    self.rotar_der(nodo.padre.padre)
            else:
                y = nodo.padre.padre.izq
                if y and y.color == 0:
                    nodo.padre.color = 1
                    y.color = 1
                    nodo.padre.padre.color = 0
                    nodo = nodo.padre.padre
                else:
                    if nodo == nodo.padre.izq:
                        nodo = nodo.padre
                        self.rotar_der(nodo)
                    nodo.padre.color = 1
                    nodo.padre.padre.color = 0
                    self.rotar_izq(nodo.padre.padre)

        self.raiz.color = 1

    def in_orden(self, nodo=None, resultado=None):
        """
        Realiza un recorrido inorden del árbol rojinegro.

        Args:
            nodo (Nodo): Nodo a partir del cual se realiza el recorrido.
            resultado (list): Lista con los nodos del árbol en orden.

        Returns:
            list: Lista con los nodos del árbol en orden.
        """
        if resultado is None:
            resultado = []
        if nodo is None:
            nodo = self.raiz

        if nodo is not None:
            if nodo.izq is not None:
                self.in_orden(nodo.izq, resultado)

            resultado.append(nodo)

            if nodo.der is not None:
                self.in_orden(nodo.der, resultado)

        return resultado
    
    def in_values(self, nodo=None, resultado=None):
        """
        Realiza un recorrido inorden del árbol rojinegro y retorna los valores de los nodos.

        Args:
            nodo (Nodo): Nodo a partir del cual se realiza el recorrido.
            resultado (list): Lista con los valores de los nodos del árbol en orden.

        Returns:
            list: Lista con los valores de los nodos del árbol en orden.
        """
        if resultado is None:
            resultado = []
        if nodo is None:
            nodo = self.raiz

        if nodo is not None:
            if nodo.izq is not None:
                self.in_values(nodo.izq, resultado)

            resultado.append(nodo.dato)

            if nodo.der is not None:
                self.in_values(nodo.der, resultado)

        return resultado
    
    def minimo(self):
        """
        Retorna el nodo con el valor mínimo del árbol rojinegro.

        Args:
            None

        Returns:
            Nodo: Nodo con el valor mínimo del árbol.
        """
        nodo_actual = self.raiz
        while nodo_actual.izq is not None:
            nodo_actual = nodo_actual.izq
        return nodo_actual    
    
    def maximo(self):
        """
        Retorna el nodo con el valor máximo del árbol rojinegro.

        Args:
            None

        Returns:
            Nodo: Nodo con el valor máximo del árbol.
        """
        nodo_actual = self.raiz
        while nodo_actual.der is not None:
            nodo_actual = nodo_actual.der
        return nodo_actual 
