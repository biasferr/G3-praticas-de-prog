
from pygame import *
import sys 


clock = time.Clock()
init()
window = display.set_mode((720,624))

window.fill((255,255,255))

# Load das imagens

idle_baixada = image.load('Idle.png')
idle = transform.scale(idle_baixada,(384 , 288))


# Variáveis do Idle

frame_atual_idle = 0    
anim_time_idle = 0

pos_x = 10
pos_y = 15

while True:
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()

        
    clock.tick(60)
    dt = clock.get_time()
    keys = key.get_pressed()


    #IDLE 
    anim_time_idle = anim_time_idle + dt
    anim_time_idle_set = anim_time_idle/1000

      

    # Desenhos no pygame

    window.fill((141, 207, 241))
    draw.rect(window,(136, 231, 137),(0,364,720,276))


    window.blit(idle, (300, 400) , ((frame_atual_idle * 48) , 0 , 48,48))

    if anim_time_idle_set > 0.15:
            frame_atual_idle += 1
            if frame_atual_idle > 7:
                frame_atual_idle = 0
            anim_time_idle = 0


    display.update()

