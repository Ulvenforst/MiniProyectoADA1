################################################################################
# Archivo: pruebas.py                                                          #
# Autores: Julián Ernesto Puyo Mora 2226905                                    #
#          Laura Camila Betancourt Horta 2223435                               #
#          Jhoan Felipe León Correa 2228527                                    #
#          Juan Camilo Narváez Tascón 2140112                                  #
# Fecha de creación: 06/15/2024                                                #
# Fecha de última modificación: 06/16/2024                                     #
# Licencia: GNU-GPL                                                            #
################################################################################

# HISTORIA: Este archivo contiene el decorador que se encarga de ejecutar las pruebas
# de la aplicación y de medir el tiempo de ejecución de cada una de ellas. Estas
# pruebas se aplican sobre ambas estructuras de datos, y son las dadas por el profesor.

import time, random

def decorador_pruebas(func):
    def wrapper(*args, **kwargs):
        Asociacion = kwargs.get('Asociacion')
        Jugador = kwargs.get('Jugador')
        Equipo = kwargs.get('Equipo')
        Sede = kwargs.get('Sede')

        if not all([Asociacion, Jugador, Equipo, Sede]):
            raise ValueError("Faltan clases necesarias para configurar el entorno de pruebas")

        asociacion = Asociacion()

        tiempos_de_ejecucion = []

        # # Crear jugadores
        # jugadores = [
        #         Jugador("Sofia García", 21, 66), Jugador("Alejandro Torres", 27, 24),
        #         Jugador("Valentina Rodriguez", 19, 15), Jugador("Juan López", 22, 78),
        #         Jugador("Martina Martinez", 30, 55), Jugador("Sebastián Pérez", 25, 42),
        #         Jugador("Camila Fernández", 24, 36), Jugador("Mateo González", 29, 89),
        #         Jugador("Isabella Díaz", 21, 92), Jugador("Daniel Ruiz", 17, 57),
        #         Jugador("Luciana Sánchez", 18, 89), Jugador("Lucas Vásquez", 26, 82)
        # ]
        
        # # Crear equipos y sedes
        # futbolCali = Equipo("Futbol Cali")
        # futbolCali.agregar_jugadores([jugadores[9], jugadores[1]])
        # volleyballCali = Equipo("Volleyball Cali")
        # volleyballCali.agregar_jugadores([jugadores[0], jugadores[8], jugadores[11], jugadores[5]])

        # futbolMedellin = Equipo("Futbol Medellín")
        # futbolMedellin.agregar_jugadores([jugadores[10], jugadores[7], jugadores[6]])
        # volleyballMedellin = Equipo("Volleyball Medellín")
        # volleyballMedellin.agregar_jugadores([jugadores[2], jugadores[3], jugadores[4]])
        
        # sedeCali = Sede("Cali")
        # sedeCali.agregar_equipos([futbolCali, volleyballCali])
        # sedeMedellin = Sede("Medellín")
        # sedeMedellin.agregar_equipos([futbolMedellin, volleyballMedellin])

        # asociacion.agregar_sedes([sedeCali, sedeMedellin])
        # print("PRUEBAS PDF:")
        # print("-------------------")
        # print("Jugadores del equipo de futbol de Medellín:")
        # for jugador in futbolMedellin.ranking_jugadores: print(jugador)
        # print("-------------------")
        # print("Jugadores del equipo de volleyball de Medellín:")
        # for jugador in volleyballMedellin.ranking_jugadores: print(jugador)
        # print("-------------------")
        # print("Jugadores del equipo de futbol de Cali:")
        # for jugador in futbolCali.ranking_jugadores: print(jugador)
        # print("-------------------")
        # print("Jugadores del equipo de volleyball de Cali:")
        # for jugador in volleyballCali.ranking_jugadores: print(jugador)
        # print("-------------------")
        # print("Ranking de jugadores de la asociación:")
        # # for jugador in asociacion.ranking_jugadores(): print(jugador)
        # print("-------------------")
        # print("Equipo con mayor rendimiento promedio:")
        # print(asociacion.equipo_con_mayor_rendimiento())
        # print("-------------------")
        # print("Equipo con menor rendimiento promedio:")
        # print(asociacion.equipo_con_menor_rendimiento())
        # print("-------------------")
        # print("Jugador con mejor rendimiento:")
        # print(asociacion.jugador_con_mejor_rendimiento())
        # print("-------------------")
        # print("Jugador con peor rendimiento:")
        # print(asociacion.jugador_con_peor_rendimiento())
        # print("-------------------")
        # print("Jugador más joven:")
        # print(asociacion.jugador_mas_joven())
        # print("-------------------")
        # print("Jugador más viejo:")
        # print(asociacion.jugador_mas_viejo())
        # print("-------------------")
        # print("Promedio de edad de los jugadores:")
        # print(asociacion.promedio_edad_jugadores())
        # print("-------------------")
        # print("Promedio de rendimiento de los jugadores:")
        # print(asociacion.promedio_rendimiento_jugadores())

        print("PRUEBAS DE INPUT 1:")
        Asociacion.resetear_datos()
        inicio = time.perf_counter()
        j1 = Jugador("Juan", 20, 94)
        j2 = Jugador("Maria", 21, 94)
        j3 = Jugador("Pedro", 22, 21)
        j4 = Jugador("Ana", 23, 25)
        j5 = Jugador("Carlos", 24, 66)
        j6 = Jugador("Laura", 25, 52)
        j7 = Jugador("Jose", 26, 48)
        j8 = Jugador("Luis", 27, 73)
        j9 = Jugador("Sara", 28, 92)
        j10 = Jugador("Jorge", 29, 51)
        j11 = Jugador("Lorena", 30, 90)
        j12 = Jugador("Raul", 31, 100)
        
        e1 = Equipo("Futbol")
        e1.agregar_jugadores([j1, j2, j3])
        e2 = Equipo("Volleyball")
        e2.agregar_jugadores([j4, j5, j6])
        e3 = Equipo("Futbol")
        e3.agregar_jugadores([j7, j8, j9])
        e4 = Equipo("Volleyball")
        e4.agregar_jugadores([j10, j11, j12])
        
        s1 = Sede("Sede Cali")
        s1.agregar_equipos([e1, e2])
        s2 = Sede("Sede Medellin")
        s2.agregar_equipos([e3, e4])
        a1 = Asociacion()
        a1.agregar_sedes([s1, s2])
        imprimirDatos(a1)
        fin = time.perf_counter()
        tiempos_de_ejecucion.append(fin - inicio)

        print("\n")
        print("PRUEBAS DE INPUT 2:")
        Asociacion.resetear_datos()
        inicio = time.perf_counter()
        j1 = Jugador("Sofia Garcia", 21, 66)
        j2 = Jugador("Alejandro Torres", 27, 24)
        j3 = Jugador("Valentina Rodriguez", 19, 15)
        j4 = Jugador("Juan Lopez", 22, 78)
        j5 = Jugador("Martina Martinez", 30, 55)
        j6 = Jugador("Sebastian Perez", 25, 42)
        j7 = Jugador("Camila Fernandez", 24, 36)
        j8 = Jugador("Mateo Gonzalez", 29, 89)
        j9 = Jugador("Isabella Diaz", 40, 92)
        j10 = Jugador("Daniel Ruiz", 17, 57)
        j11 = Jugador("Luciana Sanchez", 18, 89)
        j12 = Jugador("Lucas Vasquez", 26, 82)
        j13 = Jugador("william hernandez", 30, 44)
        j14 = Jugador("Laura Perez", 20, 78)
        j15 = Jugador("Santiago Rodriguez", 23, 32)
        j16 = Jugador("Maria Gonzalez", 28, 65)
        j17 = Jugador("Carlos Lopez", 19, 72)
        j18 = Jugador("Valeria Martinez", 21, 45)
        j19 = Jugador("Andres Perez", 30, 78)
        j20 = Jugador("Sara Hernandez", 22, 56)
        
        e1 = Equipo("Futbol")
        e1.agregar_jugadores([j10, j2])
        e2 = Equipo("Volleyball")
        e2.agregar_jugadores([j1, j9, j12, j6])
        e3 = Equipo("Futbol")
        e3.agregar_jugadores([j11, j8, j7])
        e4 = Equipo("Volleyball")
        e4.agregar_jugadores([j3, j4, j5])
        e5 = Equipo("Basketball")
        e5.agregar_jugadores([j13, j14, j15, j16])
        e6 = Equipo("Basketball")
        e6.agregar_jugadores([j17, j18, j19, j20])
        
        s1 = Sede("Sede Cali")
        s1.agregar_equipos([e1, e2, e5])
        s2 = Sede("Sede Medellin")
        s2.agregar_equipos([e3, e4, e6])
        a1 = Asociacion()
        a1.agregar_sedes([s1, s2])
        imprimirDatos(a1)
        fin = time.perf_counter()
        tiempos_de_ejecucion.append(fin - inicio)

        print("\n")
        Asociacion.resetear_datos()
        print("PRUEBAS DE INPUT 3:")
        inicio = time.perf_counter()
        j1 = Jugador("Sofia Garcia", 21, 66)
        j2 = Jugador("Alejandro Torres", 27, 24)
        j3 = Jugador("Valentina Rodriguez", 19, 15)
        j4 = Jugador("Juan Lopez", 22, 78)
        j5 = Jugador("Martina Martinez", 30, 55)
        j6 = Jugador("Sebastian Perez", 25, 42)
        j7 = Jugador("Camila Fernandez", 24, 36)
        j8 = Jugador("Mateo Gonzalez", 29, 89)
        j9 = Jugador("Isabella Diaz", 40, 92)
        j10 = Jugador("Daniel Ruiz", 17, 57)
        j11 = Jugador("Luciana Sanchez", 18, 89)
        j12 = Jugador("Lucas Vasquez", 26, 82)
        j13 = Jugador("william hernandez", 30, 44)
        j14 = Jugador("Laura Perez", 20, 78)
        j15 = Jugador("Santiago Rodriguez", 23, 32)
        j16 = Jugador("Maria Gonzalez", 28, 65)
        j17 = Jugador("Carlos Lopez", 19, 72)
        j18 = Jugador("Valeria Martinez", 21, 45)
        j19 = Jugador("Andres Perez", 30, 78)
        j20 = Jugador("Sara Hernandez", 22, 56)
        j21 = Jugador("Diego Castro", 23, 67)
        j22 = Jugador("Gabriela Ramos", 24, 43)
        j23 = Jugador("Adrian Torres", 22, 15)
        j24 = Jugador("Natalia Gomez", 21, 39)
        j25 = Jugador("Ivan Vargas", 29, 84)
        j26 = Jugador("Fernanda Ortiz", 26, 33)
        j27 = Jugador("Pablo Ramirez", 27, 65)
        j28 = Jugador("Julia Sanchez", 28, 79)
        j29 = Jugador("Ricardo Ruiz", 30, 52)
        j30 = Jugador("Victoria Leon", 25, 59)
        j31 = Jugador("Emilio Molina", 19, 46)
        j32 = Jugador("Andrea Herrera", 20, 75)
        j33 = Jugador("Leonardo Delgado", 22, 54)
        j34 = Jugador("Rosa Moreno", 23, 68)
        j35 = Jugador("Oscar Gutierrez", 26, 60)
        j36 = Jugador("Daniela Romero", 24, 58)
        j37 = Jugador("Miguel Diaz", 21, 77)
        j38 = Jugador("Lucia Alvarez", 19, 49)
        j39 = Jugador("Rodrigo Martinez", 28, 63)
        j40 = Jugador("Elena Cruz", 27, 41)
        j41 = Jugador("Manuel Silva", 23, 61)
        j42 = Jugador("Paula Garcia", 28, 88)
        j43 = Jugador("Jorge Torres", 27, 47)
        j44 = Jugador("Carolina Ramirez", 25, 69)
        j45 = Jugador("Martin Fernandez", 21, 83)
        j46 = Jugador("Sofia Ruiz", 39, 34)
        j47 = Jugador("Antonio Vasquez", 28, 73)
        j48 = Jugador("Alicia Ortega", 26, 66)
        j49 = Jugador("Alberto Mendoza", 30, 66)
        j50 = Jugador("Patricia Guzman", 42, 37)
        j51 = Jugador("Eduardo Alvarez", 22, 78)
        j52 = Jugador("Teresa Morales", 29, 14)
        j53 = Jugador("Luis Gutierrez", 36, 57)
        j54 = Jugador("Veronica Castillo", 25, 45)
        j55 = Jugador("Raul Romero", 27, 88)
        j56 = Jugador("Carmen Martinez", 30, 84)
        j57 = Jugador("Marcos Soto", 32, 62)
        j58 = Jugador("Ana Campos", 29, 12)
        j59 = Jugador("Hector Peña", 28, 76)
        j60 = Jugador("Diana Herrera", 26, 11)
        
        e1 = Equipo("Futbol")
        e1.agregar_jugadores([j16, j2, j40, j49])
        e2 = Equipo("Volleyball")
        e2.agregar_jugadores([j17, j9 , j18, j26, j38, j50, j51])
        e3 = Equipo("Basketball")
        e3.agregar_jugadores([j1, j27, j39, j54])
        e10 = Equipo("Tenis")
        e10.agregar_jugadores([j10, j19, j33, j48])
        e11 = Equipo("Natacion")
        e11.agregar_jugadores([j15, j20, j37, j59])
        
        e4 = Equipo("Futbol")
        e4.agregar_jugadores([j25, j8, j32, j58])
        e5 = Equipo("Volleyball")
        e5.agregar_jugadores([j4, j21, j52])
        e6 = Equipo("Basketball")
        e6.agregar_jugadores([j11, j46, j53])
        e12 = Equipo("Tenis")
        e12.agregar_jugadores([j24, j12, j28, j57])
        e13 = Equipo("Natacion")
        e13.agregar_jugadores([j3, j36, j47])
        
        e7 = Equipo("Futbol")
        e7.agregar_jugadores([j7, j30, j42, j45])
        e8 = Equipo("Volleyball")
        e8.agregar_jugadores([j13, j31, j41])
        e9 = Equipo("Basketball")
        e9.agregar_jugadores([j60 ,j6, j22, j29])
        e14 = Equipo("Tenis")
        e14.agregar_jugadores([j14, j35, j43, j55])
        e15 = Equipo("Natacion")
        e15.agregar_jugadores([j23, j5, j34, j44, j56])
        
        s1 = Sede("Sede Cali")
        s1.agregar_equipos([e1, e2, e3, e10, e11])
        s2 = Sede("Sede Medellin")
        s2.agregar_equipos([e7, e8, e9, e14, e15])
        s3 = Sede("Sede Bogota")
        s3.agregar_equipos([e4, e5, e6, e12, e13])
        a1 = Asociacion()
        a1.agregar_sedes([s1, s2, s3])
        imprimirDatos(a1)
        fin = time.perf_counter()
        tiempos_de_ejecucion.append(fin - inicio)

        # Puebas de rendimiento aleatorias para analizar el comportamiento en el tiempo de ejecución.
        tiempos_de_ejecucion_r = []
        n_values = [100, 200, 300, 400, 500, 600, 700, 800, 800, 900, 1000]

        for n in n_values:
            print(f"PRUEBAS PARA n = {n}:")
            Asociacion.resetear_datos()
            inicio = time.perf_counter()

            jugadores = []
            for i in range(n):
                nombre = f"Jugador {i+1}"
                edad = random.randint(16, 60)
                rendimiento = random.randint(10, 100)
                jugador = Jugador(nombre, edad, rendimiento)
                jugadores.append(jugador)

            # Se generan 'n' equipos (asumiendo 2 deportes: futball and volleyball)
            equipos = []
            for i in range(int(n/3)):
                deporte = "Futbol" if i % 2 == 0 else "Volleyball"
                equipo = Equipo(deporte)
                equipo.agregar_jugadores(jugadores[i:i+3])  # Intenta asignar 3 jugadores por equipo. Probar con int(n/3).
                equipos.append(equipo)

            sedes = []
            for i in range(int(n/6)):
                nombre_sede = f"Sede {i+1}"
                sede = Sede(nombre_sede)
                sede.agregar_equipos(equipos[i:i+2])  # Intenta asignar 2 equipos por sede. Probar con int(n/6).
                sedes.append(sede)

            asociacion = Asociacion()
            asociacion.agregar_sedes(sedes)

            fin = time.perf_counter()
            tiempos_de_ejecucion_r.append(fin - inicio)

            resultado = func(*args, **kwargs, asociacion=asociacion)

        return {'resultado': resultado, 'tiempo_correctitud': tiempos_de_ejecucion, 'tiempo_rendimiento': tiempos_de_ejecucion_r}
    return wrapper

def imprimirDatos(asociacion):
    print("-------------------")
    for sede in asociacion.ranking_sedes:
        print("Sede: ", sede.nombre)
        for equipo in sede.ranking_equipos:
            print("\tEquipo: ", equipo)
            for jugador in equipo.ranking_jugadores:
                print(f"\t\t{jugador}")
        print("-------------------")
    print("Ranking de jugadores de la asociación:")
    for jugador in asociacion.ranking_jugadores():
         print(f"\t{jugador}")
    print("-------------------")
    print("Equipo con mayor rendimiento promedio:")
    print(f"\t{asociacion.equipo_con_mayor_rendimiento()} - {asociacion.ranking_sedes[-1].nombre } ")
    print("-------------------")
    print("Equipo con menor rendimiento promedio:")
    print(f"\t{asociacion.equipo_con_menor_rendimiento()} - {asociacion.ranking_sedes[0].nombre } ")
    print("-------------------")
    print("Jugador con mejor rendimiento:")
    print(f"\t{asociacion.jugador_con_mejor_rendimiento()}")
    print("-------------------")
    print("Jugador con peor rendimiento:")
    print(f"\t{asociacion.jugador_con_peor_rendimiento()}")
    print("-------------------")
    print("Jugador más joven:")
    print(f"\t{asociacion.jugador_mas_joven()}")
    print("-------------------")
    print("Jugador más viejo:")
    print(f"\t{asociacion.jugador_mas_viejo()}")
    print("-------------------")
    print("Promedio de edad de los jugadores:")
    print(f"\t{asociacion.promedio_edad_jugadores()}")
    print("-------------------")
    print("Promedio de rendimiento de los jugadores:")
    print(f"\t{asociacion.promedio_rendimiento_jugadores()}")
