from pygame import *
import sys 

clock = time.Clock()
init()
window = display.set_mode((720,624))

# Load das imagens

idle_up = image.load('Animacoes_movimentacao/Idle/Idle_Up.png')
idle_down = image.load('Animacoes_movimentacao/Idle/Idle_Down.png')

andar_up = image.load('Animacoes_movimentacao/andar/walk_Up.png')
andar_down = image.load('Animacoes_movimentacao/andar/walk_Down.png')

andar_left_up = image.load('Animacoes_movimentacao/andar/walk_Left_Up.png')
andar_left_down = image.load('Animacoes_movimentacao/andar/walk_Left_Down.png')

andar_right_up = image.load('Animacoes_movimentacao/andar/walk_Right_Up.png')
andar_right_down = image.load('Animacoes_movimentacao/andar/walk_Right_Down.png')

pulo_up = image.load('Animacoes_movimentacao/pular/Jump_Up.png')
pulo_down = image.load('Animacoes_movimentacao/pular/Jump_Down.png')
pulo_left = image.load('Animacoes_movimentacao/pular/Jump_Left_Down.png')
pulo_right = image.load('Animacoes_movimentacao/pular/Jump_Right_Down.png')

morrer_up = image.load('Animacoes_movimentacao/morrer/Death_Up.png')
morrer_down = image.load('Animacoes_movimentacao/morrer/Death_Down.png')

# Variáveis

frame_atual_idle = 0
anim_time_idle = 0

pos_x = 300
pos_y = 300
velocidade = 14

frame_atual_walkUp = 0
anim_time_walkUp = 0

frame_atual_walkDown = 0
anim_time_walkDown = 0

frame_atual_walkLeft = 0
anim_time_walkLeft = 0

frame_atual_walkRight = 0
anim_time_walkRight = 0

pular = False
frame_atual_pulo = 0
anim_time_pulo = 0

vel_y = 0
gravidade = 1
altura_pulo = 0

morrer = False
frame_atual_morrer = 0
anim_time_morrer = 0

vidas = 3

direcao = "right"
direcao_vertical = "down"

# loop principal
while True:
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()

        if ev.type == KEYDOWN and pular == False and morrer == False:
            if ev.key == K_SPACE:
                pular = True
                vel_y = -16
            if ev.key == K_v: # Só pra testar 
                vidas -= 1

    clock.tick(60)
    dt = clock.get_time()
    keys = key.get_pressed()

    chaves_andar_up = keys[K_w]
    chaves_andar_down = keys[K_s]
    chaves_andar_left = keys[K_a]
    chaves_andar_right = keys[K_d]

    if vidas <= 0:
        morrer = True

    if morrer == True:
        chaves_andar_up = False
        chaves_andar_down = False
        chaves_andar_left = False
        chaves_andar_right = False
        pular = False

    if pular == True:
        altura_pulo += vel_y * (dt/100)
        vel_y += gravidade

        if altura_pulo >= 0:
            altura_pulo = 0
            pular = False
            vel_y = 0
            frame_atual_pulo = 0

    window.fill((141, 207, 241))

    anim_time_idle += dt
    anim_time_idle_set = anim_time_idle / 1000


    if morrer == True:

        anim_time_morrer += dt
        anim_time_morrer_set = anim_time_morrer / 1000

        if anim_time_morrer_set > 0.1:
            frame_atual_morrer += 1
            if frame_atual_morrer > 7:
                frame_atual_morrer = 7
            anim_time_morrer = 0

        if direcao_vertical == "up":
            window.blit(morrer_up, (pos_x, pos_y), ((frame_atual_morrer * 48), 0, 48, 48))
        else:
            window.blit(morrer_down, (pos_x, pos_y), ((frame_atual_morrer * 48), 0, 48, 48))

    elif chaves_andar_up == True:
        direcao_vertical = "up"
        pos_y -= velocidade * (dt/100)

        anim_time_walkUp += dt
        anim_time_walkUp_set = anim_time_walkUp / 1000

        if anim_time_walkUp_set > 0.15:
            frame_atual_walkUp += 1
            if frame_atual_walkUp > 7:
                frame_atual_walkUp = 0
            anim_time_walkUp = 0

        window.blit(andar_up, (pos_x, pos_y + altura_pulo), ((frame_atual_walkUp * 48), 0, 48, 48))


    elif chaves_andar_down == True:
        direcao_vertical = "down"
        pos_y += velocidade * (dt/100)

        anim_time_walkDown += dt
        anim_time_walkDown_set = anim_time_walkDown / 1000

        if anim_time_walkDown_set > 0.15:
            frame_atual_walkDown += 1
            if frame_atual_walkDown > 7:
                frame_atual_walkDown = 0
            anim_time_walkDown = 0

        window.blit(andar_down, (pos_x, pos_y + altura_pulo), ((frame_atual_walkDown * 48), 0, 48, 48))


    elif chaves_andar_left == True:
        direcao = "left"
        pos_x -= velocidade * (dt/100)

        anim_time_walkLeft += dt
        anim_time_walkLeft_set = anim_time_walkLeft / 1000

        if anim_time_walkLeft_set > 0.15:
            frame_atual_walkLeft += 1
            if frame_atual_walkLeft > 7:
                frame_atual_walkLeft = 0
            anim_time_walkLeft = 0

        if direcao_vertical == "up":
            window.blit(andar_left_up, (pos_x, pos_y + altura_pulo), ((frame_atual_walkLeft * 48), 0, 48, 48))
        else:
            window.blit(andar_left_down, (pos_x, pos_y + altura_pulo), ((frame_atual_walkLeft * 48), 0, 48, 48))


    elif chaves_andar_right == True:
        direcao = "right"
        pos_x += velocidade * (dt/100)

        anim_time_walkRight += dt
        anim_time_walkRight_set = anim_time_walkRight / 1000

        if anim_time_walkRight_set > 0.15:
            frame_atual_walkRight += 1
            if frame_atual_walkRight > 7:
                frame_atual_walkRight = 0
            anim_time_walkRight = 0

        if direcao_vertical == "up":
            window.blit(andar_right_up, (pos_x, pos_y + altura_pulo), ((frame_atual_walkRight * 48), 0, 48, 48))
        else:
            window.blit(andar_right_down, (pos_x, pos_y + altura_pulo), ((frame_atual_walkRight * 48), 0, 48, 48))


    elif pular == True:
        anim_time_pulo += dt
        anim_time_pulo_set = anim_time_pulo / 1000

        if anim_time_pulo_set > 0.09:
            frame_atual_pulo += 1
            if frame_atual_pulo > 7:
                frame_atual_pulo = 0
            anim_time_pulo = 0

        if direcao == "left":
            window.blit(pulo_left, (pos_x, pos_y + altura_pulo), ((frame_atual_pulo * 48), 0, 48, 48))

        elif direcao == "right":
            window.blit(pulo_right, (pos_x, pos_y + altura_pulo), ((frame_atual_pulo * 48), 0, 48, 48))

        elif direcao_vertical == "up":
            window.blit(pulo_up, (pos_x, pos_y + altura_pulo), ((frame_atual_pulo * 48), 0, 48, 48))

        else:
            window.blit(pulo_down, (pos_x, pos_y + altura_pulo), ((frame_atual_pulo * 48), 0, 48, 48))


    else:
        if anim_time_idle_set > 0.15:
            frame_atual_idle += 1
            if frame_atual_idle > 7:
                frame_atual_idle = 0
            anim_time_idle = 0

        if direcao_vertical == "up":
            window.blit(idle_up, (pos_x, pos_y), ((frame_atual_idle * 48), 0, 48, 48))
        else:
            window.blit(idle_down, (pos_x, pos_y), ((frame_atual_idle * 48), 0, 48, 48))

    display.update()
