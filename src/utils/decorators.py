from utils.sorting_algorithms import bucket_sort, counting_sort

def extraer_y_ordenar(tipo_entidad, clave, reverse=False):
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
    def decorator(func):
        def wrapper(self, new_entities, *args, **kwargs):
            current_size = getattr(self, '_hash_' + entity_name).len()
            if current_size + len(new_entities) > max_size:
                print(f"El {entity_name} excederá el tamaño máximo permitido de {max_size}.")
                return

            for key, reverse in sort_keys:
                new_entities = bucket_sort(new_entities, key=lambda x: getattr(x, key)) if key == 'rendimiento_promedio' \
                    else counting_sort(new_entities, key=lambda x: getattr(x, key), reverse=reverse)

            hash_table = getattr(self, '_hash_' + entity_name)
            for index, entity in enumerate(new_entities):
                hash_table.insert(index, entity)

            return func(self, new_entities, *args, **kwargs)
        return wrapper
    return decorator

