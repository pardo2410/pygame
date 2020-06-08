import pygame
import pygame.locals
import sys

pygame.init()

pantalla = pygame.display.set_mode((600,400))
pygame.display.set_caption('Hola Mundo')
rojo = 0
direccion = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()

    if rojo >= 255:
        direccion =-1
    if rojo <= 0:
        direccion = 1

    rojo += direccion    
    pantalla.fill((rojo,0,0))
    pygame.display.flip()
    pygame.time.delay(10)

