#include "Asociacion.h"
#include "AlgoritmosOrdenamiento.h"

// Función auxiliar para calcular el rendimiento promedio de una sede
float rendimientoPromedio(const Sede& sede) {
    if (sede.equipos.empty()) return 0.0f;
    float suma = 0;
    int totalJugadores = 0;
    for (const auto& equipo : sede.equipos) {
        suma += rendimientoPromedio(equipo) * equipo.jugadores.size();
        totalJugadores += equipo.jugadores.size();
    }
    return suma / totalJugadores;
}

// Función de comparación para Sede
bool compareSedes(const Sede& a, const Sede& b) {
    float rendimientoA = rendimientoPromedio(a);
    float rendimientoB = rendimientoPromedio(b);
    if (rendimientoA == rendimientoB) {
        return a.equipos.size() > b.equipos.size(); // Más equipos primero si el rendimiento es igual
    }
    return rendimientoA < rendimientoB; // Rendimiento promedio ascendente
}

// Función de comparación para Jugador
bool compareJugadores(const Jugador& a, const Jugador& b) {
    if (a.rendimiento == b.rendimiento) {
        return a.edad > b.edad; // Mayor edad primero si el rendimiento es igual
    }
    return a.rendimiento < b.rendimiento; // Rendimiento ascendente
}

void agregarSede(Asociacion& asociacion, const Sede& sede) {
    asociacion.sedes.push_back(sede);
}

void ordenarSedesPorRendimientoPromedio(Asociacion& asociacion) {
    mergeSort(asociacion.sedes, 0, asociacion.sedes.size() - 1, compareSedes);
}

std::vector<Jugador> rankingJugadores(const Asociacion& asociacion) {
    std::vector<Jugador> todosJugadores;
    for (const auto& sede : asociacion.sedes) {
        for (const auto& equipo : sede.equipos) {
            todosJugadores.insert(todosJugadores.end(), equipo.jugadores.begin(), equipo.jugadores.end());
        }
    }
    mergeSort(todosJugadores, 0, todosJugadores.size() - 1, compareJugadores);
    return todosJugadores;
}


