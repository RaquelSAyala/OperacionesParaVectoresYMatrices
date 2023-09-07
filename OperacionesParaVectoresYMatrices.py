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

def prod_tensor(mat1,mat2):
    """producto tensor de dos matrices/vectores"""

    m = len(mat1)
    n = len(mat2)
    m1 = len(mat1[0])
    n1 = len(mat2[0])
    fila = m * n
    columna = n1 * m1

    matriz = [[0 for i in range(fila)] for columna in range(columna)]
    for j in range(fila):
        for k in range(columna):
            matriz[j][k] = (mat1[j // n][k // n] * mat2[j % n][k % n1])
    return matriz

# Casos de prueba para las funciones de operaciones con números complejos

# Vectores complejos
vec1 = [1+2j, 3-1j]
vec2 = [2-1j, 4+3j]

# Matrices complejas
mat1 = [[1+2j, 3-1j], [0+1j, -2-3j]]
mat2 = [[2-1j, 4+3j], [1-2j, 5+4j]]
mat3 = [[1+2j, 3-1j], [0+1j, -2-3j]]

# Pruebas para las funciones de operaciones con números complejos
print("Suma de vectores complejos:", sumar_vectores_complejos(vec1, vec2))
print("Inverso de vector complejo:", inverso_vector_complejo(vec1))
print("Multiplicación escalar de vector complejo:", multiplicar_escalar_vector_complejo(2+3j, vec1))

print("Suma de matrices complejas:\n", sumar_matrices_complejas(mat1, mat2))
print("Inversa de matriz compleja:\n", inversa_matriz_compleja(mat1))
print("Multiplicación escalar de matriz compleja:\n", multiplicar_escalar_matriz_compleja(2-1j, mat2))

print("Matriz transpuesta:\n", matriz_transpuesta(mat3))
print("Matriz conjugada:\n", matriz_conjugada(mat3))
print('producto tensor',prod_tensor([[1+2j, 3-1j], [0+1j, -2-3j]],[[2-1j, 4+3j], [1-2j, 5+4j]]))
