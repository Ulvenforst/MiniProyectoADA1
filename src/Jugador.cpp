#include "Jugador.h"

int Jugador::contador = 0;

Jugador::Jugador(const std::string& nombre, int edad, int rendimiento)
        : nombre(nombre), edad(edad), rendimiento(rendimiento) {
    identificador = ++contador;
}

