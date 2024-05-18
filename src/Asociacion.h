#ifndef ASOCIACION_H
#define ASOCIACION_H

#include <vector>
#include "Sede.h"

struct Asociacion {
    std::vector<Sede> sedes;
};

void agregarSede(Asociacion& asociacion, const Sede& sede);
void ordenarSedesPorRendimientoPromedio(Asociacion& asociacion);
std::vector<Jugador> rankingJugadores(const Asociacion& asociacion);
Equipo equipoMenorRendimiento(const Asociacion& asociacion);
Jugador jugadorMayorRendimiento(const Asociacion& asociacion);
Jugador jugadorMenorRendimiento(const Asociacion& asociacion);
Jugador jugadorMasJoven(const Asociacion& asociacion);
Jugador jugadorMasVeterano(const Asociacion& asociacion);
float promedioEdadJugadores(const Asociacion& asociacion);
float promedioRendimientoJugadores(const Asociacion& asociacion);

#endif // ASOCIACION_H
