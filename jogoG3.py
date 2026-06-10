from pygame import *
import sys

init()

window = display.set_mode((1056,624))

tileset_parede = image.load('Modern_Interiors/Modern tiles_Free/Old/Tileset_32x32_1.png')
tileset = image.load('Modern_Interiors/Modern tiles_Free/Old/Tileset_32x32_16.png')
tilesize = 32


mapa = [
    ['f','f','f','f'],
    ['cse', 'pbs1', 'pbs2', 'pbs1', 'pbs2', 'pbs1', 'pbs2', 'pbs1', 'pbs2','pbs1','pbs2','pbs1','pbs2','csd'],
    ['be',  'pi1',  'pi2',  'pi1',  'pi2',  'pi1',  'pi2',  'pi1',  'pi2', 'pi1', 'pi2',  'pi1', 'pi2','bd'],
    ['be', 'fcse',  'fbs',  'fbs',  'fbs',  'fbs',  'fbs',  'fbs',  'fbs', 'fbs','fbs',  'fbs', 'fbs', 'bd'],
    ['be', 'fbe', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'bd', 'f', 'cse', 'pbs1', 'pbs2', 'pbs1', 'pbs2', 'pbs1', 'pbs2', 'pbs1', 'pbs2','pbs1','pbs2','csd' ],
    ['be', 'fbe', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'bd', 'f', 'be',  'pi1',  'pi2',  'pi1',  'pi2',  'pi1',  'pi2',  'pi1',  'pi2', 'pi1', 'pi2', 'bd' ],
    ['be', 'fbe', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'bd' ],
    ['be', 'fbe', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'bd' ],
    ['be', 'fbe', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'bd' ],
    ['be', 'fbe', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'floor', 'bd' ],
    ['be', 'pbs1', 'pbs2', 'pbs1', 'pbs2', 'pbs1', 'pbs2', 'pbs1', 'pbs2','pbs1','pbs2','pbs1','pbs2', 'pbs1', 'pbs2', 'pbs1', 'pbs2', 'pbs1', 'pbs2', 'pbs1', 'pbs2', 'pbs1', 'pbs2', 'pbs1', 'pbs2', 'pbs1', 'pbs2', 'pbs1', 'pbs2', 'pbs1', 'pbs2','bd'],
    ['be',  'pi1',  'pi2',  'pi1',  'pi2',  'pi1',  'pi2',  'pi1',  'pi2', 'pi1', 'pi2',  'pi1', 'pi2', 'pi1', 'pi2', 'pi1', 'pi2', 'pi1', 'pi2', 'pi1', 'pi2', 'pi1', 'pi2', 'pi1', 'pi2', 'pi1', 'pi2', 'pi1', 'pi2', 'pi1', 'pi2','bd', ]

        ]
blocos_escola = {
    'cse': (0,32),
    'pbs1': (32,32),
    'pbs2': (64,32),
    'csd': (64,32),
    'be': (0,64),
    'pi1': (32,64),
    'pi2': (64,64),
    'bd': (64,64),
    'fcse': (32,96),
    'fbs': (64,96),
    'fbe': (32,128),
    'floor': (64,128)


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

            elif 'p' in tile or 'f' in tile:
                if coordenada_escola:
                    window.blit(tileset_parede,(tilesize * j , tilesize*i),(coordenada_escola[0],coordenada_escola[1],tilesize,tilesize))           

            else:
                if coordenada_escola:
                    window.blit(tileset,(tilesize * j , tilesize*i),(coordenada_escola[0],coordenada_escola[1],tilesize,tilesize))           

    display.update()