#ifndef EQUIPO_H
#define EQUIPO_H

#include <string>
#include <vector>
#include "Jugador.h"

struct Equipo {
    std::string deporte;
    std::vector<Jugador> jugadores;

    Equipo(const std::string& deporte);
};

void agregarJugadores(Equipo& equipo, const std::vector<Jugador>& nuevosJugadores);
void ordenarJugadoresPorRendimiento(Equipo& equipo);
float rendimientoPromedio(const Equipo& equipo);

#endif // EQUIPO_H

