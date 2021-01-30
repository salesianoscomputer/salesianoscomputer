from random import randint  #importa la función de aleatoriedad
from time import sleep  #importa la función de esperar

print('Programa que genera 10 nùmeros aleatorios')  #dice de que va el programa
for n in range(10):  #repite 10 veces
    numero=randint(1,100)  #genera un número aleatorio del 1 al 100
    print('Generación:',n+1,'Número generado:',numero)  #dice el número que ha generado
    sleep(1)  #espera un segundo