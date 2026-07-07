from pygame import *
import sys 

clock = time.Clock()
init()
window = display.set_mode((720,624))

# Load das imagens

idle_up = image.load('Idle_Spear_Up.png')
idle_down = image.load('Idle_Spear_Down.png')

andar_up = image.load('walk_Spear_Up.png')
andar_down = image.load('walk_Spear_Down.png')

andar_left_up = image.load('walk_Spear_Left_Up.png')
andar_left_down = image.load('walk_Spear_Left_Down.png')

andar_right_up = image.load('walk_Spear_Right_Up.png')
andar_right_down = image.load('walk_Spear_Right_Down.png')

pulo_up = image.load('Jump_spear_Up.png')
pulo_down = image.load('Jump_Spear_Down.png')
pulo_left = image.load('Jump_Spear_Left_Down.png')
pulo_right = image.load('Jump_Spear_Right_Down.png')

morrer_up = image.load('death_Spear_Up.png')
morrer_down = image.load('death_Spear_Down.png')

ataque_up = image.load('Attack_Spear_Up.png')
ataque_down = image.load('Attack_Spear_Down.png')
ataque_left = image.load('Attack_Spear_Left.png')
ataque_right = image.load('Attack_Spear_Right.png')

# Zumbi 

zumbi_idle_down = image.load('idle_down_zombie_spritesheet.png')
zumbi_idle_up = image.load('idle_up_zombie_spritesheet.png')

zumbi_walk_down = image.load('walk_down_zombie_spritesheet.png')
zumbi_walk_up = image.load('walk_up_zombie_spritesheet.png')
zumbi_walk_left = image.load('walk_left_zombie_spritesheet.png')
zumbi_walk_right = image.load('walk_right_zombie_spritesheet.png')


zumbi_attack_down = image.load('attack_down_zombie_spritesheet.png')
zumbi_attack_up = image.load('attack_up_zombie_spritesheet.png')
zumbi_attack_left = image.load('attack_left_zombie_spritesheet.png')
zumbi_attack_right = image.load('attack_right_zombie_spritesheet.png')


zumbi_morrer_down = image.load('zumbi_morrer_down.png')
zumbi_morrer_up = image.load('zumbi_morrer_up.png')
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

atacar = False
frame_atual_ataque = 0
anim_time_ataque = 0

ataque_acertou = False
alcance_lanca = 40

direcao = "down"


# Variaveis do zumbi

frame_atual_zumbi_idle = 0
anim_time_zumbi_idle = 0

zumbi_x = 200
zumbi_y = 200
velocidade_zumbi = 4

andar_zumbi = False
frame_atual_zumbi_walk = 0
anim_time_zumbi_walk = 0

atacar_zumbi = False 
frame_atual_zumbi_atacar = 0
anim_time_zumbi_atacar = 0

vidas_zumbi = 3

morrer_zumbi = False
frame_atual_zumbi_morrer = 0
anim_time_zumbi_morrer = 0

ataque_zumbi_acertou = False
alcance_ataque_zumbi = 55

direcao_zumbi = "down"

# Funções:

def verificar_ataque():
    caixa_zumbi = Rect(zumbi_x, zumbi_y, 64, 64)

    if direcao == "right":
        caixa_ataque = Rect(pos_x + 48, pos_y + altura_pulo, alcance_lanca, 48)

    elif direcao == "left":
        caixa_ataque = Rect(pos_x - alcance_lanca, pos_y + altura_pulo, alcance_lanca, 48)

    elif direcao == "up":
        caixa_ataque = Rect(pos_x, pos_y + altura_pulo - alcance_lanca, 48, alcance_lanca)

    else:
        caixa_ataque = Rect(pos_x, pos_y + altura_pulo + 48, 48, alcance_lanca)

    if caixa_ataque.colliderect(caixa_zumbi):
        return True
    else:
        return False

def verificar_ataque_zumbi():
    caixa_personagem = Rect(pos_x, pos_y + altura_pulo, 48, 48)

    if direcao_zumbi == "right":
        caixa_ataque_zumbi = Rect(zumbi_x + 35, zumbi_y - 10, alcance_ataque_zumbi + 25, 84)

    elif direcao_zumbi == "left":
        caixa_ataque_zumbi = Rect(zumbi_x - alcance_ataque_zumbi - 5, zumbi_y - 10, alcance_ataque_zumbi + 25, 84)

    elif direcao_zumbi == "up":
        caixa_ataque_zumbi = Rect(zumbi_x - 10, zumbi_y - alcance_ataque_zumbi - 5, 84, alcance_ataque_zumbi + 25)

    else:
        caixa_ataque_zumbi = Rect(zumbi_x - 10, zumbi_y + 35, 84, alcance_ataque_zumbi + 25)

    if caixa_ataque_zumbi.colliderect(caixa_personagem):
        return True
    else:
        return False

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
            if ev.key == K_v:
                vidas -= 1

        if ev.type == MOUSEBUTTONDOWN and morrer == False:
            if ev.button == 1 and atacar == False:
                atacar = True
                frame_atual_ataque = 0
                anim_time_ataque = 0
                ataque_acertou = False

    clock.tick(60)
    dt = clock.get_time()
    keys = key.get_pressed()

    # mecanismos personagem

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
        atacar = False

    if pular == True:
        altura_pulo += vel_y * (dt/100)
        vel_y += gravidade

        if altura_pulo >= 0:
            altura_pulo = 0
            pular = False
            vel_y = 0
            frame_atual_pulo = 0

    # Mecanismos zumbi 
    distancia_x_zumbi = pos_x - zumbi_x
    distancia_y_zumbi = pos_y - zumbi_y

    if vidas_zumbi <= 0:
        morrer_zumbi = True

    if morrer_zumbi == True:
        andar_zumbi = False
        atacar_zumbi = False

        
    if morrer_zumbi == False and  abs(distancia_x_zumbi) < 250 and abs(distancia_y_zumbi) < 250:

        if abs(distancia_x_zumbi) <= 25 and abs(distancia_y_zumbi) <= 25:
            andar_zumbi = False
            if atacar_zumbi == False:
                atacar_zumbi = True
                frame_atual_zumbi_atacar = 0
                anim_time_zumbi_atacar = 0
                ataque_zumbi_acertou = False
        else:
            andar_zumbi = True
            atacar_zumbi = False

            vel_zumbi = velocidade_zumbi * (dt/100)

            if pos_x > zumbi_x:
                zumbi_x += vel_zumbi
            elif pos_x < zumbi_x:
                zumbi_x -= vel_zumbi

            if pos_y > zumbi_y:
                zumbi_y += vel_zumbi
            elif pos_y < zumbi_y:
                zumbi_y -= vel_zumbi

            if abs(distancia_x_zumbi) > abs(distancia_y_zumbi) + 10:
                if pos_x > zumbi_x:
                    direcao_zumbi = "right"
                elif pos_x < zumbi_x:
                    direcao_zumbi = "left"
            elif abs(distancia_y_zumbi) > abs(distancia_x_zumbi) + 10:
                if pos_y > zumbi_y:
                    direcao_zumbi = "down"
                elif pos_y < zumbi_y:
                    direcao_zumbi = "up"
    else:
        andar_zumbi = False
        atacar_zumbi = False


    window.fill((141, 207, 241))

    anim_time_idle += dt
    anim_time_idle_set = anim_time_idle / 1000

     # Animacoes personagem
    if morrer == True:

        anim_time_morrer += dt
        anim_time_morrer_set = anim_time_morrer / 1000

        if anim_time_morrer_set > 0.1:
            frame_atual_morrer += 1
            if frame_atual_morrer > 7:
                frame_atual_morrer = 7
            anim_time_morrer = 0

        if direcao == "up":
            window.blit(morrer_up, (pos_x, pos_y), ((frame_atual_morrer * 48), 0, 48, 48))
        else:
            window.blit(morrer_down, (pos_x, pos_y), ((frame_atual_morrer * 48), 0, 48, 48))


    elif atacar == True:
        anim_time_ataque += dt
        anim_time_ataque_set = anim_time_ataque / 1000

        if anim_time_ataque_set > 0.05:
            frame_atual_ataque += 1
            if frame_atual_ataque > 7:
                frame_atual_ataque = 0
                atacar = False
            anim_time_ataque = 0

            if ataque_acertou == False and morrer_zumbi == False and frame_atual_ataque >= 3:
                if verificar_ataque() == True:
                    vidas_zumbi -= 1
                    ataque_acertou = True
                    
        if direcao == "left":
                window.blit(ataque_left, (pos_x, pos_y + altura_pulo), ((frame_atual_ataque * 48), 0, 48, 48))

        elif direcao == "down":
                window.blit(ataque_down, (pos_x, pos_y + altura_pulo),((frame_atual_ataque * 48), 0, 48, 48))

        elif direcao == "right" :
                window.blit(ataque_right,(pos_x, pos_y + altura_pulo),((frame_atual_ataque * 48), 0, 48, 48))
        else:
                window.blit(ataque_up,(pos_x, pos_y + altura_pulo),((frame_atual_ataque * 48), 0, 48, 48))


    elif chaves_andar_up == True:
        direcao = "up"
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
        direcao = "down"
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

        if direcao == "up":
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

        if direcao == "up":
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

        elif direcao == "up":
            window.blit(pulo_up, (pos_x, pos_y + altura_pulo), ((frame_atual_pulo * 48), 0, 48, 48))

        else:
            window.blit(pulo_down, (pos_x, pos_y + altura_pulo), ((frame_atual_pulo * 48), 0, 48, 48))


    else:
        if anim_time_idle_set > 0.15:
            frame_atual_idle += 1
            if frame_atual_idle > 7:
                frame_atual_idle = 0
            anim_time_idle = 0

        if direcao == "up":
            window.blit(idle_up, (pos_x, pos_y), ((frame_atual_idle * 48), 0, 48, 48))
        else:
            window.blit(idle_down, (pos_x, pos_y), ((frame_atual_idle * 48), 0, 48, 48))
    

# Animacoes zumbi 

    anim_time_zumbi_idle += dt
    anim_time_zumbi_idle_set = anim_time_zumbi_idle / 1000

    if morrer_zumbi == True:

        anim_time_zumbi_morrer += dt
        anim_time_zumbi_morrer_set = anim_time_zumbi_morrer / 1000

        if anim_time_zumbi_morrer_set > 0.1:
            frame_atual_zumbi_morrer += 1

            if frame_atual_zumbi_morrer > 7:
                frame_atual_zumbi_morrer = 7

            anim_time_zumbi_morrer = 0

        if direcao_zumbi == "up":
            window.blit(zumbi_morrer_up, (zumbi_x, zumbi_y), ((frame_atual_zumbi_morrer * 64), 0, 64, 64))
        else:
            window.blit(zumbi_morrer_down, (zumbi_x, zumbi_y), ((frame_atual_zumbi_morrer * 64), 0, 64, 64))


    elif atacar_zumbi == True:
        anim_time_zumbi_atacar += dt
        anim_time_zumbi_atacar_set = anim_time_zumbi_atacar / 1000
        if anim_time_zumbi_atacar_set > 0.1:
            frame_atual_zumbi_atacar += 1

            if frame_atual_zumbi_atacar > 7:
                frame_atual_zumbi_atacar = 0
                ataque_zumbi_acertou = False

            anim_time_zumbi_atacar = 0

            if ataque_zumbi_acertou == False and morrer == False and frame_atual_zumbi_atacar >= 3:
                if verificar_ataque_zumbi() == True:
                    vidas -= 1
                    ataque_zumbi_acertou = True

        if direcao_zumbi == "left":
            window.blit(zumbi_attack_left, (zumbi_x, zumbi_y), ((frame_atual_zumbi_atacar * 64), 0, 64, 64))

        elif direcao_zumbi == "right":
            window.blit(zumbi_attack_right, (zumbi_x, zumbi_y), ((frame_atual_zumbi_atacar * 64), 0, 64, 64))

        elif direcao_zumbi == "up":
            window.blit(zumbi_attack_up, (zumbi_x, zumbi_y), ((frame_atual_zumbi_atacar * 64), 0, 64, 64))

        else:
            window.blit(zumbi_attack_down, (zumbi_x, zumbi_y), ((frame_atual_zumbi_atacar * 64), 0, 64, 64))


    elif andar_zumbi == True:

        anim_time_zumbi_walk += dt
        anim_time_zumbi_walk_set = anim_time_zumbi_walk / 1000

        if anim_time_zumbi_walk_set > 0.15:
            frame_atual_zumbi_walk += 1
            if frame_atual_zumbi_walk > 7:
                frame_atual_zumbi_walk = 0
            anim_time_zumbi_walk = 0

        if direcao_zumbi == "right":
            window.blit(zumbi_walk_right,(zumbi_x, zumbi_y),((frame_atual_zumbi_walk * 64), 0, 64, 64))

        elif direcao_zumbi == "left":
            window.blit(zumbi_walk_left,(zumbi_x, zumbi_y),((frame_atual_zumbi_walk * 64), 0, 64, 64))

        elif direcao_zumbi == "down":
            window.blit(zumbi_walk_down,(zumbi_x, zumbi_y),((frame_atual_zumbi_walk * 64), 0, 64, 64))

        else:
            window.blit(zumbi_walk_up,(zumbi_x, zumbi_y),((frame_atual_zumbi_walk * 64), 0, 64, 64))
                
    else:
        if anim_time_zumbi_idle_set > 0.2:
            frame_atual_zumbi_idle += 1
            if frame_atual_zumbi_idle > 3:
                frame_atual_zumbi_idle = 0
            anim_time_zumbi_idle = 0

        if direcao_zumbi == "up":
            window.blit(zumbi_idle_up,(zumbi_x, zumbi_y),((frame_atual_zumbi_idle * 64), 0, 64, 64))

        else:
            window.blit(zumbi_idle_down,(zumbi_x, zumbi_y),((frame_atual_zumbi_idle * 64), 0, 64, 64))

    display.update()