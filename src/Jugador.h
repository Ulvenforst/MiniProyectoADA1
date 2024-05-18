#ifndef JUGADOR_H
#define JUGADOR_H

#include <string>

struct Jugador {
    static int contador;
    int identificador;
    std::string nombre;
    int edad;
    int rendimiento;

    Jugador(const std::string& nombre, int edad, int rendimiento);
};

#endif // JUGADOR_H
