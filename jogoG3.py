from pygame import *
import sys


def geraMapa(mapa,listaMapa):
    for linha in mapa:
        linha_limpa = linha.strip()
        linha_mapa = linha_limpa.split(',')
        listaMapa.append(linha_mapa)

arq_mapa1 = open ('mapa1.txt', 'r')
mapa1 = []  

init()

window = display.set_mode((1056,624))

tileset_parede = image.load('modern interior usando/Room_Bulder_subfiles_32x32/Room_Builder_Walls_32x32.png')
tileset_bordas = image.load('modern interior usando/Room_Bulder_subfiles_32x32/Room_Builder_borders_32x32.png')
tileset_floor = image.load('modern interior usando/Room_Bulder_subfiles_32x32/Room_Builder_floors_32x32.png')

tilesize = 32

geraMapa(arq_mapa1,mapa1)
print(mapa1)


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
caminho_obj = 'modern interior usando/escola/5_Classroom_and_Library_Black_Shadow_Singles_32x32/Classroom_and_Library_Singles_32x32_'
caminho_morto = 'modern interior usando/mortos/Hospital_Singles_Shadowless_32x32_'
garoto_morto = image.load(f'{caminho_morto}516.png')

obj= {
    'quadro': image.load(f'{caminho_obj}36.png'), 'anotacao': image.load(f'{caminho_obj}33.png'),
    'estante': image.load(f'{caminho_obj}57.png'), 'janela': image.load(f'modern interior usando/Room_Bulder_subfiles_32x32/1_Generic_Black_Shadow_32x32.png'),
    'cad_frente': image.load(f'{caminho_obj}1.png'), 'mesa_prof_frente': image.load(f'{caminho_obj}25.png'),
    'cart_vazia': image.load(f'{caminho_obj}6.png'),'cart_casa': image.load(f'{caminho_obj}8.png'),
    'cart_papel': image.load(f'{caminho_obj}10.png'),'cart_livro': image.load(f'{caminho_obj}12.png'),
    'cad_tras': image.load(f'{caminho_obj}2.png'),'cart_estojo_lado': image.load(f'{caminho_obj}22.png'),
    'carteira_com_livro_lado':  image.load(f'{caminho_obj}24.png'),'cart_vazia_lado':  image.load(f'{caminho_obj}20.png'),
    'mesa_prof_lado':  image.load(f'{caminho_obj}29.png'),'mapa_mundi':  image.load(f'{caminho_obj}31.png'),
    'globo':  image.load(f'{caminho_obj}35.png'), 'quadro_lado': image.load(f'{caminho_obj}37.png'), 
    'armario': image.load(f'{caminho_obj}40.png'), 'estante2': image.load(f'{caminho_obj}69.png'), 
    'placa': image.load('modern interior usando/genericos/Museum_Black_Shadow_Singles_32x32_27.png'),
    #mortos
    'morto_coberto_sangue': image.load(f'{caminho_morto}518.png'), 'idosa_coberta': image.load(f'{caminho_morto}513.png'),
    #sangue
    'poça de sangue 1': image.load('modern interior usando/mortos/sangue/Halloween_Shadow_Singles_32x32_79.png'),
    'poça de sangue 2': image.load('modern interior usando/mortos/sangue/Halloween_Shadow_Singles_32x32_80.png'),
    'cerebro':  image.load('modern interior usando/mortos/sangue/Halloween_Shadow_Singles_32x32_209.png'),
    'garoto_morto': transform.flip(garoto_morto, True, True), 'homem_morto': image.load(f'{caminho_morto}510.png')
}



janela_crop = (267, 1548, 72, 52)
posicoes_objetos = [
    (obj['estante'], (32, 40)), (obj['quadro'], (120, 32)), (obj['anotacao'], (180, 50)),
    (obj['janela'], (245, 43), janela_crop), (obj['cad_frente'], (290, 82)), (obj['mesa_prof_frente'], (160, 96)),
    (obj['cart_casa'], (88, 154)), (obj['cart_vazia'], (120, 154)), (obj['cart_papel'], (152, 154)),
    (obj['cart_livro'], (216, 154)), (obj['cart_vazia'], (32, 186)), (obj['cart_vazia'], (32, 218)),
    (obj['cart_papel'], (120, 218)), (obj['cart_casa'], (152, 218)), (obj['cart_vazia'], (184, 218)),
    (obj['cart_vazia'], (32, 250)), (obj['cart_vazia'], (290, 250)),
    #sala2
    (obj['poça de sangue 2'],(500,250)), (obj['janela'], (500, 140), janela_crop), (obj['mapa_mundi'], (590, 140)), (obj['mesa_prof_lado'],(600,200)), 
    (obj['quadro_lado'], (655,200)), (obj['cart_vazia_lado'],(505,255)), (obj['carteira_com_livro_lado'],(505,195)),
    (obj['cart_vazia_lado'],(420,195)),(obj['cart_estojo_lado'],(420,255)), (obj['armario'],(130,335)), (obj['armario'],(162,335)),
    (obj['armario'],(194,335)), (obj['armario'],(226,335)), (obj['estante2'],(258,335)), (obj['armario'],(322,335)), (obj['armario'],(354,335)), (obj['globo'],(600,180)),
    (obj['armario'],(550,335)),(obj['estante'],(582,335)), (obj['morto_coberto_sangue'],(90,110)),
    (obj['placa'],(420,420)), (obj['poça de sangue 1'],(320,440)),(obj['poça de sangue 2'],(120,415)), (obj['idosa_coberta'],(120,400)),
    (obj['cerebro'],(650,380)), (obj['poça de sangue 1'],(210,96)),(obj['poça de sangue 2'],(282,220)) ,(obj['garoto_morto'],(250,200)),
    (obj['poça de sangue 1'],(590,290)),(obj['cerebro'],(280,285)),(obj['poça de sangue 1'],(650,460)),
    (obj['homem_morto'],(650,440))
    ]


lista_colliders = []
for i in range(len(mapa1)):
    for j in range(len(mapa1[i])):
        tile = mapa1[i][j]
        
        if 'p' in tile or tile == 'f' or tile in ['be', 'bd', 'cse', 'csd', 'cie', 'cid', 'bi']:
            # Cria um retângulo na posição exata do tile
            novo_collider = Rect(tilesize * j, tilesize * i, tilesize, tilesize)
            lista_colliders.append(novo_collider)

objetos_com_colisao = [
    'cad_frente', 'cart_casa', 
    'cart_vazia', 'cart_papel', 'cart_livro', 'cad_tras', 'cart_estojo_lado', 
    'carteira_com_livro_lado', 'cart_vazia_lado', 'armario','placa','mesa_prof_lado','mesa_prof_frente'
]

for item in posicoes_objetos:
    imagem = item[0]
    posicao = item[1]
    
    for nome, img in obj.items():
        if img == imagem and nome in objetos_com_colisao:
            largura = imagem.get_width()
            altura = imagem.get_height()
            
            obj_collider = Rect(posicao[0], posicao[1], largura, altura)
            lista_colliders.append(obj_collider)
            break




while True:
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()



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
    for item in posicoes_objetos:
        if len(item) == 3: 
            window.blit(item[0], item[1], item[2])
        else:
            window.blit(item[0], item[1])
    
    window.blit(obj['cad_tras'],(88,186))
    window.blit(obj['cad_tras'],(152,186))
    window.blit(obj['cad_tras'],(216,186))
    window.blit(obj['cad_tras'],(120,250))
    window.blit(obj['cad_tras'],(152,250))
    window.blit(obj['cad_tras'],(184,250))
    
    
    #APAGAR DPS
    for colisor in lista_colliders:
        draw.rect(window, (255, 0, 0), colisor, 2)
    

    #for colisor in lista_colisores:
        #if jogador_rect.colliderect(colisor):


    display.update()
