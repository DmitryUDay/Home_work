import pygame
pygame.init()
width,kolvo = height = int(input('делаем доску(МОТЕМОТИЧКУ), крч введи ширину')) 
size = (width, height)
window = pygame.display.set_mode(size)

kolvo = cols = int(input('Теперь давай напишем количество в строке кубиков'))
kvad_wid = width / kolvo


BAr = pygame.display.set_caption("Это доска")

white_color = (255, 255, 255)
black_color = (0, 0, 0)

def risual(window):
    window.fill(white_color)
    for cic in range(kolvo):
        for col in range(cic % 2, kolvo, 2):
            pygame.draw.rect(window, black_color, (col * kvad_wid, cic*kvad_wid, kvad_wid, kvad_wid))

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

    risual(window)
    pygame.display.update()

pygame.quit()