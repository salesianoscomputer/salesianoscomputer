import random  #importa funciones de números aleatorios

def Generar_lista(lista,maximo,longitud):  #crea una función llamada Generar_lista la cual le pasas la lista a la cual vas a poner los números, hasta que número puede tener la lista y cuantos elementos puede tener  
    for i in range(longitud):  #bucle que dura los miembros que pueda tener la lista
        indice = True  #creamos una variable que sirve como interruptor para el bucle
        while(indice):   #hacemos un bucle que se desactiva cambiando índice a False para que haya tantos miembros como se dijo
            numero = random.randrange(maximo)  #genera un número entre el 1 y el número maximo
            indice=Buscar_lista(lista,numero)  #busca si hay un número repetido
        lista.append(numero)  #añade el número a la lista
    print('lista sin ordenar: ',lista)  #imprime la lista sin ordenar
    print()  #deja un hueco en blanco en la consola
    
def Buscar_lista (lista,numero):  #crea una función llamada Buscar_lista la cual le pasas en la lista la cual se va a buscar un número y el número
    for i in lista:  #revisa todos los miembros de la lista
        if i == numero:  #por cada número se mira si el número que buscamos si esta repetido es igual al miembro de la lista
            return(True)  #si es así paramos de buscar para que genere otro número aleatorio
    return(False)  #si no encuentra ninguno se añade a la lista

def Ordenar_lista (lista):  #crea una función llamada Ordenar_lista la cual ordena la lista que le dices
    lista.sort() #ordena la lista

Lista = []  #crea una lista
Generar_lista (Lista,100,20)  #genera una lista en la lista 'Lista' con números del 1 al 100 de 20 elementos
Ordenar_lista (Lista)  #ordena la lista
print('lista ordenada: ',Lista)  #imprime la lista ordenada