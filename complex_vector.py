from sys import stdin
from math import *


def suma(c1, c2):
    """
    La función suma recibe dos números complejos (listas de longitud 2) y retorna
    un único número complejo (lista de longitud 2) que es la suma de la parte real y
    la suma de la parte imaginaria de cada número
    """
    return [c1[0] + c2[0], c1[1] + c2[1]]


def resta(c1, c2):
    """
    La función resta recibe dos números complejos (listas de longitud 2) y retorna
    un único número complejo (lista de longitud 2) que corresponde a la resta de la parte real y
    la resta de la parte imaginaria de cada número respectivamente
    """
    return [c1[0] - c2[0], c1[1] - c2[1]]


def Multiplicacion(x, z):
    """
La funcion recibe dos tuplas, cada una es un numero imaginario x y z en ellas la posicion
      [0] esta parte real y [1] es la parte imaginaria, hallamos ParteA y ParteD para
      al final sumarlos y hallar la parte real despues hallamos ParteB y ParteC las cuales sumamos para hallar
      la parte imaginaria.
 se retorna una tupla [0] parte real y [1] parte imaginaria
    """
    A = x[0] * z[0]
    B = x[0] * z[1]
    C = x[1] * z[0]
    D = (x[1] * z[1]) * (-1)
    SumR = A + D
    SumI = B + C
    Respuesta = (SumR, SumI)
    return Respuesta


def Div(x, z):
    """
   Entran dos tuplas (x,z) = numero imaginario [0] = parte real y [1] = parte imaginaria ParteR = Numerador[0] / Denominador
                        ParteI = Numerador[1] / Denominador.
   Return tupla [0] = parte real y [1] = parte imaginaria
    """
    Numerador = Multiplicacion(x, z)
    Denominador = (z[0] ** 2) + (z[1] ** 2)
    ParteR = Numerador[0] / Denominador
    ParteI = Numerador[1] / Denominador
    Respuesta = (ParteR, ParteI)
    return Respuesta


def Modulo(x):
    """
   Entra un numero complejo (x) y se le saca el modulo.
   return modulo del numero complejo
    """
    return ((x[0] ** 2) + (x[1] ** 2)) ** 0.5


def Conjugado(x):
    """
   Entra un numero complejo (x) se multiplica parte imaginaria por -1
   return ParteR igual que como entra y la ParteI negativa
    """
    return [x[0], x[1] * -1]


def cart_pol(c1):
    """
    La función cart_pol recibe un número complejo (lista de longitud 2) y retorna la
    operación de pasar de cartesianas a polares, con el lado y ángulo respectivamente
    """
    r = math.sqrt(c1[0]**2 + c1[1]**2)
    angle = math.degrees(math.atan2(c1[1], c1[0]))
    return [r, angle]


def pol_cart(c1):
    """
    La función pol_cart recibe un número complejo (lista de longitud 2) y retorna la
    operación de pasar de polares a cartesianas, con las coordenadas X y Y respectivamente
    """
    r, angle = c1[0], math.radians(c1[1])
    x = r * math.cos(angle)
    y = r * math.sin(angle)
    return [x, y]


def Fase(x):
    """
     Entra un numeron complejo el cual vamos sacarle su fase
     return la arco tangente de su ParteI sobre su ParteR
    """
    respuesta = atan(x[1] / x[0])
    return respuesta