#include <iostream>
#include "Asociacion.h"

int main() {
    // Crear jugadores
    std::vector<Jugador> jugadores = {
        {"Sofia García", 21, 66}, {"Alejandro Torres", 27, 24}, {"Valentina Rodriguez", 19, 15},
        {"Juan López", 22, 78}, {"Martina Martinez", 30, 55}, {"Sebastián Pérez", 25, 42},
        {"Camila Fernández", 24, 36}, {"Mateo González", 29, 89}, {"Isabella Díaz", 21, 92},
        {"Daniel Ruiz", 17, 57}, {"Luciana Sánchez", 18, 89}, {"Lucas Vásquez", 26, 82}
    };

    // Crear equipos para la sede de Cali
    Equipo futbolCali("Futbol");
    agregarJugadores(futbolCali, {jugadores[9], jugadores[1]}); // IDs 10 y 2

    Equipo volleyballCali("Volleyball");
    agregarJugadores(volleyballCali, {jugadores[0], jugadores[8], jugadores[11], jugadores[5]}); // IDs 1, 9, 12 y 6

    // Crear equipos para la sede de Medellín
    Equipo futbolMedellin("Futbol");
    agregarJugadores(futbolMedellin, {jugadores[10], jugadores[7], jugadores[6]}); // IDs 11, 8 y 7

    Equipo volleyballMedellin("Volleyball");
    agregarJugadores(volleyballMedellin, {jugadores[2], jugadores[3], jugadores[4]}); // IDs 3, 4 y 5

    // Crear sedes
    Sede sedeCali("Cali");
    sedeCali.equipos.push_back(futbolCali);
    sedeCali.equipos.push_back(volleyballCali);

    Sede sedeMedellin("Medellín");
    sedeMedellin.equipos.push_back(futbolMedellin);
    sedeMedellin.equipos.push_back(volleyballMedellin);

    // Crear la asociación y agregar las sedes
    Asociacion asociacion;
    agregarSede(asociacion, sedeCali);
    agregarSede(asociacion, sedeMedellin);

    // Ordenar equipos dentro de las sedes
    for (auto& sede : asociacion.sedes) {
        for (auto& equipo : sede.equipos) {
            ordenarJugadoresPorRendimiento(equipo);
        }
        ordenarEquiposPorRendimientoPromedio(sede);
    }

    // Ordenar las sedes
    ordenarSedesPorRendimientoPromedio(asociacion);

    // Obtener y mostrar el ranking de jugadores
    std::vector<Jugador> ranking = rankingJugadores(asociacion);
    std::cout << "Ranking de jugadores: {";
    for (size_t i = 0; i < ranking.size(); ++i) {
        std::cout << ranking[i].identificador;
        if (i < ranking.size() - 1) {
            std::cout << ", ";
        }
    }
    std::cout << "}" << std::endl;

    return 0;
}

