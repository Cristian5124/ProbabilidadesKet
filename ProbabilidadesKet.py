import numpy as np

# Función para calcular la probabilidad de encontrar el sistema en una posición en particular
def probabilidad(posicion, ket):
    norma = np.linalg.norm(ket)
    probabilidad = abs(ket[posicion])**2 / norma**2
    return probabilidad

# Función para encontrar la probabilidad de transitar del primer vector ket al segundo
def probtransicion(ket1, ket2):
    conjug = np.conj(ket1)
    norma = np.linalg.norm(np.dot(conjug, ket2))
    probabilidad_transicion = abs(np.dot(conjug, ket2))**2 / norma**2
    return probabilidad_transicion

# Ejemplo de uso
posiciones = 4
ket1 = np.array([-3-1j,-2j,1j,2])  # Ejemplo de vector ket

# Calculo de la probabilidad de encontrar el sistema en la posición 2
probposicion = probabilidad(2, ket1)
print("La probabilidad de encontrar el sistema en la posición 2 es:", probposicion*100,"%")
print("")

# Probabilidad de transitar del vector ket 1 a otro vector ket 2
ket2 = np.array([1-3j,2j,0,1-1j])
probtransicion = probtransicion(ket1, ket2)
print("La probabilidad de transitar del vector ket1 al vector ket2 es de:", probtransicion*100,"%")
print("")

# Matriz que describe un observable y un vector ket
def media_varianza(matriz, ket1):

    # Verifica si la matriz es hermitiana
    if not np.allclose(matriz, np.conj(matriz.T)):
        print("La matriz no es hermitiana.")
        return None

    # Calculo de la media
    media = np.dot(np.conj(ket1), np.dot(matriz, ket1)).real
    print("La media del observable en el estado dado es de:", media)
    print("")

    # Calculo de la varianza
    varianza = np.dot(np.conj(ket1), np.dot(matriz**2, ket1)).real - media**2
    print("La varianza del observable en el estado dado es de:", varianza)
    print("")

# Ejemplo
matriz = np.random.rand(4, 4) + 1j * np.random.rand(4, 4)
matriz = matriz + matriz.conj().T
media_varianza(matriz, ket1)

# Valores propios y probabilidades
def valprop_probs(matriz, ket1):

    # Verifica si la matriz es hermitiana
    if not np.allclose(matriz, np.conj(matriz.T)):
        print("La matriz no es hermitiana.")
        return None

    # Calculo de los valores propios y vectores propios de la matriz
    valprop, vectprop = np.linalg.eig(matriz)
    print("Los valores propios de la matriz son:\n\n", valprop)
    print("")
    print("Los vectores propios de la matriz son:\n\n", vectprop)
    print("")

    # Calcula la probabilidad de transitar a cada uno de los vectores propios después de la observación
    '''ket1 = np.array([-3-1j,-2j,1j,2])
    probabilidades = []
    for i in range(len(ket1)):
        probabilidad = probtransicion(ket1, vectprop[:,i])
        probabilidades.append(probabilidad)
    print("La probabilidad de transitar a cada uno de los vectores propios después de la observación es de:", probabilidades)'''

# Ejemplo
valprop_probs(matriz,ket1)


