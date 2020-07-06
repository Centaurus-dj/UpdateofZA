
#label pygame:
#    init python:
#        import pygame
#        import sys


#        pygame.init()

#        screen = pygame.display.set_mode((1280,720))

#android-icon_foreground.png        black = 0, 0, 0

#        import sys, pygame
#        pygame.init()

#        size = width, height = 320, 240
#        speed = [2, 2]
#        black = 0, 0, 0

#        screen = pygame.display.set_mode(size)

#        balle = pygame.image.load("balle.png")
#        ballerect = balle.get_rect()

#        while 1:
#            for event in pygame.event.get():
#                if event.type == pygame.QUIT: sys.exit()

#            ballerect = ballerect.move(speed)

#            if ballerect.left < 0 or ballerect.right > width:
#                speed[0] = -speed[0]

#            if ballerect.top < 0 or ballerect.bottom > height:
#                speed[1] = -speed[1]

#                screen.fill(black)
#                screen.blit(balle, ballerect)
#                pygame.display.flip()
