################################################################################
# Archivo: Asociacion.py                                                       #
# Autores: Julián Ernesto Puyo Mora 2226905                                    #
#          Laura Camila Betancourt Horta 2223435                               #
#          Jhoan Felipe León Correa 2228527                                    #
#          Juan Camilo Narváez Tascón 2140112                                  #
# Fecha de creación: 06/02/2024                                                #
# Fecha de última modificación: 06/02/2024                                     #
# Licencia: GNU-GPL                                                            #
################################################################################

# CLASE: Asociacion
# INTENCIÓN: Representar una asociación de deportes.
# RELACIONES: Esta clase se relaciona con la clase Sede; una asociación tiene varias sedes.

from ..data_structures.ArbolRojiNegro   import ArbolRojiNegro
from ..data_structures.Nodo             import Nodo
from .Jugador                           import Jugador

K = 10 # Número máximo de sedes permitidas en la asociación.

class Asociacion:
    def __init__(self):
        self._sedes = []
        self._arbol_sedes = ArbolRojiNegro()
        self._arbol_jugadores = ArbolRojiNegro()
        self._arbol_jugadores_edad = ArbolRojiNegro()

    def agregar_sedes(self, nueva_sede):
        """
        Agrega una nueva sede a la asociación.

        Args:
            nueva_sede (Sede): Sede a agregar.

        Returns:
            None
        """
        if len(self._sedes) + len(nueva_sede) > K:
            print(f"La sede {self._nombre} excederá el tamaño máximo permitido de Sedes.")
            return
        self._sedes.extend(nueva_sede)

        for sede in self._sedes:
            suma_rendimiento_equipos= 0
            for equipo in sede.equipos:
                suma_rendimiento_jugadores = 0
                for jugador in equipo.jugadores:
                    suma_rendimiento_jugadores += jugador.rendimiento
                    self._arbol_jugadores.insertar(Nodo(jugador, jugador.rendimiento, jugador.edad))
                    self._arbol_jugadores_edad.insertar(Nodo(jugador, jugador.edad, jugador.rendimiento))
                promedio_equipo = suma_rendimiento_jugadores / len(equipo.jugadores)
                suma_rendimiento_equipos+=promedio_equipo
            rendimiento_sede=suma_rendimiento_equipos/len(sede.equipos)

            self._arbol_sedes.insertar(Nodo(sede, rendimiento_sede, len(sede.equipos)))

    @staticmethod
    def resetear_datos():
        """
        Reinicia los datos de la asociación.

        Returns:
            None
        """
        Jugador._reset_contador()

    @property
    def ranking_sedes(self):
        """
        Retorna el ranking de sedes de la asociación.

        Args:
            None

        Returns:
            list: Lista de sedes ordenadas por rendimiento.
        """
        return self._arbol_sedes.in_orden()
    
    def ranking_jugadores(self):
        """
        Retorna el ranking de jugadores de la asociación.

        Args:
            None

        Returns:
            list: Lista de jugadores ordenados por rendimiento.
        """
        return self._arbol_jugadores.in_orden()
    
    def jugador_con_mejor_rendimiento(self):
        """
        Retorna el jugador con mejor rendimiento de la asociación.

        Args:
            None

        Returns:
            Jugador: Jugador con mejor rendimiento.
        """
        maximo = self._arbol_jugadores.maximo()
        return maximo

    def jugador_con_peor_rendimiento(self):
        """
        Retorna el jugador con peor rendimiento de la asociación.

        Args:
            None

        Returns:
            Jugador: Jugador con peor rendimiento.
        """
        minimo = self._arbol_jugadores.minimo()
        return minimo


    def equipo_con_mayor_rendimiento(self):
        """
        Retorna el equipo con mayor rendimiento de la asociación.

        Args:
            None

        Returns:
            Equipo: Equipo con mayor rendimiento.
        """
        maximo = self._sedes[0]._arbol_equipos.maximo()
        for sede in self._sedes:
            if maximo.dato < sede._arbol_equipos.maximo().dato:
               maximo=sede._arbol_equipos.maximo()
        return maximo

    def equipo_con_menor_rendimiento(self):
        """
        Retorna el equipo con menor rendimiento de la asociación.

        Args:
            None

        Returns:
            Equipo: Equipo con menor rendimiento.
        """
        minimo = self._sedes[0]._arbol_equipos.minimo()
        for sede in self._sedes:
            if minimo.dato > sede._arbol_equipos.minimo().dato:
               minimo=sede._arbol_equipos.minimo()
        return minimo
    
    def jugador_mas_viejo(self):
        """
        Retorna el jugador más viejo de la asociación.

        Args:
            None

        Returns:
            Jugador: Jugador más viejo.
        """
        maximo = self._sedes[0].equipos[0]._arbol_jugadores_edad.maximo()
        for sedes in self._sedes:
            for equipo in sedes.equipos:
                if maximo.dato < equipo._arbol_jugadores_edad.maximo().dato:
                   maximo=equipo._arbol_jugadores_edad.maximo()
        return maximo

    def jugador_mas_joven(self):
        """
        Retorna el jugador más joven de la asociación.

        Args:
            None

        Returns:
            Jugador: Jugador más joven.
        """
        minimo = self._sedes[0].equipos[0]._arbol_jugadores_edad.minimo()
        for sedes in self._sedes:
            for equipo in sedes.equipos:
                if minimo.dato > equipo._arbol_jugadores_edad.minimo().dato:
                   minimo=equipo._arbol_jugadores_edad.minimo()
        return minimo
         
    def promedio_rendimiento_jugadores(self):
        """
        Retorna el promedio de rendimiento de los jugadores de la asociación.

        Args:
            None

        Returns:
            float: Promedio de rendimiento de los jugadores.
        """
        longitud=0
        suma=0
        for sede in self._sedes:
            for equipo in sede.equipos:
                rendimientos=equipo._arbol_jugadores.in_values()
                suma+=sum(rendimientos)
                longitud+=len(rendimientos)
        promedio=suma/longitud
        return promedio

    def promedio_edad_jugadores(self):
        """
        Retorna el promedio de edad de los jugadores de la asociación.

        Args:
            None

        Returns:
            float: Promedio de edad de los jugadores.
        """
        longitud=0
        suma=0
        for sede in self._sedes:
            for equipo in sede.equipos:
                rendimientos=equipo._arbol_jugadores_edad.in_values()
                suma+=sum(rendimientos)
                longitud+=len(rendimientos)
        promedio=suma/longitud
        return promedio
                 
    @property
    def sedes(self):
        """
        Getter de sedes.

        Returns:
            list: Lista de sedes.
        """
        return self._sedes

