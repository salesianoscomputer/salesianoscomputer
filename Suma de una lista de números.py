print('Programa que pedirá números hasta dejar una entrada vacía')  #explica de que va el programa
print('El programa cuenta cuántos números se han introducido')  #explica de que va el programa
print('y la suma de todos esos números introducidos')  #explica de que va el programa
print('(Entrada vacía = Terminar)')  #explica de que va el programa
n=0  #define una variable a 0
suma=0  #define otra variable a 0
seguir=True  #define una variable para controlar el bucle
while seguir:  #empieza el bucle
    numero=input('Escribe un número: ')  #fija una variable al número que le digas
    if numero=='':  #si no le has puesto nada
        seguir=False  #quita el bucle
    else:  #si le pusiste algo
        numero=int(numero)  #dice que la respuesta es un número
        n=n+1  #suma 1 a una variable llamada n
        suma+=numero  #sumas a una variable el número

print('Se han introducido',n,'números')  #dice cuantos números se han introducido
print('Los números suman',suma)   #dice la suma de todos los números