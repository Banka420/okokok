import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))


pygame.display.set_caption("OP")
icon = pygame.image.load('football.png')
pygame.display.set_icon(icon)

iconX = 400
iconY= 300

def football(x,y):
    screen.blit(icon , (x,y))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    iconX += 0.05


    screen.fill ((0,255,0))

    football(iconX,iconY)
    pygame.display.update()