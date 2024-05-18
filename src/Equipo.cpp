#include "Equipo.h"
#include <iostream>
#include <algorithm>

Equipo::Equipo(const std::string& deporte) : deporte(deporte) {}

void agregarJugadores(Equipo& equipo, const std::vector<Jugador>& nuevosJugadores) {
    const int N_min = 2;
    const int N_max = 4;

    if (equipo.jugadores.size() + nuevosJugadores.size() > N_max) {
        std::cerr << "El equipo " << equipo.deporte << " excederá el tamaño máximo permitido de jugadores.\n";
        return;
    }

    equipo.jugadores.insert(equipo.jugadores.end(), nuevosJugadores.begin(), nuevosJugadores.end());

    if (equipo.jugadores.size() < N_min) {
        std::cerr << "El equipo " << equipo.deporte << " no cumple con el tamaño mínimo requerido de jugadores.\n";
    }
}

void ordenarJugadoresPorRendimiento(Equipo& equipo) {
    std::sort(equipo.jugadores.begin(), equipo.jugadores.end(), [](const Jugador& a, const Jugador& b) {
        if (a.rendimiento == b.rendimiento) {
            return a.edad > b.edad; // Mayor edad primero si el rendimiento es igual
        }
        return a.rendimiento < b.rendimiento; // Rendimiento ascendente
    });
}

float rendimientoPromedio(const Equipo& equipo) {
    if (equipo.jugadores.empty()) return 0.0f;
    float suma = 0;
    for (const auto& jugador : equipo.jugadores) {
        suma += jugador.rendimiento;
    }
    return suma / equipo.jugadores.size();
}

