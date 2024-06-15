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
from ..classes.Sede                     import Sede

K=2

class Asociacion:
    def __init__(self):
        self._sedes = []
        self._arbol_sedes = ArbolRojiNegro()

    def agregar_sede(self, nueva_sede):
        if len(self._sedes) + len(nueva_sede) > K:
            print(f"La sede {self._nombre} excederá el tamaño máximo permitido de Sedes.")
            return
        self._sedes.extend(nueva_sede)

        for sede in self._sedes:
            suma_rendimiento_equipos= 0
            for equipo in sede.equipos:
                suma_rendimiento_jugadores = sum(jugador.rendimiento for jugador in equipo.jugadores)
                promedio_equipo = suma_rendimiento_jugadores / len(equipo.jugadores)
                suma_rendimiento_equipos+=promedio_equipo
            rendimiento_sede=suma_rendimiento_equipos/len(sede.equipos)
    
            self._arbol_sedes.insertar(Nodo(sede.nombre, rendimiento_sede, len(sede.equipos)))

    def ranking_sedes(self):
        print(self._arbol_sedes.in_orden())
    
    def jugador_mayor_rendimiento(self):
        maximo = self._sedes[0].equipos[0]._arbol_jugadores.maximo()
        for sedes in self._sedes:
            for equipo in sedes.equipos:
                if maximo.dato < equipo._arbol_jugadores.maximo().dato:
                   maximo=equipo._arbol_jugadores.maximo()
        return maximo

    def jugador_menor_rendimiento(self):
        minimo = self._sedes[0].equipos[0]._arbol_jugadores.minimo()
        for sedes in self._sedes:
            for equipo in sedes.equipos:
                if minimo.dato > equipo._arbol_jugadores.minimo().dato:
                   minimo=equipo._arbol_jugadores.minimo()
        return minimo

    def equipo_mayor_rendimiento(self):
        maximo = self._sedes[0]._arbol_equipos.maximo()
        for sede in self._sedes:
            if maximo.dato < sede._arbol_equipos.maximo().dato:
               maximo=sede._arbol_equipos.maximo()
        return maximo

    def equipo_menor_rendimiento(self):
        minimo = self._sedes[0]._arbol_equipos.minimo()
        for sede in self._sedes:
            if minimo.dato > sede._arbol_equipos.minimo().dato:
               minimo=sede._arbol_equipos.minimo()
        return minimo
    
    def jugador_mayor_edad(self):
        maximo = self._sedes[0].equipos[0]._arbol_jugadores_edad.maximo()
        for sedes in self._sedes:
            for equipo in sedes.equipos:
                if maximo.dato < equipo._arbol_jugadores_edad.maximo().dato:
                   maximo=equipo._arbol_jugadores_edad.maximo()
        return maximo

    def jugador_menor_edad(self):
        minimo = self._sedes[0].equipos[0]._arbol_jugadores_edad.minimo()
        for sedes in self._sedes:
            for equipo in sedes.equipos:
                if minimo.dato > equipo._arbol_jugadores_edad.minimo().dato:
                   minimo=equipo._arbol_jugadores_edad.minimo()
        return minimo
         
    def promedio_rendimiento(self):
        longitud=0
        suma=0
        for sede in self._sedes:
            for equipo in sede.equipos:
                rendimientos=equipo._arbol_jugadores.in_values()
                suma+=sum(rendimientos)
                longitud+=len(rendimientos)
        promedio=suma/longitud
        return promedio

    def promedio_edad(self):
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
        return self._sedes

