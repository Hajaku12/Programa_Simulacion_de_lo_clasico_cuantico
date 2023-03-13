import complex_library as lc
import numpy as np
import matplotlib.pyplot as plt
import complex_vector as vc
from tkinter import messagebox


def graficaCuantica(v, clics):
    print('Vector estado final:', v)
    labels = []
    state = []
    for i in range(len(v)):
        labels.append('Pto.' + str(i))
        state.append(lc.modulo(v[i][0]) ** 2)

    ind = np.arange(len(labels))
    plt.bar(ind, state)
    plt.xlabel('state')
    plt.ylabel('Value')
    plt.xticks(ind, labels, rotation=45)
    plt.title('dynamic evolution of the system after' + str(clics) + 'time clics')
    plt.show()


def grafica(v, clics):
    print('Final state vector', v)
    labels = []
    state = []
    for i in range(len(v)):
        labels.append('Pto.' + str(i))
        state.append(v[i][0][0])

    ind = np.arange(len(labels))
    plt.bar(ind, state)
    plt.xlabel('State')
    plt.ylabel('Value')
    plt.xticks(ind, labels, rotation=45)
    plt.title('dynamic evolution of the system after ' + str(clics) + 'time clics')
    plt.show()


def proceso(v, m, clics):
    if clics == 0:
        return v
    elif clics == 1:
        return vc.productoMatrices(m, v)
    else:
        return vc.productoMatrices(m, proceso(v, m, clics - 1))


def main():
    vector = [[[5, 4]],
              [[2, 1]],
              [[0, 2]],
              [[0, 0]],
              [[1, 1]],
              [[12, 11]]
              ]
    matriz = [[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
              [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
              [[0, 0], [1, 0], [0, 0], [0, 0], [0, 0], [1, 0]],
              [[0, 0], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0]],
              [[0, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0]],
              [[1, 0], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0]],
              ]
    for i in range(int(input("Enter the numbers of clics:")) + 1):
        grafica(proceso(vector, matriz, i), i)


main()