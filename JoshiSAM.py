import pygame
import sys
import random
from pygame.locals import *
pygame.init()
 
#COLORES
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ORANGE=(255,165,5)
CELESTE=(66,148,255)
#PANTALLA
ANCHO=1000
ALTO=800
#JUGADOR
JUGADOR_POS=[500,750]
JUGADOR_TAM=20
#ENEMIGO1
ENEMIGO_TAM=25
ENEMIGO_POS=[random.randint(0,ANCHO-ENEMIGO_TAM),30]
#ENEMIGO2
ENEMIGO_TAM2=35
ENEMIGO_POS2=[random.randint(0,ANCHO-ENEMIGO_TAM2),30]
#ENEMIGO3
ENEMIGO_TAM3=30
ENEMIGO_POS3=[random.randint(0,ANCHO-ENEMIGO_TAM3),30]
#ENEMIGO4
ENEMIGO_TAM4=38
ENEMIGO_POS4=[random.randint(0,ANCHO-ENEMIGO_TAM4),30]

#ENEMIGO5
ENEMIGO_TAM5=42
ENEMIGO_POS5=[random.randint(0,ANCHO-ENEMIGO_TAM5),30]

#ventana
ventana= pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption("SAMMEX")

clock=pygame.time.Clock()

#Escribir 
fuente = pygame.font.Font(None, 50)
texto1 = fuente.render("Bienvenidos al JOSHISAM", 0, (ORANGE))
#Escribir Reloj
fuente1 = pygame.font.SysFont("Arial",34,True,False)
info = fuente1.render("Cloock", 0, (ORANGE))
texto2 = fuente1.render("Tiempo :", 0, (WHITE))




#Funciones
def detectar_colision1(JUGADOR_POS,ENEMIGO_POS,):
    jx=JUGADOR_POS[0]
    jy=JUGADOR_POS[1]
    ex=ENEMIGO_POS[0]
    ey=ENEMIGO_POS[1]
    
    if (ex>jx and ex<(jx+JUGADOR_TAM)) or (jx>=ex and jx<(ex+ENEMIGO_TAM)):
       if (ey>jy and ey<(jy+JUGADOR_TAM)) or (jy>=ex and jy<(ey+ENEMIGO_TAM)):
                return True
    return False
def detectar_colision2(JUGADOR_POS,ENEMIGO_POS2,):
    jx=JUGADOR_POS[0]
    jy=JUGADOR_POS[1]
    ex=ENEMIGO_POS2[0]
    ey=ENEMIGO_POS2[1]
    
    if (ex>jx and ex<(jx+JUGADOR_TAM)) or (jx>=ex and jx<(ex+ENEMIGO_TAM)):
       if (ey>jy and ey<(jy+JUGADOR_TAM)) or (jy>=ex and jy<(ey+ENEMIGO_TAM)):
                return True
    return False
def detectar_colision3(JUGADOR_POS,ENEMIGO_POS3,):
    jx=JUGADOR_POS[0]
    jy=JUGADOR_POS[1]
    ex=ENEMIGO_POS3[0]
    ey=ENEMIGO_POS3[1]
    
    if (ex>jx and ex<(jx+JUGADOR_TAM)) or (jx>=ex and jx<(ex+ENEMIGO_TAM3)):
       if (ey>jy and ey<(jy+JUGADOR_TAM)) or (jy>=ex and jy<(ey+ENEMIGO_TAM3)):
                return True
    return False

def detectar_colision4(JUGADOR_POS,ENEMIGO_POS4,):
    jx=JUGADOR_POS[0]
    jy=JUGADOR_POS[1]
    ex=ENEMIGO_POS4[0]
    ey=ENEMIGO_POS4[1]
    
    if (ex>jx and ex<(jx+JUGADOR_TAM)) or (jx>=ex and jx<(ex+ENEMIGO_TAM4)):
       if (ey>jy and ey<(jy+JUGADOR_TAM)) or (jy>=ex and jy<(ey+ENEMIGO_TAM4)):
                return True
    return False

def detectar_colision5(JUGADOR_POS,ENEMIGO_POS5,):
    jx=JUGADOR_POS[0]
    jy=JUGADOR_POS[1]
    ex=ENEMIGO_POS5[0]
    ey=ENEMIGO_POS5[1]
    
    if (ex>jx and ex<(jx+JUGADOR_TAM)) or (jx>=ex and jx<(ex+ENEMIGO_TAM5)):
       if (ey>jy and ey<(jy+JUGADOR_TAM)) or (jy>=ex and jy<(ey+ENEMIGO_TAM5)):
                return True
    return False


         
game_over=False
running= True
while not game_over:        
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
           x=JUGADOR_POS[0] 
           if x>=9:
             if event.key == pygame.K_LEFT:
              x-=JUGADOR_TAM
             if event.key == pygame.K_RIGHT:
              x+=JUGADOR_TAM
             JUGADOR_POS[0]=x
           else:
               x=10
               JUGADOR_POS[0]=x
           if x<=ANCHO-2:
             if event.key == pygame.K_LEFT:
              x-=JUGADOR_TAM
             if event.key == pygame.K_RIGHT:
              x+=JUGADOR_TAM
             JUGADOR_POS[0]=x
           else:
               x=ANCHO-3
               JUGADOR_POS[0]=x
           
           

    ventana.fill(BLACK)
   #Movimiento enemigo 1
    if ENEMIGO_POS[1]>=0 and ENEMIGO_POS[1]<ALTO:
       ENEMIGO_POS[1]+=20
    else:
       ENEMIGO_POS[0]=random.randint(0,ANCHO-ENEMIGO_TAM)
       ENEMIGO_POS[1]=0
   #moviemiento enemigo 2
    if ENEMIGO_POS2[1]>=0 and ENEMIGO_POS2[1]<ALTO:
       ENEMIGO_POS2[1]+=25
    else:
       ENEMIGO_POS2[0]=random.randint(0,ANCHO-ENEMIGO_TAM2)
       ENEMIGO_POS2[1]=0
   #moviemiento enemigo 3
    if ENEMIGO_POS3[1]>=0 and ENEMIGO_POS3[1]<ALTO:
       ENEMIGO_POS3[1]+=25
    else:
       ENEMIGO_POS3[0]=random.randint(0,ANCHO-ENEMIGO_TAM3)
       ENEMIGO_POS3[1]=0

    #moviemiento enemigo 4
    if ENEMIGO_POS4[1]>=0 and ENEMIGO_POS4[1]<ALTO:
       ENEMIGO_POS4[1]+=25
    else:
       ENEMIGO_POS4[0]=random.randint(0,ANCHO-ENEMIGO_TAM4)
       ENEMIGO_POS4[1]=0

    #moviemiento enemigo 5
    if ENEMIGO_POS5[1]>=0 and ENEMIGO_POS5[1]<ALTO:
       ENEMIGO_POS5[1]+=25
    else:
       ENEMIGO_POS5[0]=random.randint(0,ANCHO-ENEMIGO_TAM5)
       ENEMIGO_POS5[1]=0

    #Colisiones
    if detectar_colision1(JUGADOR_POS,ENEMIGO_POS,):
        game_over=True
    if detectar_colision2(JUGADOR_POS,ENEMIGO_POS2,):
        game_over=True
    if detectar_colision3(JUGADOR_POS,ENEMIGO_POS3,):
        game_over=True
    if detectar_colision4(JUGADOR_POS,ENEMIGO_POS4,):
        game_over=True
    if detectar_colision5(JUGADOR_POS,ENEMIGO_POS5,):
        game_over=True


    #DIBUJAR ENEMIGO1
    pygame.draw.circle(ventana, RED, (ENEMIGO_POS[0], ENEMIGO_POS[1]), ENEMIGO_TAM, ENEMIGO_TAM)

    #DIBUJAR ENEMIGO2
    pygame.draw.circle(ventana, WHITE, (ENEMIGO_POS2[0], ENEMIGO_POS2[1]), ENEMIGO_TAM2, ENEMIGO_TAM2)

    #DIBUJAR ENEMIGO3
    pygame.draw.circle(ventana, BLUE, (ENEMIGO_POS3[0], ENEMIGO_POS3[1]), ENEMIGO_TAM3, ENEMIGO_TAM3)

    #DIBUJAR ENEMIGO4
    pygame.draw.circle(ventana, ORANGE, (ENEMIGO_POS4[0], ENEMIGO_POS4[1]), ENEMIGO_TAM4, ENEMIGO_TAM4)
    
    #DIBUJAR ENEMIGO5
    pygame.draw.circle(ventana, CELESTE, (ENEMIGO_POS5[0], ENEMIGO_POS5[1]), ENEMIGO_TAM5, ENEMIGO_TAM5)
    
   
    #Dibujar jugador
    pygame.draw.circle(ventana, GREEN, (JUGADOR_POS[0], JUGADOR_POS[1]), JUGADOR_TAM, JUGADOR_TAM)

    
    segundos=pygame.time.get_ticks()/1000
    segundos=str(segundos)
    contador=fuente1.render(segundos,0,(GREEN))
    ventana.blit(contador, (120,20))
    ventana.blit(texto1, (300,50))
    ventana.blit(texto2, (5,20))
    clock.tick(50)#Velocidad
    pygame.display.update()