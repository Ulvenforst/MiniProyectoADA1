#include "Sede.h"
#include <algorithm>

Sede::Sede(const std::string& nombre) : nombre(nombre) {}

void ordenarEquiposPorRendimientoPromedio(Sede& sede) {
    std::sort(sede.equipos.begin(), sede.equipos.end(), [](const Equipo& a, const Equipo& b) {
        float rendimientoA = rendimientoPromedio(a);
        float rendimientoB = rendimientoPromedio(b);
        if (rendimientoA == rendimientoB) {
            return a.jugadores.size() > b.jugadores.size(); // Más jugadores primero si el rendimiento es igual
        }
        return rendimientoA < rendimientoB; // Rendimiento promedio ascendente
    });
}

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

