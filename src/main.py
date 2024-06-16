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
import matplotlib.pyplot as plt
from Listas.runListas import runListas
from Listas.classes import Asociacion as ListaAsociacion, Jugador as ListaJugador, Equipo as ListaEquipo, Sede as ListaSede
from ArbolRojiNegro.runArboles import runArboles
from ArbolRojiNegro.classes import Asociacion as ArbolAsociacion, Jugador as ArbolJugador, Equipo as ArbolEquipo, Sede as ArbolSede

def graficar_tiempos(tiempoLista, tiempoArboles):
    tiemposLista = tiempoLista
    tiemposArboles = tiempoArboles

    x = range(len(tiemposLista))
    labels = [f'input{i+1}' for i in x]
    
    bar_width = 0.35
    x_lista = [i - bar_width/2 for i in x]
    x_arboles = [i + bar_width/2 for i in x]
    
    plt.figure(figsize=(10, 5))
    plt.bar(x_lista, tiemposLista, width=bar_width, color='#1f77b4', label='Tiempos Listas')
    plt.bar(x_arboles, tiemposArboles, width=bar_width, color='#ff7f0e', label='Tiempos Árboles') 
    plt.plot(x_lista, tiemposLista, 'o-', color='#aec7e8')
    plt.plot(x_arboles, tiemposArboles, 'o-', color='#fdae6b')
    plt.title('Comparación de Tiempos de Ejecución')
    plt.xlabel('Inputs de casos de prueba')
    plt.ylabel('Tiempo (s)')
    plt.xticks(x, labels)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    tiemposListaEjemplos = []
    tiemposListaRendimiento  = []
    tiemposArbolEjemplos  = []
    tiemposArbolRendimiento = []

    # === Ejecutar los algoritmos con los casos de prueba ===

    with open('resultados.txt', 'w') as f:
        original_stdout = sys.stdout
        sys.stdout = f
        print("""##################################################
# Archivo: resultados.txt                         
# Autores: Julián Ernesto Puyo Mora 2226905       
#          Laura Camila Betancourt Horta 2223435  
#          Jhoan Felipe León Correa 2228527       
#          Juan Camilo Narváez Tascón 2140112     
# Licencia: GNU-GPL                               
##################################################
              """)
        print("""========
 LISTAS:
========\n""")
        tiemposListaEjemplos = runListas(Asociacion=ListaAsociacion, Jugador=ListaJugador, Equipo=ListaEquipo, Sede=ListaSede)["tiempo_correctitud"]
        tiemposListaRendimiento = runListas(Asociacion=ListaAsociacion, Jugador=ListaJugador, Equipo=ListaEquipo, Sede=ListaSede)["tiempo_rendimiento"]
        print("""\n====================
 Árboles Rojinegros: 
====================\n""")
        tiemposArbolEjemplos = runArboles(Asociacion=ArbolAsociacion, Jugador=ArbolJugador, Equipo=ArbolEquipo, Sede=ArbolSede)["tiempo_correctitud"]
        tiemposArbolRendimiento = runArboles(Asociacion=ArbolAsociacion, Jugador=ArbolJugador, Equipo=ArbolEquipo, Sede=ArbolSede)["tiempo_rendimiento"]
        sys.stdout = original_stdout

    print("Los resultados se han guardado en 'resultados.txt'")

    # === Graficar los resultados ===
    graficar_tiempos(tiemposListaEjemplos, tiemposArbolEjemplos)
    graficar_tiempos(tiemposListaRendimiento, tiemposArbolRendimiento)

    print("Resultados con Listas:", tiemposListaRendimiento)
    print("Resultados con Arboles RojiNegros:", tiemposArbolRendimiento)
