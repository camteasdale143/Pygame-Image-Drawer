import pygame

surface = pygame.display.set_mode((500,500))
surface.fill((127, 90, 88, 255))
#Rectangle drawn with color: White
pygame.draw.rect(surface, (255, 255, 255), pygame.Rect(62, 211, 0, 0))

#Rectangle drawn with color: White
pygame.draw.rect(surface, (255, 255, 255), pygame.Rect(254, 81, 60, -5))

#Rectangle drawn with color: White
pygame.draw.rect(surface, (255, 255, 255), pygame.Rect(437, 77, 0, 0))

#Rectangle drawn with color: White
pygame.draw.rect(surface, (255, 255, 255), pygame.Rect(440, 207, 0, 0))

#Rectangle drawn with color: White
pygame.draw.rect(surface, (255, 255, 255), pygame.Rect(233, 110, 230, 155))

#Rectangle drawn with color:  Lemon Chiffon
pygame.draw.rect(surface, (255, 248, 198, 255), pygame.Rect(136, 122, 148, 78))

#Ellipse drawn with color:  Lemon Chiffon
pygame.draw.ellipse(surface, (255, 248, 198, 255), pygame.Rect(136, 97, 186, 54))

#Circle drawn with color:  Coffee
pygame.draw.circle(surface, (111, 78, 55, 255), (49, 240), 31)


pygame.display.update()
pygame.time.delay(3000)
pygame.image.save(surface, 'house_101147632.bmp')