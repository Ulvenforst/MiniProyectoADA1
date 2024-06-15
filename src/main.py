################################################################################
# Archivo: main.py                                                             # 
# Autores: Julián Ernesto Puyo Mora 2226905                                    #
#          Laura Camila Betancourt Horta 2223435                               #
#          Jhoan Felipe León Correa 2228527                                    #
#          Juan Camilo Narváez Tascón 2140112                                  #
# Fecha de creación: 06/02/2024                                                #
# Fecha de última modificación: 06/15/2024                                     #
# Licencia: GNU-GPL                                                            #
################################################################################

# HISTORIA: Este programa está diseñado para la "Asociación de Deportes" que busca 
# optimizar el rendimiento y la distribución de recursos entre sus equipos y jugadores. 
# La asociación administra múltiples sedes a nivel nacional, cada una con varios 
# equipos deportivos. Los jugadores de estos equipos son evaluados en base a su 
# rendimiento y edad para organizar y optimizar los equipos dentro de cada sede. 
# El programa prioriza los jugadores y equipos con mejor rendimiento para la asignación 
# de recursos, mientras identifica aquellos que necesitan mejoras. Se implementan 
# algoritmos para clasificar sedes, equipos y jugadores de acuerdo a su rendimiento 
# y otros criterios. Se entrega con informe, código fuente y documentación detallada 
# sobre su ejecución y estructura de archivos.

import sys
from Listas.runListas import runListas
from Listas.classes import Asociacion as ListaAsociacion, Jugador as ListaJugador, Equipo as ListaEquipo, Sede as ListaSede
from ArbolRojiNegro.runArboles import runArboles
from ArbolRojiNegro.classes import Asociacion as ArbolAsociacion, Jugador as ArbolJugador, Equipo as ArbolEquipo, Sede as ArbolSede

if __name__ == "__main__":
    with open('resultados.txt', 'w') as f:
        original_stdout = sys.stdout
        sys.stdout = f

        print("~" * 50 + "\n")
        print("Resultados con Listas:")
        print("\n" + "~" * 50)
        runListas(Asociacion=ListaAsociacion, Jugador=ListaJugador, Equipo=ListaEquipo, Sede=ListaSede)
        print("\n\n" + "~" * 50)
        print("Resultados con Arboles RojiNegros:")
        print("\n" + "~" * 50)
        runArboles(Asociacion=ArbolAsociacion, Jugador=ArbolJugador, Equipo=ArbolEquipo, Sede=ArbolSede)
        sys.stdout = original_stdout

    print("Los resultados se han guardado en 'resultados.txt'")
