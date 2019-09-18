import pygame

surface = pygame.display.set_mode((500,500))
surface.fill((0, 0, 0))
#Rectangle drawn with color:  Nebula Green - (89, 232, 23, 255)
pygame.draw.rect(surface, (89, 232, 23, 255), pygame.Rect(133 - 50, 145, 377, 387))

#Rectangle drawn with color:  Lemon Chiffon - (255, 248, 198, 255)
pygame.draw.rect(surface, (255, 248, 198, 255), pygame.Rect(139 - 50, 284, 29, 27))

#Rectangle drawn with color:  Lemon Chiffon - (255, 248, 198, 255)
pygame.draw.rect(surface, (255, 248, 198, 255), pygame.Rect(246 - 50, 303, 61, 40))

#Rectangle drawn with color:  Blonde - (251, 246, 217, 255)
pygame.draw.rect(surface, (251, 246, 217, 255), pygame.Rect(199 - 50, 355, 41, 134))

#Circle drawn with color:  Blue Dress - (21, 125, 236, 255)
pygame.draw.circle(surface, (21, 125, 236, 255), (404, 97), 84)


pygame.display.update()
pygame.time.delay(3000)
pygame.image.save(surface, 'house_101147632.bmp')