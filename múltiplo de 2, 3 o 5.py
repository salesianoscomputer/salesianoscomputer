print('Este programa te dice si un número es múltiplo de 2, 3 o 5')  #imprime lo que hace el programa
n=input('Escribe un número: ')  #guarda en una variable el número que le digas
n=int(n)  #dice que interprete lo que le dijiste como un número

#comprueba si el resto de el número que pusiste entre 2 es 0
if n%2==0:  #si es así
    div2=n/2  #divide entre 2 el número
    print('El número',n,'es múltiplo de 2')  #dice que el número es múltiplo de 2
    print('Al dividir',n,'entre 2 se obtiene',div2)  #dice cuanto da la división
else:  #si no es así
    print('El número', n, 'no es múltiplo de 2')  #dice que no es múltiplo de 2

#comprueba si el resto de el número que pusiste entre 3 es 0
if n%3==0:  #si es así
    div3=n/3  #divide entre 2 el número
    print('El número',n,'es múltiplo de 3')  #dice que el número es múltiplo de 2
    print('Al dividir',n,'entre 3 se obtiene',div3)  #dice cuanto da la división
else:  #si no es así
    print('El número', n, 'no es múltiplo de 3')  #dice que no es múltiplo de 2

#comprueba si el resto de el número que pusiste entre 5 es 0
if n%5==0:  #si es así
    div5=n/5  #divide entre 2 el número
    print('El número',n,'es múltiplo de 5')  #dice que el número es múltiplo de 2
    print('Al dividir',n,'entre 5 se obtiene',div5)  #dice cuanto da la división
else:  #si no es así
    print('El número', n, 'no es múltiplo de 5')  #dice que no es múltiplo de 2