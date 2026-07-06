from pygame import *
import sys

#VARIAVEIS
tile_size = 32
frame_largura = 96
frame_altura = 128
tiles_solidos= {'be', 'bd', 'cse', 'csd', 'cie', 'cid', 'bi', 'curse', 'cursd'}
posicoes_cadeira_escola = [(88, 186), (152, 186), (216, 186), (120, 250), (152, 250), (184, 250)]

#FUNCOES
def geraMapa(mapa, listaMapa):
    for linha in mapa:
        linha_limpa = linha.strip()
        linha_mapa = linha_limpa.split(',')
        listaMapa.append(linha_mapa)


def carrega_mapa(caminho):
    mapa = []
    with open(caminho, 'r') as arquivo:
        geraMapa(arquivo, mapa)
    return mapa


def mudaEscala(animacao):
    return transform.scale(animacao, (768, 128))


def desenha_objetos(posicoes_objetos):
    for item in posicoes_objetos:
        if len(item) == 3:
            window.blit(item[0], item[1], item[2])
        else:
            window.blit(item[0], item[1])


def desenha_mapa(mapa, blocos, posicoes_objetos):
    window.fill((0, 0, 0))

    for i in range (len(mapa)):
        for j in range(len(mapa[i])):
            tile = mapa[i][j]
            coordenada = blocos.get(tile)
            x = tile_size * j
            y = tile_size * i
            area = (x, y, tile_size, tile_size)

            if tile == 'f':
                draw.rect(window, (0, 0, 0), area)
            elif 'p' in tile and coordenada:
                window.blit(tileset_parede, (x, y), (coordenada[0], coordenada[1], tile_size, tile_size))
            elif 'f' in tile and coordenada:
                window.blit(tileset_floor, (x, y), (coordenada[0], coordenada[1], tile_size, tile_size))
            elif coordenada:
                window.blit(tileset_bordas, (x, y), (coordenada[0], coordenada[1], tile_size, tile_size))

    desenha_objetos(posicoes_objetos)




def desenha_mapa1():
    desenha_mapa(mapa1, blocos_escola, posicoes_objetos_mapa1)


def desenha_mapa2():
    desenha_mapa(mapa2, blocos_supermercado, posicoes_objetos_mapa2)


def constroi_coliders(mapa, posicoes_objetos, objetos_com_colisao, objetos):
    coliders = []

    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            tile= mapa[i][j]
            if 'p' in tile or tile == 'f' or tile in tiles_solidos:
                coliders.append(Rect(tile_size * j, tile_size * i, tile_size, tile_size))

    for item in posicoes_objetos:
        imagem, posicao = item[0], item[1]
        for nome, img in objetos.items():
            if img == imagem and nome in objetos_com_colisao:
                coliders.append(Rect(posicao[0], posicao[1], imagem.get_width(), imagem.get_height()))
                break

    return coliders


def avanca_frame(anim_time, frame_atual, dt, intervalo, max_frame):
    anim_time += dt
    
    if anim_time / 1000 > intervalo:
        frame_atual += 1
        
        if frame_atual > max_frame:
            frame_atual = 0
        anim_time = 0
    return anim_time, frame_atual


def desenha_frame_anim(spritesheet, x, y, frame,mov_y):
    window.blit(
        spritesheet,
        (x, y +mov_y),
        (frame * frame_largura, 0, frame_largura, frame_altura),
    )


def colidiu_com_algum(player_collider, coliders):
    return any(player_collider.colliderect(colisor) for colisor in coliders)

def desenha_telaInicio():
    window.fill((0,0,0))
    window.blit(background,(-200,-300))
    window.blit(frame, (410,155),(749,716,279,342))
    draw.rect(window,(15, 142, 64) if bt_play.collidepoint(meu_mouse) else (23, 181, 83),bt_play)
    draw.rect(window,(175, 50, 38) if bt_sair.collidepoint(meu_mouse) else (245, 65, 47),bt_sair)

    window.blit(texto_play,(480,260))
    window.blit(texto_sair,(490,340))

def desenha_telaFinal():
    window.fill((0,0,0))
    window.blit(background,(-200,-300))
    window.blit(frame, (410,155),(749,716,279,342))
    draw.rect(window,(15, 142, 64) if bt_play.collidepoint(meu_mouse) else (23, 181, 83),bt_play)
    draw.rect(window,(175, 50, 38) if bt_sair.collidepoint(meu_mouse) else (245, 65, 47),bt_sair)

    window.blit(texto_reiniciar,(480,260))
    window.blit(texto_sair,(490,340))



init()
window = display.set_mode((1056,624))
clock = time.Clock()

#TELA DE INICIO!
tela_de_inicio = True
tela_final = False
background = image.load('background opcao.png')
frame = image.load('ui/Interface windows.png')

pixelFont = font.Font('full Pack 2025.ttf',25)
texto_play = pixelFont.render('JOGAR', True, (255,255,255))
texto_sair = pixelFont.render('SAIR', True, (255,255,255))
texto_reiniciar = pixelFont.render('REINICIAR', True, (255,255,255))

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

posicoes_gasolinas_escola = posicoes_gasolinas_escola = [
    Rect(800, 400, 32, 32),
    Rect(100, 100, 32, 32),#sala1
    Rect(600, 260, 32, 32),#sala2
    Rect(350, 410, 32, 32)
]

posicoes_gasolinas_supermercado = [
    Rect(200, 150, 32, 32),  # açougue
    Rect(500, 300, 32, 32),  
    Rect(850, 450, 32, 32)   # cestos de comida
]

#MAPA 1
mapa_escola = False
mapa1 = carrega_mapa('mapa1.txt')

tileset_parede = image.load('modern interior usando/Room_Bulder_subfiles_32x32/Room_Builder_Walls_32x32.png')
tileset_bordas = image.load('modern interior usando/Room_Bulder_subfiles_32x32/Room_Builder_borders_32x32.png')
tileset_floor = image.load('modern interior usando/Room_Bulder_subfiles_32x32/Room_Builder_floors_32x32.png')

tilesize = tile_size

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
    (objt_mapa1['armario'],(550,335)),(objt_mapa1['estante'],(582,335)),
    (objt_mapa1['placa'],(420,420)), (objt_mapa1['poça de sangue 1'],(320,440)),(objt_mapa1['poça de sangue 2'],(120,415)),
    (objt_mapa1['cerebro'],(650,380)), (objt_mapa1['poça de sangue 1'],(210,96)),(objt_mapa1['poça de sangue 2'],(282,220)) ,
    (objt_mapa1['poça de sangue 1'],(590,290)),(objt_mapa1['cerebro'],(280,285)),(objt_mapa1['poça de sangue 1'],(650,460)),
    (objt_mapa1['cad_tras'],(88,186)),(objt_mapa1['cad_tras'],(152,186)),(objt_mapa1['cad_tras'],(216,186)),(objt_mapa1['cad_tras'],(120,250)),
    (objt_mapa1['cad_tras'],(152,250)),(objt_mapa1['cad_tras'],(184,250))
    
    ]



objetos_com_colisao_mapa1 = [
    'cad_frente', 'cart_casa',
    'cart_vazia', 'cart_papel', 'cart_livro', 'cad_tras', 'cart_estojo_lado',
    'carteira_com_livro_lado', 'cart_vazia_lado', 'armario', 'placa', 'mesa_prof_lado', 'mesa_prof_frente'
]

lista_coliders_mapa1 = constroi_coliders(
    mapa1, posicoes_objetos_mapa1, objetos_com_colisao_mapa1, objt_mapa1
)

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
mapa2 = carrega_mapa('mapa2.txt')

mapa_supermercado = False
spawn_supermercado_pendente = False

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

#OBJETOS MERCADO
caminho_açougue = 'modern interior usando/supermercado/açougue/Grocery_Store_Black_Shadow_Singles_32x32_'
caminho_mercado = 'modern interior usando/supermercado/Grocery_Store_Black_Shadow_Singles_32x32_'

objt_mapa2= {
    'ralo':image.load(f'{caminho_açougue}327.png'),'gancho1': image.load(f'{caminho_açougue}319.png'),
    'gancho2':image.load(f'{caminho_açougue}322.png'),'gancho3':image.load(f'{caminho_açougue}321.png'),
    'carne1': image.load(f'{caminho_açougue}314.png'),'carne2': image.load(f'{caminho_açougue}316.png'),
    'carne3': image.load(f'{caminho_açougue}317.png'), 'carne4': image.load(f'{caminho_açougue}318.png'),
    'mesaAcougue1': image.load(f'{caminho_açougue}331.png'), 'mesaAcougue2': image.load(f'{caminho_açougue}332.png'),
    'geladeira1': image.load(f'{caminho_mercado}57.png'),'geladeira2': image.load(f'{caminho_mercado}64.png'),
    'carrinho': image.load(f'{caminho_mercado}36.png'), 'caixa_esquerda': image.load(f'{caminho_mercado}168.png'),
    'caixa_direita': image.load(f'{caminho_mercado}159.png'), 'prateleira_be': image.load(f'{caminho_mercado}76.png'),
    'prateleira_bd': image.load(f'{caminho_mercado}78.png'),'comida_prat1': image.load(f'{caminho_mercado}102.png'),
    'comida_prat2': image.load(f'{caminho_mercado}101.png'),'comida_prat3': image.load(f'{caminho_mercado}100.png'),
    'prateleira_lado': image.load(f'{caminho_mercado}114.png'),'janela_pequena': image.load(f'{caminho_mercado}156.png'),
    'janela_grande': image.load(f'{caminho_mercado}157.png'),'freezer': image.load(f'{caminho_mercado}148.png'),
    'caixa_frente1': image.load(f'{caminho_mercado}170.png'),'caixa_frente2': image.load(f'{caminho_mercado}173.png'),
    'geladeira_costas': image.load(f'modern interior usando/supermercado/Grocery_Store_Singles_Shadowless_32x32_255.png'),
    'detector_le': image.load(f'{caminho_mercado}153.png'),'detector_ld': image.load(f'{caminho_mercado}152.png'),
    'cesto_v1': image.load(f'{caminho_mercado}350.png'),
    'cesto_v2': image.load(f'{caminho_mercado}352.png'),'cesto_v3': image.load(f'{caminho_mercado}354.png'),
    'cesto_b1': image.load(f'{caminho_mercado}355.png'),'cesto_b2': image.load(f'{caminho_mercado}357.png'),'cenouras': image.load(f'{caminho_mercado}369.png'),
    'rosa': image.load(f'{caminho_mercado}365.png'),'morangos': image.load(f'{caminho_mercado}362.png'),
    'ervilhas': image.load(f'{caminho_mercado}358.png'),'bananas': image.load(f'{caminho_mercado}367.png'),



}

posicoes_objetos_mapa2 = [
    (objt_mapa2['ralo'], (160, 96)),(objt_mapa2['ralo'], (160, 150)),(objt_mapa2['ralo'], (288, 150)),
    (objt_mapa2['gancho1'], (128, 50)),(objt_mapa2['gancho3'], (160, 50)),(objt_mapa2['gancho2'], (192, 50)),
    (objt_mapa2['gancho2'], (224, 50)),(objt_mapa2['gancho3'], (256, 50)),(objt_mapa2['gancho2'], (288, 50)),
    (objt_mapa2['gancho2'], (320, 50)),(objt_mapa2['gancho3'], (352, 50)),(objt_mapa2['gancho3'], (384, 50)),
    (objt_mapa2['gancho3'], (416, 50)),(objt_mapa2['carne1'], (128, 50)),(objt_mapa2['carne2'], (160, 50)),
    (objt_mapa2['carne4'], (192, 50)),(objt_mapa2['carne3'], (224, 50)),(objt_mapa2['carne2'], (256, 50)),
    (objt_mapa2['carne3'], (320, 50)),(objt_mapa2['carne1'], (352, 50)),(objt_mapa2['carne4'], (416, 50)),
    (objt_mapa2['mesaAcougue1'], (368, 160)),(objt_mapa2['mesaAcougue2'], (384, 145)),(objt_mapa2['janela_grande'], (32, 205)),
    (objt_mapa2['janela_pequena'], (92, 205)),(objt_mapa2['geladeira1'], (64, 192)),(objt_mapa2['geladeira2'], (128, 192)),
    (objt_mapa2['janela_pequena'], (320, 205)),(objt_mapa2['janela_grande'], (384, 205)),(objt_mapa2['janela_grande'], (480, 205)),
    (objt_mapa2['prateleira_be'], (336, 192)),(objt_mapa2['comida_prat1'], (352, 192)),(objt_mapa2['prateleira_bd'], (384, 192)),
    (objt_mapa2['prateleira_be'], (400, 192)),(objt_mapa2['comida_prat2'], (416, 192)),(objt_mapa2['prateleira_bd'], (448, 192)),
    (objt_mapa2['freezer'], (512, 224)),(objt_mapa2['geladeira_costas'], (64, 352)),(objt_mapa2['geladeira_costas'], (128, 352)),
    (objt_mapa2['prateleira_be'], (304, 288)), (objt_mapa2['comida_prat3'], (320, 288)),(objt_mapa2['comida_prat1'], (352, 288)),
    (objt_mapa2['comida_prat2'], (384, 288)),(objt_mapa2['prateleira_bd'], (416, 288)),(objt_mapa2['prateleira_lado'], (432, 278)),
    (objt_mapa2['carrinho'], (228, 370)), (objt_mapa2['caixa_esquerda'], (228, 448)),(objt_mapa2['caixa_direita'], (416, 448)),
    (objt_mapa2['detector_le'], (288, 540)),(objt_mapa2['detector_ld'], (352, 540)),(objt_mapa2['janela_grande'], (600, 270)),
    (objt_mapa2['janela_pequena'], (680, 270)), (objt_mapa2['janela_grande'], (780, 270)),(objt_mapa2['janela_grande'], (880, 270)),
    (objt_mapa2['cesto_v1'], (780, 290)),(objt_mapa2['cesto_v2'], (812, 292)),(objt_mapa2['rosa'], (812, 290)),(objt_mapa2['cesto_v3'], (844, 292)),
    (objt_mapa2['bananas'], (844, 292)),(objt_mapa2['cesto_b1'], (780, 380)),(objt_mapa2['cesto_b2'], (812, 380)),
    (objt_mapa2['cenouras'], (780, 364)),(objt_mapa2['morangos'], (812, 380)),(objt_mapa2['cesto_b1'], (894, 380)),
    (objt_mapa2['ervilhas'], (894, 380)),(objt_mapa2['cesto_b2'], (926, 380)),(objt_mapa2['cenouras'], (926, 364)),
    (objt_mapa2['cesto_b2'], (812, 440)),(objt_mapa2['cesto_b1'], (780, 440)) 
]


#COLIDERS
objetos_com_colisao_mapa2 = [
    'mesaAcougue1', 'mesaAcougue2', 'geladeira1', 'geladeira2', 'geladeira_costas',
    'prateleira_be', 'prateleira_bd', 'comida_prat1', 'comida_prat2', 'comida_prat3', 'carrinho', 'caixa_esquerda',
    'caixa_direita', 'cesto_v1', 'cesto_v2', 'cesto_v3', 'cesto_b1', 'cesto_b2', 'prateleira_lado'
]

lista_coliders_mapa2 = constroi_coliders(
    mapa2, posicoes_objetos_mapa2, objetos_com_colisao_mapa2, objt_mapa2
)




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
    meu_mouse = mouse.get_pos()
    bt_play= Rect(475,250,150,50)
    bt_sair= Rect(475,330,150,50)
    
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
        if tela_de_inicio == True:
            if ev.type == MOUSEBUTTONDOWN:
                if bt_play.collidepoint(meu_mouse):
                    mapa_escola= True
                    tela_de_inicio = False
                elif bt_sair.collidepoint(meu_mouse):
                    quit()
                    sys.exit()

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

    if tela_de_inicio == True:
        desenha_telaInicio()


    if tela_de_inicio == False and tela_final == False and morrer == False:
        if chaves_andar_up:
            pos_y -= velocidade * (dt/100)
        elif chaves_andar_down:
            pos_y += velocidade * (dt/100)
        elif chaves_andar_left:
            pos_x -= velocidade * (dt/100)
        elif chaves_andar_right:
            pos_x += velocidade * (dt/100)


    player_collider = Rect(pos_x + 40, pos_y + 65, 20, 20)

   
    if tela_de_inicio == False and tela_final == False:
        if mapa_supermercado== True and spawn_supermercado_pendente== True:
                pos_x = 300
                pos_y = 550
                spawn_supermercado_pendente = False
        #ESCOLA
        if mapa_escola == True:
            desenha_mapa1()
            
            anim_time_gascan, frame_atual_gascan_girando = avanca_frame(
                anim_time_gascan, frame_atual_gascan_girando, dt, 0.3, len(gascan_rodando) - 1
            )
            
            
            gasolinas_restantes = []
            for gas_rect in posicoes_gasolinas_escola:
                if player_collider.colliderect(gas_rect):
                    #ADICIONAR PONTUAÇAO
                    continue 
                window.blit(gascan_rodando[frame_atual_gascan_girando], (gas_rect.x, gas_rect.y))
                gasolinas_restantes.append(gas_rect)
            posicoes_gasolinas_escola = gasolinas_restantes

            #troca de mapa- win condition (gasolinas coletadas)
            if len(posicoes_gasolinas_escola) == 0:
                mapa_escola = False
                mapa_supermercado = True
                spawn_supermercado_pendente = True
                
            #PORTA ABRINDO
            player_perto_p1 = (12 < pos_x < 100 and 250 < pos_y < 350)
            anim_time_porta1 += dt
            anim_time_porta1_set = anim_time_porta1 / 1000
            
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

            # Colisão Escola
            if colidiu_com_algum(player_collider, lista_coliders_mapa1):
                pos_x = old_pos_x
                pos_y = old_pos_y

       #MERCADO
        if mapa_supermercado == True:
            

            desenha_mapa2()
            
            gasolinas_restantes_mercado = []
            for gas_rect in posicoes_gasolinas_supermercado:
                
                if player_collider.colliderect(gas_rect):
                    #ADICIONAR PONTUACAO
                    continue 
               
                window.blit(gascan_rodando[frame_atual_gascan_girando], (gas_rect.x, gas_rect.y))
                gasolinas_restantes_mercado.append(gas_rect)
            posicoes_gasolinas_supermercado = gasolinas_restantes_mercado

            # Colisão mercado
            if colidiu_com_algum(player_collider, lista_coliders_mapa2):
                pos_x = old_pos_x
                pos_y = old_pos_y

    
        anim_time_idle += dt
        
        if morrer == True:
            anim_time_morrer += dt
            anim_time_morrer_set = anim_time_morrer / 1000
            if anim_time_morrer_set > 0.1:
                frame_atual_morrer += 1
                if frame_atual_morrer > 7:
                    frame_atual_morrer = 7
                anim_time_morrer = 0

            if direcao_vertical == "up":
                window.blit(morrer_up, (pos_x, pos_y), ((frame_atual_morrer * frame_largura), 0, frame_largura, frame_altura))
            else:
                window.blit(morrer_down, (pos_x, pos_y), ((frame_atual_morrer * frame_largura), 0, frame_largura, frame_altura))

        elif chaves_andar_up:
            direcao_vertical = "up"
            anim_time_walkUp, frame_atual_walkUp = avanca_frame(anim_time_walkUp, frame_atual_walkUp, dt, 0.15, 7)
            desenha_frame_anim(andar_up, pos_x, pos_y, frame_atual_walkUp, altura_pulo)

        elif chaves_andar_down:
            direcao_vertical = "down"
            anim_time_walkDown, frame_atual_walkDown = avanca_frame(anim_time_walkDown, frame_atual_walkDown, dt, 0.15, 7)
            desenha_frame_anim(andar_down, pos_x, pos_y, frame_atual_walkDown, altura_pulo)

        elif chaves_andar_left:
            direcao = "left"
            anim_time_walkLeft, frame_atual_walkLeft = avanca_frame(anim_time_walkLeft, frame_atual_walkLeft, dt, 0.15, 7)
            sprite_andar = andar_left_up if direcao_vertical == "up" else andar_left_down
            desenha_frame_anim(sprite_andar, pos_x, pos_y, frame_atual_walkLeft, altura_pulo)

        elif chaves_andar_right:
            direcao = "right"
            anim_time_walkRight, frame_atual_walkRight = avanca_frame(anim_time_walkRight, frame_atual_walkRight, dt, 0.15, 7)
            sprite_andar = andar_right_up if direcao_vertical == "up" else andar_right_down
            desenha_frame_anim(sprite_andar, pos_x, pos_y, frame_atual_walkRight, altura_pulo)

        elif pular == True:
            anim_time_pulo, frame_atual_pulo = avanca_frame(anim_time_pulo, frame_atual_pulo, dt, 0.09, 7)
            if direcao == "left":
                desenha_frame_anim(pulo_left, pos_x, pos_y, frame_atual_pulo, altura_pulo)
            elif direcao == "right":
                desenha_frame_anim(pulo_right, pos_x, pos_y, frame_atual_pulo, altura_pulo)
            elif direcao_vertical == "up":
                desenha_frame_anim(pulo_up, pos_x, pos_y, frame_atual_pulo, altura_pulo)
            else:
                desenha_frame_anim(pulo_down, pos_x, pos_y, frame_atual_pulo, altura_pulo)

        else:
            anim_time_idle, frame_atual_idle = avanca_frame(anim_time_idle, frame_atual_idle, dt, 0.15, 7)
            sprite_idle = idle_up if direcao_vertical == "up" else idle_down
            desenha_frame_anim(sprite_idle, pos_x, pos_y, frame_atual_idle, 0)

    display.update()
