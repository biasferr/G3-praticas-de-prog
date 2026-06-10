from pygame import *
import sys

init()

window = display.set_mode((1056,624))

tileset_parede = image.load('moderninteriors-win/1_Interiors/32x32/Room_Bulder_subfiles_32x32/Room_Builder_Walls_32x32.png')
tileset_bordas = image.load('moderninteriors-win/1_Interiors/32x32/Room_Bulder_subfiles_32x32/Room_Builder_borders_32x32.png')
tileset_floor = image.load('moderninteriors-win/1_Interiors/32x32/Room_Bulder_subfiles_32x32/Room_Builder_Floors_32x32.png')

tilesize = 32


mapa = [
    ['f','f','f','f'],
    ['cse', 'pbs2', 'pbs2', 'pbs2', 'pbs2', 'pbs2', 'pbs2', 'pbs2', 'pbs2','pbs2','pbs2','pbs2','pbs2','csd'],
    ['be',  'pi',  'pi',  'pi',  'pi',  'pi',  'pi',  'pi',  'pi', 'pi', 'pi',  'pi', 'pi','bd'],
    ['be', 'fcse',  'fbs',  'fbs',  'fbs',  'fbs',  'fbs',  'fbs',  'fbs', 'fbs','fbs',  'fbs', 'fbs', 'bd'],
    ['be', 'fbe', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'bd', 'f', 'cse', 'pbs2', 'pbs2', 'pbs2', 'pbs2', 'pbs2', 'pbs2', 'pbs2', 'pbs2','pbs2','pbs2','csd' ],
    ['be', 'fbe', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'bd', 'f', 'be',  'pi',  'pi',  'pi',  'pi',  'pi',  'pi',  'pi',  'pi', 'pi', 'pi', 'bd' ],
    ['be', 'fbe', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'bd', 'f', 'be', 'fcse', 'fbs', 'fbs', 'fbs', 'fbs', 'fbs', 'fbs', 'fbs', 'fbs', 'fbs', 'bd'],
    ['be', 'fbe', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'bd', 'f', 'be', 'fbe', 'floor','floor','floor','floor','floor','floor','floor','floor','floor','bd'],
    ['be', 'fbe', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'bd', 'f', 'be', 'fbe', 'floor','floor','floor','floor','floor','floor','floor','floor','floor','bd' ],
    ['be', 'fbe', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'bd', 'f', 'be', 'fbe', 'floor','floor','floor','floor','floor','floor','floor','floor','floor','bd' ],
    ['be', 'pbs2', 'pbs2', 'pbs2', 'pbs2', 'pbs2', 'pbs2', 'pbs2', 'pbs2','pbs2','pbs2','pbs2','pbs2', 'pbs2', 'pbs2', 'pbs2', 'pbs2', 'pbs2', 'pbs2', 'pbs2', 'pbs2', 'pbs2', 'pbs2', 'pbs2', 'pbs2', 'pbs2', 'pbs2', 'pbs2', 'pbs2', 'pbs2', 'pbs2','csd'],
    ['be',  'pi',  'pi',  'pi',  'pi',  'pi',  'pi',  'pi',  'pi', 'pi', 'pi',  'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi','bd', ],
    ['be', 'fcse',  'fbs',  'fbs',  'fbs',  'fbs',  'fbs',  'fbs',  'fbs', 'fbs','fbs',  'fbs', 'fbs','fbs',  'fbs',  'fbs',  'fbs',  'fbs',  'fbs',  'fbs',  'fbs', 'fbs','fbs',  'fbs', 'fbs','fbs',  'fbs',  'fbs',  'fbs',  'fbs',  'fbs','bd'],
    ['be', 'fbe',  'floor',  'floor',  'floor',  'floor',  'floor',  'floor',  'floor', 'floor','floor',  'floor', 'floor','floor',  'floor',  'floor',  'floor',  'floor',  'floor',  'floor',  'floor', 'floor','floor',  'floor', 'floor','floor',  'floor',  'floor',  'floor',  'floor',  'floor','bd'],
    ['be', 'fbe',  'floor',  'floor',  'floor',  'floor',  'floor',  'floor',  'floor', 'floor','floor',  'floor', 'floor','floor',  'floor',  'floor',  'floor',  'floor',  'floor',  'floor',  'floor', 'floor','floor',  'floor', 'floor','floor',  'floor',  'floor',  'floor',  'floor',  'floor','bd'],
    ['cie','bi', 'bi', 'bi', 'bi', 'bi','bi','bi','bi','bi','bi','bi','bi','bi','bi','bi','bi','bi','bi','bi','bi','bi','bi','bi','bi','bi','bi','bi','bi','bi','bi','cid']
        ]
blocos_escola = {
    'cse': (192,192),
    'pbs1': (0,576),
    'pbs2': (32,576),
    'csd': (256,192),
    'be': (192,224),
    'pi': (32,608),
    'bd': (256,224),
    'fcse': (0,640),
    'fbs': (32,640),
    'fbe': (0,672),
    'floor': (32,672),
    'cie': (192,256),
    'cid': (256,256),
    'bi': (224,256)


}


while True:
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()


    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            tile = mapa[i][j]

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

    display.update()
