import pygame  
pygame.init() # Inicializamos pygame
size = 800, 600  # Muestro una ventana de 800x600
screen = pygame.display.set_mode(size) 
pygame.display.set_caption("Juego Ball")  # Cambio el título de la ventana
run=True  # Comenzamos el bucle del juego
while run:
    for event in pygame.event.get():# Capturamos los eventos que se han producido
        if event.type == pygame.QUIT:  # Si el evento es salir de la ventana, terminamos
            run = False  # Salgo de pygame

pygame.quit()  #salir
