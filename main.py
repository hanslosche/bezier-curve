import pygame
import time

pygame.init()
pygame.display.set_caption("cubic bezier curve")
screenSize = (1280, 720)
screen = pygame.display.set_mode(screenSize)

x, y = 500.0, 500.0
width, height = 70, 70
speed=  0.001

font = pygame.font.Font("Bangers-Regular.ttf", 32)
position_text1 = font.render("P0", True, (255, 255, 255), (0, 0, 0))
position_text2 = font.render("P1", True, (255, 255, 255), (0, 0, 0))
position_text3 = font.render("P2", True, (255, 255, 255), (0, 0, 0))
position_text4  = font.render("P3", True, (255, 255, 255), (0, 0, 0))

textRect1 = position_text1.get_rect()
textRect2 = position_text2.get_rect()
textRect3 = position_text3.get_rect()
textRect4 = position_text4.get_rect()

path_positions = [(100.0, 600.0), (200.0, 100.0), (1000.0, 80.0), (1050, 610.0)]

t = 0
running = True

while running:
    screen.fill((0,0,0))
    pygame.time.delay(100)

    P0 = path_positions[0]
    P1 = path_positions[1]
    P2 = path_positions[2]
    P3 = path_positions[3]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    while t < 1:
        t += speed

        P0_x = pow((1-t), 3) * P0[0]
        P0_y = pow((1-t), 3) * P0[1]
        P1_x = 3 * pow((1-t), 2) * t * P1[0]
        P1_y = 3 * pow((1-t), 2) * t * P1[1]

        P2_x = 3 * (1-t) * pow(t, 2) * P2[0]
        P2_y = 3 * (1-t) * pow(t, 2) * P2[0]

        P3_x = pow(t, 3) * P3[0]
        P3_y = pow(t, 3) * P3[1]

        formular = ((P0_x + P1_x + P2_x + P3_x), (P0_y + P3_y + P2_y + P1_y))
        x,y = formular

        #display text

        textRect1.center = P0
        textRect2.center = P1
        textRect3.center = P2
        textRect4.center = P3

        screen.blit(position_text1, textRect1)
        screen.blit(position_text2, textRect2)
        screen.blit(position_text3, textRect3)
        screen.blit(position_text4, textRect4)

        #display the lines
        pygame.draw.line(screen, (0, 255, 0), P0, P1, 1)
        pygame.draw.line(screen, (0, 0, 255), P2, P3, 1)

        pygame.draw.circle(screen, (255, 255, 255), (round(x), round(y)), 1)
        pygame.display.update()


pygame.quit()
