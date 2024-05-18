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
```C++
#include <iostream>
#include <string>
#include <vector>

// Constantes que definirás según tus necesidades
#define M 2      // Número máximo de equipos por sede
#define K 2      // Número máximo de sedes en la asociación
#define N_min 2  // Número mínimo de jugadores por equipo
#define N_max 4  // Número máximo de jugadores por equipo

struct Jugador {
    static int contador; // Contador automático
    int identificador;
    std::string nombre;
    int edad;
    int rendimiento;

    // Constructor que asigna un identificador automáticamente
    Jugador(const std::string& nombre, int edad, int rendimiento)
        : nombre(nombre), edad(edad), rendimiento(rendimiento) {
        identificador = ++contador;
    }
};

// Inicialización del contador de identificadores
int Jugador::contador = 0;

struct Equipo {
    std::string deporte;
    std::vector<Jugador> jugadores;

    // Constructor
    Equipo(const std::string& deporte) : deporte(deporte) {}

    // Método para agregar un grupo de jugadores y validar el tamaño
    void agregarJugadores(const std::vector<Jugador>& nuevosJugadores) {
        if (jugadores.size() + nuevosJugadores.size() > N_max) {
            std::cerr << "El equipo " << deporte << " excederá el tamaño máximo permitido de jugadores.\n";
            return;
        }

        jugadores.insert(jugadores.end(), nuevosJugadores.begin(), nuevosJugadores.end());

        if (jugadores.size() < N_min) {
            std::cerr << "El equipo " << deporte << " no cumple con el tamaño mínimo requerido de jugadores.\n";
        }
    }
};

struct Sede {
    std::string nombre;
    std::vector<Equipo> equipos;

    // Constructor
    Sede(const std::string& nombre) : nombre(nombre) {}
};

struct Asociacion {
    std::vector<Sede> sedes;
};

int main() {
    // Crear jugadores {<nombre>,<edad>,<rendimiento>}
    std::vector<Jugador> jugadores = {
        {"Sofia García", 21, 66}, {"Alejandro Torres", 27, 24}, {"Valentina Rodriguez", 19, 15},
        {"Juan López", 22, 78}, {"Martina Martinez", 30, 55}, {"Sebastián Pérez", 25, 42},
        {"Camila Fernández", 24, 36}, {"Mateo González", 29, 89}, {"Isabella Díaz", 21, 92},
        {"Daniel Ruiz", 17, 57}, {"Luciana Sánchez", 18, 89}, {"Lucas Vásquez", 26, 82}
    };

    // Crear equipos para la sede de Cali
    Equipo futbolCali("Futbol");
    futbolCali.agregarJugadores({jugadores[9], jugadores[1]}); // IDs 10 y 2

    Equipo volleyballCali("Volleyball");
    volleyballCali.agregarJugadores({jugadores[0], jugadores[8], jugadores[11], jugadores[5]}); // IDs 1, 9, 12 y 6

    // Crear equipos para la sede de Medellín
    Equipo futbolMedellin("Futbol");
    futbolMedellin.agregarJugadores({jugadores[10], jugadores[7], jugadores[6]}); // IDs 11, 8 y 7

    Equipo volleyballMedellin("Volleyball");
    volleyballMedellin.agregarJugadores({jugadores[2], jugadores[3], jugadores[4]}); // IDs 3, 4 y 5

    // Crear sedes
    Sede sedeCali("Cali");
    sedeCali.equipos.push_back(futbolCali);
    sedeCali.equipos.push_back(volleyballCali);

    Sede sedeMedellin("Medellín");
    sedeMedellin.equipos.push_back(futbolMedellin);
    sedeMedellin.equipos.push_back(volleyballMedellin);

    // Crear la asociación y agregar las sedes
    Asociacion asociacion;
    asociacion.sedes.push_back(sedeCali);
    asociacion.sedes.push_back(sedeMedellin);

    return 0;
}

```
La salida de esta instancia debería ser:
```C++
Equipo& futbolMedellin = asociacion.sedes[1].equipos[0] //> {7, 8, 11}
Equipo& volleyballMedellin = asociacion.sedes[1].equipos[1] //> {3, 5, 4}

Equipo& futbolCali = asociacion.sedes[0].equipos[0] //> {6,1,12,9}
Equipo& volleyballCali = asociacion.sedes[0].equipos[1] //> {2,10}

// Si se supone un método en Asociacion para el ranking de jugadores:
asociacion.ranking_jugadores() //>{3, 2, 7, 6, 5, 10, 1, 4, 12, 8, 11, 9}
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
