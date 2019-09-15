import pygame

surface = pygame.display.set_mode((500,500))
surface.fill((0, 0, 0))
#Circle drawn with color: White
pygame.draw.circle(surface, (255, 255, 255), (247, 240), 267)


pygame.display.update()
pygame.time.delay(3000)
pygame.image.save(surface, 'house_101147632.bmp')