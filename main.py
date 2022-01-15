import pygame
import random

# initialising pygamee
pygame.init()

# making the screen
screen = pygame.display.set_mode((800, 600))

# for setting font
base_font = pygame.font.Font(None, 32)

# setting title and logo
pygame.display.set_caption("OP")
icon = pygame.image.load('football.png')
pygame.display.set_icon(icon)

# starting position of ball (basically centre)
iconX = 400
iconY = 300


# making the football
def football(x, y):
    screen.blit(icon, (x, y))

# defining user answer
userans = ''

# making the question
n1 = random.randint(0, 100)
n2 = random.randint(0, 100)
ans1 = n1 + n2
ans1 = str(ans1)
nn1 = str(n1)
nn2 = str(n2)
nn3 = nn1 + " + " + nn2
question = ("What is " + nn3 + " ? (Press Space After Writing ans)")
print(ans1)
print(type(ans1))
print(userans)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                userans = userans[:-1]
            else:
                userans += event.unicode
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if userans == ans1:
                    userans = "CORRECT"
                else:
                    userans = "FALSE"
                    #not working




    iconX += 0.02

    # for making background green
    screen.fill((0, 255, 0))

    # for making the football appear
    football(iconX, iconY)

    # for printing the question
    questionbox = base_font.render(question , True, (0, 0, 0))
    screen.blit(questionbox, (0, 0))

    # for printing answer bar
    if iconX != 799:
        useranswertext = base_font.render(userans, True, (0, 0, 0))
        screen.blit(useranswertext, (0, 20))




    pygame.display.update()
