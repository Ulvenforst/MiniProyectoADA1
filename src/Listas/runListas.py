################################################################################
# Archivo: runListas.py                                                        #
# Autores: Julián Ernesto Puyo Mora 2226905                                    #
#          Laura Camila Betancourt Horta 2223435                               #
#          Jhoan Felipe León Correa 2228527                                    #
#          Juan Camilo Narváez Tascón 2140112                                  #
# Fecha de creación: 06/15/2024                                                #
# Fecha de última modificación: 06/15/2024                                     #
# Licencia: GNU-GPL                                                            #
################################################################################

# HISTORIA: Este archivo se encarga de ejecutar el programa con los casos de prueba
# haciendo uso de la estructura de datos de listas.

from pruebas import decorador_pruebas

@decorador_pruebas
def runListas(*args, **kwargs):
    asociacion = kwargs.get('asociacion')
    return "Resultados con Listas:"
