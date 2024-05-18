#ifndef ALGORITMOS_ORDENAMIENTO_H
#define ALGORITMOS_ORDENAMIENTO_H

#include <vector>
#include <functional> // Para std::function

// Plantilla para merge_sort
template <typename T>
void mergeSort(std::vector<T>& vec, int left, int right, std::function<bool(const T&, const T&)> comp);

// Plantilla para merge
template <typename T>
void merge(std::vector<T>& vec, int left, int mid, int right, std::function<bool(const T&, const T&)> comp);

#include "AlgoritmosOrdenamiento.cpp" // Incluimos la implementación de las plantillas

#endif // ALGORITMOS_ORDENAMIENTO_H

