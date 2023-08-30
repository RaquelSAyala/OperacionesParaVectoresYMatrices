# complex_operations.py
import numpy as np


def sumar_vectores_complejos(vec1, vec2):
    """
    Realiza la adición de dos vectores complejos.
    """
    return np.add(vec1, vec2)


def inverso_vector_complejo(vec):
    """
    Calcula el inverso aditivo de un vector complejo.
    """
    return np.negative(vec)


def multiplicar_escalar_vector_complejo(escalar, vec):
    """
    Realiza la multiplicación de un escalar por un vector complejo.
    """
    return np.multiply(escalar, vec)


def sumar_matrices_complejas(mat1, mat2):
    """
    Realiza la adición de dos matrices complejas.
    """
    return np.add(mat1, mat2)


def inversa_matriz_compleja(mat):
    """
    Calcula la inversa aditiva de una matriz compleja.
    """
    return np.negative(mat)


def multiplicar_escalar_matriz_compleja(escalar, mat):
    """
    Realiza la multiplicación de un escalar por una matriz compleja.
    """
    return np.multiply(escalar, mat)


def matriz_transpuesta(mat):
    """
    Calcula la transpuesta de una matriz o vector complejo.
    """
    return np.transpose(mat)


def matriz_conjugada(mat):
    """
    Calcula la matriz conjugada de una matriz o vector complejo.
    """
    return np.conjugate(mat)

# Casos de prueba para las funciones de operaciones con números complejos

# Vectores complejos
vec1 = [1+2j, 3-1j]
vec2 = [2-1j, 4+3j]

# Matrices complejas
mat1 = [[1+2j, 3-1j], [0+1j, -2-3j]]
mat2 = [[2-1j, 4+3j], [1-2j, 5+4j]]
mat3 = [[1+2j, 3-1j], [0+1j, -2-3j]]

# Pruebas para las funciones de operaciones con números complejos
print("Suma de vectores complejos:", add_complex_vectors(vec1, vec2))
print("Inverso de vector complejo:", inverse_complex_vector(vec1))
print("Multiplicación escalar de vector complejo:", scalar_multiply_complex_vector(2+3j, vec1))

print("Suma de matrices complejas:\n", add_complex_matrices(mat1, mat2))
print("Inversa de matriz compleja:\n", inverse_complex_matrix(mat1))
print("Multiplicación escalar de matriz compleja:\n", scalar_multiply_complex_matrix(2-1j, mat2))

print("Matriz transpuesta:\n", transpose_matrix(mat3))
print("Matriz conjugada:\n", conjugate_matrix(mat3))
