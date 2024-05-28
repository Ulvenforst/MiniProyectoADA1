# MiniProyectoADA1
> La fecha de entrega límite es el 16 de junio de 2024 a las 23:59.

> Se debe entregar un informe `.pdf`, código fuente, y README.txt que describa los archivos entregados e instrucciones de ejecución.

> Archivo `PuyoBetancourthLeonNarvaez.zip`.

## Problema de la asociación de deportes
Una asociación de deportes desea realizar un análisis a fondo de su organización
deportiva, con la finalidad de definir cuáles equipos y jugadores se verán recompensados 
con más recursos para sus entrenamientos, además de cuáles equipos y jugadores requieren 
planes para mejorar su rendimiento. **Esta organización o `Asociacion` tiene $K$ `sedes` por todo el país,
cada `Sede` un `nombre` y $M$ `equipos` para diferentes deportes, a su vez `Equipo` tiene un `deporte` definido 
y está formado por una cantidad minima $N_{min}$ y máxima $N_{max}$ de `jugadores`**. **Cada `Jugador` tendrá un 
número como `identificador`, su `nombre`, `edad` y `rendimiento`**, este último 
tomará valores $i \in \mathbb{N} :1\leqslant i \leqslant 100$.

> [!NOTE]
> $K,M,N_{min},N_{max} \in \mathbb{N} \wedge N_{min} < N_{max}$

La `Asociacion` busca que los **`equipos` internamente estén ordenados ascendentemente 
teniendo en la cuenta el rendimiento de los `jugadores`, en caso de empate se 
colocará primero el `Jugador` de mayor edad**. También para cada `Sede`, se busca
que los `equipos` estén ordenados ascendentemente por su rendimiento promedio, el 
cual se define como la suma de los rendimientos de los `jugadores` del equipo sobre
la cantidad de `jugadores` del equipo 
$$\texttt{rendimiento} \\_ \texttt{promedio}=\frac{\Sigma_{i=1}^{N}\texttt{Jugador}_i\texttt{.rendimiento}}{N}$$
En caso de empate en el valor del rendimiento entre `equipos`, **se pondrá primero el `Equipo` que tiene mayor cantidad 
de `jugadores`**. Para las `sedes` se busca algo similar, se requiere ordenar las `sedes` de forma ascendente 
según el promedio de los rendimientos de todos los equipos de la respectiva `Sede`, en caso de que dos `sedes` 
tengan el mismo rendimiento promedio la `Sede` con mas `jugadores` se pondrá primero. Por último con el fin 
de saber el ranking de los jugadores para tomar decisiones respecto a esto, se requiere también generar la 
lista de todos los `jugadores` de todas las `sedes` **ordenados por su rendimiento ascendentemente**.

### Ejemplo del problema
> Este código lo hice de manera rápida con base en el ejemplo del pdf con ánimo de empezar a estructurar las clase, por ende puede ser cambiado cuando se inicie el proyecto.
```Python
# Constantes que definirás según tus necesidades
M = 2      # Número máximo de equipos por sede
K = 2      # Número máximo de sedes en la asociación
N_min = 2  # Número mínimo de jugadores por equipo
N_max = 4  # Número máximo de jugadores por equipo

class Jugador:
    contador = 0  # Contador automático
    def __init__(self, nombre, edad, rendimiento):
        self.identificador = Jugador.contador + 1
        Jugador.contador += 1
        self.nombre = nombre
        self.edad = edad
        self.rendimiento = rendimiento

class Equipo:
    def __init__(self, deporte):
        self.deporte = deporte
        self.jugadores = []

    def agregar_jugadores(self, nuevos_jugadores):
        if len(self.jugadores) + len(nuevos_jugadores) > N_max:
            print(f"El equipo {self.deporte} excederá el tamaño máximo permitido de jugadores.")
            return
        self.jugadores.extend(nuevos_jugadores)
        if len(self.jugadores) < N_min:
            print(f"El equipo {self.deporte} no cumple con el tamaño mínimo requerido de jugadores.")

class Sede:
    def __init__(self, nombre):
        self.nombre = nombre
        self.equipos = []

class Asociacion:
    def __init__(self):
        self.sedes = []
    def ranking_jugadores(self):
        jugadores = []
        for sede in self.sedes:
            for equipo in sede.equipos:
                jugadores.extend(equipo.jugadores)
        # Supongamos que el ranking es simplemente por identificador
        jugadores.sort(key=lambda jugador: jugador.identificador)  # Esto debe implementarse
        return [jugador.identificador for jugador in jugadores]

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
futbolCali = Equipo("Futbol")
futbolCali.agregar_jugadores([jugadores[9], jugadores[1]])
volleyballCali = Equipo("Volleyball")
volleyballCali.agregar_jugadores([jugadores[0], jugadores[8], jugadores[11], jugadores[5]])

futbolMedellin = Equipo("Futbol")
futbolMedellin.agregar_jugadores([jugadores[10], jugadores[7], jugadores[6]])
volleyballMedellin = Equipo("Volleyball")
volleyballMedellin.agregar_jugadores([jugadores[2], jugadores[3], jugadores[4]])

sedeCali = Sede("Cali")
sedeCali.equipos.extend([futbolCali, volleyballCali])
sedeMedellin = Sede("Medellín")
sedeMedellin.equipos.extend([futbolMedellin, volleyballMedellin])

asociacion.sedes.extend([sedeCali, sedeMedellin])
```
La salida de esta instancia debería ser:
```Python
Equipo& futbolMedellin = asociacion.sedes[1].equipos[0] #> {6, 7, 10}
Equipo& volleyballMedellin = asociacion.sedes[1].equipos[1] #> {2, 4, 3}

Equipo& futbolCali = asociacion.sedes[0].equipos[0] #> {5, 0, 11, 8}
Equipo& volleyballCali = asociacion.sedes[0].equipos[1] #> {1, 9}

# Si se supone un método en Asociacion para el ranking de jugadores:
asociacion.ranking_jugadores() #>{2, 1, 6, 5, 4, 9, 0, 3, 11, 7, 10, 8}
```
Además de esto la asosiación, también necesita obtener algunos datos como:
* Equipo con menor rendimiento.
* Jugador con mayor rendimiento.
* Jugador con menor rendimiento.
* Jugador más joven.
* Jugador más veterano.
* Promedio de edad de los jugadores.
* Promedio del rendimiento de los jugadores.

Para este ejemplo las respuestas serían:
* Equipo con mayor rendimiento: Futbol sede Medellin.
* Equipo con menor rendimiento: Futbol sede Cali.
* Jugador con mayor rendimiento: {9, Isabella Díaz, 92}
* Jugador con menor rendimiento: {3, Valentina Rodríguez, 15}
* Jugador más joven: {10, Daniel Ruiz, 17}
* Jugador más veterano: {5, Martina Martínez, 30}
* Promedio de edad de los jugadores: 23.25
* Promedio del rendimiento de los jugadores: 60.41

---

El gerente de la asociación ha escuchado que los estudiantes de Ingeniería de
Sistemas, especialmente del curso de ADA I, de la Universidad del Valle, son especialistas 
en resolver este tipo de problemas y en los menores tiempos posibles, 
y ha decidido contratarlos para resolver su problema.

## Trabajo a realizar
**Plantear 2 soluciones al problema planteado.**
> [!IMPORTANT]
>  Una solución se considera diferente a otra en la medida que utilice diferentes estructuras de datos para almacenar los datos, y por ende en algunos de los algoritmos para manipular los respectivos datos.

Para cada solución se debe:
1. Explicar de manera clara la idea de la solución al problema, qué estucturas de datos va a usar, qué métodos o algoritmos usaría, etc..
2. Si va a utilizar un algoritmo ya existente, debe especificarlo. Tanto para los algoritmos existentes como los propuestos en el proyecto, debe determinar su complejidad computacional teórica.
3. En caso de utilizar un algoritmo ya existente, como por ejemplo, *Merge Sort* o cualquier otro, **NO es permitido hacer uso de funciones en bibliotecas** (librerías) del lenguaje de programación, todos los algoritmos existentes (que se han visto en clase) que vaya a requerir para el proyecto debe escribirlos manualmente, y cerciorarse de que funcionan en la práctica igual que como están planteados en la teoría.
4. Set de distintas pruebas con diferentes tamaños y parámetros de entrada (mínimo 4 pruebas de 4 instancias del problema).
5. Adjuntar la solución al problema (junto con las instrucciones para ejecutar el código) en uno de los siguientes 3 lenguajes: java 🤮, C++ ❤️, python 🐍.
6. Realizar un informe con lo siguiente:
   * **Análisis de resultados**: deben haber comparaciones de la complejidad teórica estimada con la complejidad real del algoritmo en ejecución, comparaciones de tamaño de entrada *vs* tiempo de salida, esto se hace tomando tiempos de ejecución del algoritmo que soluciona el problema. También estas comparaciones deben ser presentadas por medio de gráficos (tamaño de entrada *vs* tiempo de salida), y también debe comparar los tiempos de salida de las distintas soluciones que presente, evidenciando que hay diferencias entre los tiempos de salida de las distintas soluciones que se plantea (que concuerda la mejora en la complejidad computacional teórica).
   * Conclusiones del proyecto.
