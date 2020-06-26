import pygame 
import sys
import random


ANCHO=800
ALTO=600
posx=375
posy=500
rojo=(255,0,0)
blanco=(255,255,255)
azul=(0,0,255)
jugador_size=50
enemigo_size=50
posx1=random.randint(0,ANCHO-enemigo_size)
posy1=0

ventana=pygame.display.set_mode((ANCHO, ALTO))

a=False
hola=pygame.time.Clock()

def colision (posx,posy,posx1,posy1):
    jug_x=posx
    jug_y=posy
    enem_x=posx1
    enem_y=posy1
    if (enem_x >= jug_x and enem_x < (jug_x + jugador_size)) or (jug_x >= enem_x and jug_x < (enem_x + enemigo_size)):
        if (enem_y >= jug_y and enem_y < (jug_y + jugador_size)) or (jug_y >= enem_y and jug_y < (enem_y + enemigo_size)):
            return True
    return False

while not a:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            x=posx
            y=posy
            if event.key == pygame.K_LEFT:
                x-=20
            if event.key == pygame.K_RIGHT:
                x+=20
            if event.key == pygame.K_DOWN:
                y+=20
            if event.key == pygame.K_UP:
                y-=20
            posx=x
            posy=y

    ventana.fill(blanco)

    if posy1 >=0 and posy1 < ALTO:
        posy1+=20
    else:
        posx1=random.randint(0,ANCHO-enemigo_size)
        posy1=0

    if colision(posx,posy,posx1,posy1):
        a=True

    pygame.draw.rect(ventana, azul, (posx1,posy1,enemigo_size,enemigo_size))

    pygame.draw.rect(ventana, rojo, (posx,posy,jugador_size,jugador_size))

    hola.tick(30)

    pygame.display.update()