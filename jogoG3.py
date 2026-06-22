from pygame import *
import sys


def geraMapa(mapa,listaMapa):
    for linha in mapa:
        linha_limpa = linha.strip()
        linha_mapa = linha_limpa.split(',')
        listaMapa.append(linha_mapa)

def mudaEscala(animacao):
    animacao = transform.scale(animacao,(768,128))
    return animacao

def desenha_mapa1():
    window.fill((0,0,0))
        #MAPA ESCOLA
    for i in range(len(mapa1)):
        for j in range(len(mapa1[i])):
            tile = mapa1[i][j]

            coordenada_escola = blocos_escola.get(tile)
            if tile == 'f':
                draw.rect(window,(0,0,0),(tilesize*j, tilesize*i, tilesize, tilesize))

            elif 'p' in tile:
                if coordenada_escola:
                    window.blit(tileset_parede,(tilesize * j , tilesize*i),(coordenada_escola[0],coordenada_escola[1],tilesize,tilesize))           
            elif 'f' in tile:
                if coordenada_escola:
                    window.blit(tileset_floor,(tilesize * j , tilesize*i),(coordenada_escola[0],coordenada_escola[1],tilesize,tilesize))           
    
            else:
                if coordenada_escola:
                    window.blit(tileset_bordas,(tilesize * j , tilesize*i),(coordenada_escola[0],coordenada_escola[1],tilesize,tilesize))           
    
    
    



    #OBJETOS ESCOLA
    for item in posicoes_objetos_mapa1:
        if len(item) == 3: 
            window.blit(item[0], item[1], item[2])
        else:
            window.blit(item[0], item[1])
    
    window.blit(objt_mapa1['cad_tras'],(88,186))
    window.blit(objt_mapa1['cad_tras'],(152,186))
    window.blit(objt_mapa1['cad_tras'],(216,186))
    window.blit(objt_mapa1['cad_tras'],(120,250))
    window.blit(objt_mapa1['cad_tras'],(152,250))
    window.blit(objt_mapa1['cad_tras'],(184,250))


def desenha_telaInicio():
    window.blit(background,(0,0))
    window.blit(settings,(400,300))
    



init()
window = display.set_mode((1056,624))
clock = time.Clock()

#TELA DE INICIO!
background = image.load('city background.png')
telaDeInicio = True
settings = image.load('ui/Setting menu.png')

#gasolina
gascan_rodando = [
    image.load('objectss/gas can rotations/west.png'),
    image.load('objectss/gas can rotations/south-east.png'),
    image.load('objectss/gas can rotations/south-west.png'),
    image.load('objectss/gas can rotations/east.png'),
    image.load('objectss/gas can rotations/north-west.png')]

gascan_desaparecendo= [
    image.load('objectss/gas can desaparecendo/gas can1.png'),
    image.load('objectss/gas can desaparecendo/gas can 2.png'),
    image.load('objectss/gas can desaparecendo/gas can 3.png')
]

frame_atual_gascan_girando = 0
anim_time_gascan = 0

frame_atual_gascan_desaparecendo = 0

gasolina = True

#MAPA 1
mapa_escola = False
arq_mapa1 = open ('mapa1.txt', 'r')
mapa1 = []  

tileset_parede = image.load('modern interior usando/Room_Bulder_subfiles_32x32/Room_Builder_Walls_32x32.png')
tileset_bordas = image.load('modern interior usando/Room_Bulder_subfiles_32x32/Room_Builder_borders_32x32.png')
tileset_floor = image.load('modern interior usando/Room_Bulder_subfiles_32x32/Room_Builder_floors_32x32.png')

tilesize = 32

geraMapa(arq_mapa1,mapa1)


blocos_escola = {
    'cse': (192,192),
    'pbs1': (0,576),
    'pbs2': (32,576),
    'csd': (256,192),
    'be': (192,224),
    'pi': (32,608),
    'bd': (256,224),
    'fcse1': (0,640),
    'fbs1': (32,640),
    'fbe1': (0,672),
    'floor1': (32,672),
    'cie': (192,256),
    'cid': (256,256),
    'bi': (224,256),
    'pbds': (64,576),
    'pbes': (0,576),
    'pbdi': (64,608),
    'pbei': (0,608),
    'fcse2': (256,832),
    'fbs2': (288,832),
    'fbe2': (256,864),
    'floor2': (288,864)


}

#OBJETOS ESCOLA
#sala 1
caminho_objt_mapa1 = 'modern interior usando/escola/5_Classroom_and_Library_Black_Shadow_Singles_32x32/Classroom_and_Library_Singles_32x32_'
caminho_morto = 'modern interior usando/mortos/Hospital_Singles_Shadowless_32x32_'
garoto_morto = image.load(f'{caminho_morto}516.png')

objt_mapa1= {
    'quadro': image.load(f'{caminho_objt_mapa1}36.png'), 'anotacao': image.load(f'{caminho_objt_mapa1}33.png'),
    'estante': image.load(f'{caminho_objt_mapa1}57.png'), 'janela': image.load(f'modern interior usando/Room_Bulder_subfiles_32x32/1_Generic_Black_Shadow_32x32.png'),
    'cad_frente': image.load(f'{caminho_objt_mapa1}1.png'), 'mesa_prof_frente': image.load(f'{caminho_objt_mapa1}25.png'),
    'cart_vazia': image.load(f'{caminho_objt_mapa1}6.png'),'cart_casa': image.load(f'{caminho_objt_mapa1}8.png'),
    'cart_papel': image.load(f'{caminho_objt_mapa1}10.png'),'cart_livro': image.load(f'{caminho_objt_mapa1}12.png'),
    'cad_tras': image.load(f'{caminho_objt_mapa1}2.png'),'cart_estojo_lado': image.load(f'{caminho_objt_mapa1}22.png'),
    'carteira_com_livro_lado':  image.load(f'{caminho_objt_mapa1}24.png'),'cart_vazia_lado':  image.load(f'{caminho_objt_mapa1}20.png'),
    'mesa_prof_lado':  image.load(f'{caminho_objt_mapa1}29.png'),'mapa_mundi':  image.load(f'{caminho_objt_mapa1}31.png'),
    'globo':  image.load(f'{caminho_objt_mapa1}35.png'), 'quadro_lado': image.load(f'{caminho_objt_mapa1}37.png'), 
    'armario': image.load(f'{caminho_objt_mapa1}40.png'), 'estante2': image.load(f'{caminho_objt_mapa1}69.png'), 
    'placa': image.load('modern interior usando/genericos/Museum_Black_Shadow_Singles_32x32_27.png'),
    'poça de sangue 1': image.load('modern interior usando/mortos/sangue/Halloween_Shadow_Singles_32x32_79.png'),
    'poça de sangue 2': image.load('modern interior usando/mortos/sangue/Halloween_Shadow_Singles_32x32_80.png'),
    'cerebro':  image.load('modern interior usando/mortos/sangue/Halloween_Shadow_Singles_32x32_209.png'),
    'garoto_morto': transform.flip(garoto_morto, True, True), 'homem_morto': image.load(f'{caminho_morto}510.png')
}



janela_crop = (267, 1548, 72, 52)
posicoes_objetos_mapa1 = [
    (objt_mapa1['estante'], (32, 40)), (objt_mapa1['quadro'], (120, 32)), (objt_mapa1['anotacao'], (180, 50)),
    (objt_mapa1['janela'], (245, 43), janela_crop), (objt_mapa1['cad_frente'], (290, 82)), (objt_mapa1['mesa_prof_frente'], (160, 96)),
    (objt_mapa1['cart_casa'], (88, 154)), (objt_mapa1['cart_vazia'], (120, 154)), (objt_mapa1['cart_papel'], (152, 154)),
    (objt_mapa1['cart_livro'], (216, 154)), (objt_mapa1['cart_vazia'], (32, 186)), (objt_mapa1['cart_vazia'], (32, 218)),
    (objt_mapa1['cart_papel'], (120, 218)), (objt_mapa1['cart_casa'], (152, 218)), (objt_mapa1['cart_vazia'], (184, 218)),
    (objt_mapa1['cart_vazia'], (32, 250)), (objt_mapa1['cart_vazia'], (290, 250)),
    #sala2
    (objt_mapa1['poça de sangue 2'],(500,250)), (objt_mapa1['janela'], (500, 140), janela_crop), (objt_mapa1['mapa_mundi'], (590, 140)), (objt_mapa1['mesa_prof_lado'],(600,200)), 
    (objt_mapa1['quadro_lado'], (655,200)), (objt_mapa1['cart_vazia_lado'],(505,240)), (objt_mapa1['carteira_com_livro_lado'],(505,195)),
    (objt_mapa1['cart_vazia_lado'],(420,195)),(objt_mapa1['cart_estojo_lado'],(420,240)), (objt_mapa1['armario'],(130,335)), (objt_mapa1['armario'],(162,335)),
    (objt_mapa1['armario'],(194,335)), (objt_mapa1['armario'],(226,335)), (objt_mapa1['estante2'],(258,335)), (objt_mapa1['armario'],(322,335)), (objt_mapa1['armario'],(354,335)), (objt_mapa1['globo'],(600,180)),
    (objt_mapa1['armario'],(550,335)),(objt_mapa1['estante'],(582,335)),# (objt_mapa1['morto_coberto_sangue'],(90,110)),
    (objt_mapa1['placa'],(420,420)), (objt_mapa1['poça de sangue 1'],(320,440)),(objt_mapa1['poça de sangue 2'],(120,415)), #(objt_mapa1['idosa_coberta'],(120,400)),
    (objt_mapa1['cerebro'],(650,380)), (objt_mapa1['poça de sangue 1'],(210,96)),(objt_mapa1['poça de sangue 2'],(282,220)) ,#(objt_mapa1['garoto_morto'],(250,200)),
    (objt_mapa1['poça de sangue 1'],(590,290)),(objt_mapa1['cerebro'],(280,285)),(objt_mapa1['poça de sangue 1'],(650,460)),
    #(objt_mapa1['homem_morto'],(650,440))
    ]


lista_coliders_mapa1 = []
for i in range(len(mapa1)):
    for j in range(len(mapa1[i])):
        tile = mapa1[i][j]
        
        if 'p' in tile or tile == 'f' or tile in ['be', 'bd', 'cse', 'csd', 'cie', 'cid', 'bi']:
            novo_collider = Rect(tilesize * j, tilesize * i, tilesize, tilesize)
            lista_coliders_mapa1.append(novo_collider)

objetos_com_colisao_mapa1 = [
    'cad_frente', 'cart_casa', 
    'cart_vazia', 'cart_papel', 'cart_livro', 'cad_tras', 'cart_estojo_lado', 
    'carteira_com_livro_lado', 'cart_vazia_lado', 'armario','placa','mesa_prof_lado','mesa_prof_frente'
]

for item in posicoes_objetos_mapa1:
    imagem = item[0]
    posicao = item[1]
    
    for nome, img in objt_mapa1.items():
        if img == imagem and nome in objetos_com_colisao_mapa1:
            largura = imagem.get_width()
            altura = imagem.get_height()
            
            objt_collider_mapa1 = Rect(posicao[0], posicao[1], largura, altura)
            lista_coliders_mapa1.append(objt_collider_mapa1)
            break

#OBJETOS ANIMADOS
#load das imagens
door_animada = image.load('modern interior usando/escola/animated_door_big_4_32x32.png')

#variáveis:
frame_atual_porta1 = 0
frame_atual_porta2 = 0

anim_time_porta1= 0
porta1 = True
abrirPorta1 = False
fecharPorta1 = False


#MAPA 2
arq_mapa2 = open ('mapa2.txt', 'r')
mapa2 = []

mapa_supermercado = False

geraMapa(arq_mapa2,mapa2)

blocos_supermercado = {
    'cse': (192,192),
    'csd': (256,192),
    'be': (192,224),
    'bd': (256,224),
    'cie': (192,256),
    'cid': (256,256),
    'bi': (224,256),
    'pbs': (736,640),
    'pi':(736,672),
    'fcse1': (0,192),
    'fbs1': (32,192),
    'fbe1': (0,224),
    'floor1': (32,224),
    'pbes': (704,640),
    'pbds': (768,640),
    'pbei': (704,672),
    'pbdi': (768,672),
    'cursd': (128,192),
    'floor2': (32,160),
    'curse': (160,192),
    'fcse3': (128,64),
    'fbs3': (160,64),
    'fbe3': (128,96),
    'floor3':(160,96),
    'pbs2': (32,64),
    'pi2': (32,96)
    
}





#MOVIMENTAÇÃO PERSONAGEM
# Load das imagens

idle_up = image.load('Animacoes_movimentacao/Idle/Idle_Up.png')
idle_up = mudaEscala(idle_up)
idle_down = image.load('Animacoes_movimentacao/Idle/Idle_Down.png')
idle_down = mudaEscala(idle_down)

andar_up = image.load('Animacoes_movimentacao/andar/walk_Up.png')
andar_up= mudaEscala(andar_up)
andar_down = image.load('Animacoes_movimentacao/andar/walk_Down.png')
andar_down= mudaEscala(andar_down)

andar_left_up = image.load('Animacoes_movimentacao/andar/walk_Left_Up.png')
andar_left_up= mudaEscala(andar_left_up)
andar_left_down = image.load('Animacoes_movimentacao/andar/walk_Left_Down.png')
andar_left_down= mudaEscala(andar_left_down)

andar_right_up = image.load('Animacoes_movimentacao/andar/walk_Right_Up.png')
andar_right_up= mudaEscala(andar_right_up)
andar_right_down = image.load('Animacoes_movimentacao/andar/walk_Right_Down.png')
andar_right_down= mudaEscala(andar_right_down)

pulo_up = image.load('Animacoes_movimentacao/pular/Jump_Up.png')
pulo_up=mudaEscala(pulo_up)
pulo_down = image.load('Animacoes_movimentacao/pular/Jump_Down.png')
pulo_down= mudaEscala(pulo_down)
pulo_left = image.load('Animacoes_movimentacao/pular/Jump_Left_Down.png')
pulo_left=mudaEscala(pulo_left)
pulo_right = image.load('Animacoes_movimentacao/pular/Jump_Right_Down.png')
pulo_right= mudaEscala(pulo_right)

morrer_up = image.load('Animacoes_movimentacao/morrer/Death_Up.png')
morrer_up=mudaEscala(morrer_up)
morrer_down = image.load('Animacoes_movimentacao/morrer/Death_Down.png')
morrer_down=mudaEscala(morrer_down)

# Variáveis

frame_atual_idle = 0
anim_time_idle = 0

pos_x = 500
pos_y = 380
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
            if ev.key == K_o:
                abrirPorta1 = True

    clock.tick(60)
    dt = clock.get_time()
    keys = key.get_pressed()

    old_pos_x = pos_x
    old_pos_y = pos_y

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

    if telaDeInicio == True:
        desenha_telaInicio()

    if mapa_escola == True:
        desenha_mapa1()
        # desenha_gasolina(gascan_rodando,frame_atual_gascan_girando,anim_time_gascan)
        anim_time_gascan += dt
        anim_time_set = anim_time_gascan/1000

        # if gasolina == True:
        #     if anim_time_set>0.3:
        #         frame_atual_gascan_desaparecendo +=1
        #         if frame_atual_gascan_desaparecendo > len(gascan_desaparecendo):
        #             gasolina = False
        #             frame_atual_gascan_desaparecendo = 0
        #         anim_time_gascan = 0
        #     window.blit(gascan_desaparecendo[frame_atual_gascan_desaparecendo],(800,400))
                


        if anim_time_set > 0.3:
            frame_atual_gascan_girando += 1
            if frame_atual_gascan_girando > len(gascan_rodando)-1:
                frame_atual_gascan_girando = 0
            anim_time_gascan = 0
        window.blit(gascan_rodando[frame_atual_gascan_girando],(800,400))

    #MAPA 2
    if mapa_supermercado == True:
        window.fill((0,0,0))
        #MAPA SUPERMERCADO
        for i in range(len(mapa2)):
            for j in range(len(mapa2[i])):
                tile = mapa2[i][j]

                coordenada_supermercado = blocos_supermercado.get(tile)
                if tile == 'f':
                    draw.rect(window,(0,0,0),(tilesize*j, tilesize*i, tilesize, tilesize))

                elif 'p' in tile:
                    if coordenada_supermercado:
                        window.blit(tileset_parede,(tilesize * j , tilesize*i),(coordenada_supermercado[0],coordenada_supermercado[1],tilesize,tilesize))           
                elif 'f' in tile:
                    if coordenada_supermercado:
                        window.blit(tileset_floor,(tilesize * j , tilesize*i),(coordenada_supermercado[0],coordenada_supermercado[1],tilesize,tilesize))           
        
                else:
                    if coordenada_supermercado:
                        window.blit(tileset_bordas,(tilesize * j , tilesize*i),(coordenada_supermercado[0],coordenada_supermercado[1],tilesize,tilesize))



    anim_time_porta1 += dt
    anim_time_porta1_set = anim_time_porta1 / 1000

    
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
            window.blit(morrer_up, (pos_x, pos_y), ((frame_atual_morrer * 96), 0, 96, 128))
        else:
            window.blit(morrer_down, (pos_x, pos_y), ((frame_atual_morrer * 96), 0, 96, 128))

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

        window.blit(andar_up, (pos_x, pos_y + altura_pulo), ((frame_atual_walkUp * 96), 0, 96, 128))


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

        window.blit(andar_down, (pos_x, pos_y + altura_pulo), ((frame_atual_walkDown * 96), 0, 96, 128))


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
            window.blit(andar_left_up, (pos_x, pos_y + altura_pulo), ((frame_atual_walkLeft * 96), 0, 96, 128))
        else:
            window.blit(andar_left_down, (pos_x, pos_y + altura_pulo), ((frame_atual_walkLeft * 96), 0, 96, 128))


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
            window.blit(andar_right_up, (pos_x, pos_y + altura_pulo), ((frame_atual_walkRight * 96), 0, 96, 128))
        else:
            window.blit(andar_right_down, (pos_x, pos_y + altura_pulo), ((frame_atual_walkRight * 96), 0, 96, 128))


    elif pular == True:
        anim_time_pulo += dt
        anim_time_pulo_set = anim_time_pulo / 1000

        if anim_time_pulo_set > 0.09:
            frame_atual_pulo += 1
            if frame_atual_pulo > 7:
                frame_atual_pulo = 0
            anim_time_pulo = 0

        if direcao == "left":
            window.blit(pulo_left, (pos_x, pos_y + altura_pulo), ((frame_atual_pulo * 96), 0, 96, 128))

        elif direcao == "right":
            window.blit(pulo_right, (pos_x, pos_y + altura_pulo), ((frame_atual_pulo * 96), 0, 96, 128))

        elif direcao_vertical == "up":
            window.blit(pulo_up, (pos_x, pos_y + altura_pulo), ((frame_atual_pulo * 96), 0, 96, 128))

        else:
            window.blit(pulo_down, (pos_x, pos_y + altura_pulo), ((frame_atual_pulo * 96), 0, 96, 128))


    else:
        if anim_time_idle_set > 0.15:
            frame_atual_idle += 1
            if frame_atual_idle > 7:
                frame_atual_idle = 0
            anim_time_idle = 0

        if direcao_vertical == "up":
            window.blit(idle_up, (pos_x, pos_y), ((frame_atual_idle * 96), 0, 96, 128))
        else:
            window.blit(idle_down, (pos_x, pos_y), ((frame_atual_idle * 96), 0, 96, 128))

    player_collider = Rect(pos_x+40,pos_y +65,20,20)

    if mapa_escola == True:
        player_perto_p1 = (12 < pos_x < 100 and 250 < pos_y < 350) 
        

        if player_perto_p1:
        
            if anim_time_porta1_set > 0.1: 
                if frame_atual_porta1 < 5:
                    frame_atual_porta1 += 1
                anim_time_porta1 = 0
        else:

            if anim_time_porta1_set > 0.1:
                if frame_atual_porta1 > 0:
                    frame_atual_porta1 -= 1
                anim_time_porta1 = 0



        window.blit(door_animada, (64, 288), ((frame_atual_porta1 * 32), 0, 32, 96)) 

        for colisor in lista_coliders_mapa1:
            if player_collider.colliderect(colisor):
                pos_x = old_pos_x
                pos_y = old_pos_y

        
    

    

    # draw.rect(window, (0,255,0), player_collider, 2)
    

    display.update()
