#ifndef SEDE_H
#define SEDE_H

#include <string>
#include <vector>
#include "Equipo.h"

struct Sede {
    std::string nombre;
    std::vector<Equipo> equipos;

    Sede(const std::string& nombre);
};

void ordenarEquiposPorRendimientoPromedio(Sede& sede);
float rendimientoPromedio(const Sede& sede);

#endif // SEDE_H

