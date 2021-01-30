from math import sqrt  #importar función de raices cuadradas
def diagonal(lado):  #crea una función llamada diagonal la cual le pasas lo que mide el lado
    resultado=sqrt(lado**2+lado**2)  #fija a una variable lo que mide la diagonal usando pitágoras
    return resultado  #devuelve el resultado de la diagonal

print('Programa que calcula la diagonal de varios cuadrados')  #dice lo que dice
print('El cuadrado de lado',1,'tiene de diagonal',diagonal(1))  #dice la diagonal de un cuadrado de lado 1
print('El cuadrado de lado',5,'tiene de diagonal',diagonal(5))  #dice la diagonal de un cuadrado de lado 1
print('El cuadrado de lado',10,'tiene de diagonal',diagonal(10))  #dice la diagonal de un cuadrado de lado 1
print('El cuadrado de lado',12,'tiene de diagonal',diagonal(12))  #dice la diagonal de un cuadrado de lado 1