from pygame import *
import sys

init()
window = display.set_mode((1056,624))

background = image.load('background opcao.png')
frame = image.load('ui/Interface windows.png')
pixelFont = font.Font('full Pack 2025.ttf',25)
fontee = font.Font('Pixeled.ttf',35)
fontee_pequena = font.Font('Pixeled.ttf',20)
texto_reiniciar = pixelFont.render('REINICIAR',True,(255,255,255))
texto_sair = pixelFont.render('SAIR',True,(255,255,255))
texto_venceu = fontee.render('VOCE VENCEU!',True, (255,255,255))
sombra_texto_venceu = fontee.render('VOCE VENCEU!',True, (61, 61, 61))

texto_perdeu = fontee.render('VOCE PERDEU!',True, (255,255,255))
sombra_texto_perdeu = fontee.render('VOCE PERDEU!',True, (61, 61, 61))

gasolina_parada = image.load('objectss/gas can rotations/south.png')

n_gasolinas= 3


vencer = False
perder = True

while True:
    meu_mouse = mouse.get_pos()
    bt_reiniciar= Rect(460,230,180,50)
    bt_sair2= Rect(475,290,150,50)
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()

    window.fill((0,0,0))
    window.blit(background,(-200,-300))
    window.blit(frame, (410,155),(749,716,279,342))
    draw.rect(window,(15, 142, 64) if bt_play.collidepoint(meu_mouse) else (23, 181, 83),bt_play)
    draw.rect(window,(175, 50, 38) if bt_sair.collidepoint(meu_mouse) else (245, 65, 47),bt_sair)

    window.blit(texto_reiniciar,(460,240))
    window.blit(texto_sair,(500,300))

    window.blit(gasolina_parada, (450,370))
    texto_x = fontee_pequena.render(f'X {n_gasolinas}',True, (255,255,255))
    window.blit(texto_x, (500,360))
  

    if vencer == True:
        window.blit(sombra_texto_venceu, (355,73))
        window.blit(texto_venceu, (350,70))
        
    elif perder == True:
        window.blit(sombra_texto_perdeu, (355,73))
        window.blit(texto_perdeu, (350,70))

    display.update()