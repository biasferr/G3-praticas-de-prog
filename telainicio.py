from pygame import *
import sys


init()
window = display.set_mode((1056,624))
clock = time.Clock()

background = image.load('background opcao.png')
frame = image.load('ui/Interface windows.png')

path_botao = 'ui/button/'
pixelFont = font.Font('full Pack 2025.ttf',25)
texto_play = pixelFont.render('JOGAR', True, (255,255,255))
texto_sair = pixelFont.render('SAIR', True, (255,255,255))


while True:
    meu_mouse = mouse.get_pos()
    bt_play= Rect(475,250,150,50)
    bt_sair= Rect(475,330,150,50)
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()
        

    
    window.fill((0,0,0))
    window.blit(background,(-200,-300))
    window.blit(frame, (410,155),(749,716,279,342))
    draw.rect(window,(15, 142, 64) if bt_play.collidepoint(meu_mouse) else (23, 181, 83),bt_play)
    draw.rect(window,(175, 50, 38) if bt_sair.collidepoint(meu_mouse) else (245, 65, 47),bt_sair)

    window.blit(texto_play,(480,260))
    window.blit(texto_sair,(490,340))

    display.update()
