def decorador_pruebas(func):
    def wrapper(*args, **kwargs):
        Asociacion = kwargs.get('Asociacion')
        Jugador = kwargs.get('Jugador')
        Equipo = kwargs.get('Equipo')
        Sede = kwargs.get('Sede')

        # Asegurarse de que todas las clases necesarias están proporcionadas
        if not all([Asociacion, Jugador, Equipo, Sede]):
            raise ValueError("Faltan clases necesarias para configurar el entorno de pruebas")

        # Configuración de la asociación y jugadores
        asociacion = Asociacion()

        # Crear jugadores
        jugadores = [
                Jugador("Sofia García", 21, 66), Jugador("Alejandro Torres", 27, 24),
                Jugador("Valentina Rodriguez", 19, 15), Jugador("Juan López", 22, 78),
                Jugador("Martina Martinez", 30, 55), Jugador("Sebastián Pérez", 25, 42),
                Jugador("Camila Fernández", 24, 36), Jugador("Mateo González", 29, 89),
                Jugador("Isabella Díaz", 21, 92), Jugador("Daniel Ruiz", 17, 57),
                Jugador("Luciana Sánchez", 18, 89), Jugador("Lucas Vásquez", 26, 82)
        ]
        
        # Crear equipos y sedes
        futbolCali = Equipo("Futbol Cali")
        futbolCali.agregar_jugadores([jugadores[9], jugadores[1]])
        volleyballCali = Equipo("Volleyball Cali")
        volleyballCali.agregar_jugadores([jugadores[0], jugadores[8], jugadores[11], jugadores[5]])

        futbolMedellin = Equipo("Futbol Medellín")
        futbolMedellin.agregar_jugadores([jugadores[10], jugadores[7], jugadores[6]])
        volleyballMedellin = Equipo("Volleyball Medellín")
        volleyballMedellin.agregar_jugadores([jugadores[2], jugadores[3], jugadores[4]])
        
        sedeCali = Sede("Cali")
        sedeCali.agregar_equipos([futbolCali, volleyballCali])
        sedeMedellin = Sede("Medellín")
        sedeMedellin.agregar_equipos([futbolMedellin, volleyballMedellin])

        asociacion.agregar_sedes([sedeCali, sedeMedellin])
        
        print("-------------------")
        print("Jugadores del equipo de futbol de Medellín:")
        for jugador in futbolMedellin.ranking_jugadores: print(jugador)
        print("-------------------")
        print("Jugadores del equipo de volleyball de Medellín:")
        for jugador in volleyballMedellin.ranking_jugadores: print(jugador)
        print("-------------------")
        print("Jugadores del equipo de futbol de Cali:")
        for jugador in futbolCali.ranking_jugadores: print(jugador)
        print("-------------------")
        print("Jugadores del equipo de volleyball de Cali:")
        for jugador in volleyballCali.ranking_jugadores: print(jugador)
        print("-------------------")
        # print("Ranking de jugadores de la asociación:")
        # for jugador in asociacion.ranking_jugadores(): print(jugador)
        print("-------------------")
        print("Equipo con mayor rendimiento promedio:")
        print(asociacion.equipo_con_mayor_rendimiento())
        print("-------------------")
        print("Equipo con menor rendimiento promedio:")
        print(asociacion.equipo_con_menor_rendimiento())
        print("-------------------")
        print("Jugador con mejor rendimiento:")
        print(asociacion.jugador_con_mejor_rendimiento())
        print("-------------------")
        print("Jugador con peor rendimiento:")
        print(asociacion.jugador_con_peor_rendimiento())
        print("-------------------")
        print("Jugador más joven:")
        print(asociacion.jugador_mas_joven())
        print("-------------------")
        print("Jugador más viejo:")
        print(asociacion.jugador_mas_viejo())
        print("-------------------")
        print("Promedio de edad de los jugadores:")
        print(asociacion.promedio_edad_jugadores())
        print("-------------------")
        print("Promedio de rendimiento de los jugadores:")
        print(asociacion.promedio_rendimiento_jugadores())
        
        return func(*args, **kwargs, asociacion=asociacion)
    return wrapper

