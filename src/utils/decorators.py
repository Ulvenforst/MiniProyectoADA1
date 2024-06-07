################################################################################
# Archivo: decorators.py                                                       # 
# Autores: Julián Ernesto Puyo Mora 2226905                                    #
#          Laura Camila Betancourt Horta 2223435                               #
#          Jhoan Felipe León Correa 2228527                                    #
#          Juan Camilo Narváez Tascón 2140112                                  #
# Fecha de creación: 06/06/2024                                                #
# Fecha de última modificación: 06/06/2024                                     #
# Licencia: GNU-GPL                                                            #
################################################################################

# HISTORIA: Este módulo contiene los decoradores que se utilizan en la clases para
# gestionar la inserción de entidades en las tablas hash y ordenarlas según criterios
# específicos.

from utils.sorting_algorithms import bucket_sort, counting_sort

def extraer_y_ordenar(tipo_entidad, clave, reverse=False):
    """
    Decorador que extrae las entidades de la asociación y las ordena según la clave especificada.

    Args:
        tipo_entidad (str): Tipo de entidad a extraer y ordenar.
        clave (str): Clave por la que se ordenarán las entidades.
        reverse (bool, optional): Si se ordenarán de forma ascendente o descendente. Por defecto es False.

    Returns:
        function: Función decorada.
    """
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            if tipo_entidad == 'jugadores':
                entidades = self.obtener_jugadores()
            elif tipo_entidad == 'equipos':
                entidades = self.obtener_equipos()
            entidades_ordenadas = self.ordenar_entidades(entidades, key=clave, reverse=reverse)
            return func(self, entidades_ordenadas, *args, **kwargs)
        return wrapper
    return decorator

def manage_insertions(max_size, sort_keys, entity_name):
    """
    Decorador que gestiona la inserción de entidades en las tablas hash y las ordena según criterios específicos.

    Args:
        max_size (int): Tamaño máximo permitido para la tabla hash.
        sort_keys (list): Lista de tuplas con las claves por las que se ordenarán las entidades.
        entity_name (str): Nombre de la entidad a gestionar.

    Returns:
        function: Función decorada.
    """
    def decorator(func):
        def wrapper(self, new_entities, *args, **kwargs):
            current_list = getattr(self, '_list_' + entity_name)  # Cambiado de hash a list
            if len(current_list) + len(new_entities) > max_size:
                print(f"El {entity_name} excederá el tamaño máximo permitido de {max_size}.")
                return

            for key, reverse in sort_keys:
                new_entities = bucket_sort(new_entities, key=lambda x: getattr(x, key)) if key == 'rendimiento_promedio' \
                    else counting_sort(new_entities, key=lambda x: getattr(x, key), reverse=reverse)

            current_list.extend(new_entities) 

            return func(self, new_entities, *args, **kwargs)
        return wrapper
    return decorator

