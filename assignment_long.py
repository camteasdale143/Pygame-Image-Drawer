import pygame

surface = pygame.display.set_mode((500,500))
surface.fill((125, 5, 65, 255))
#Rectangle drawn with color: White
pygame.draw.rect(surface, (255, 255, 255), pygame.Rect(145, 120, 151, 141))

#Ellipse drawn with color: White
pygame.draw.ellipse(surface, (255, 255, 255), pygame.Rect(193, 181, 168, 91))

#Ellipse drawn with color:  Brown Sugar
pygame.draw.ellipse(surface, (226, 167, 111, 255), pygame.Rect(256, 227, 185, 123))

#Rectangle drawn with color:  Orange Salmon
pygame.draw.rect(surface, (196, 116, 81, 255), pygame.Rect(259, 470, 1, 1))

#Rectangle drawn with color:  Orange Salmon
pygame.draw.rect(surface, (196, 116, 81, 255), pygame.Rect(70, 227, 1, 1))

#Rectangle drawn with color:  Orange Salmon
pygame.draw.rect(surface, (196, 116, 81, 255), pygame.Rect(199, 134, 1, 1))

#Rectangle drawn with color:  Orange Salmon
pygame.draw.rect(surface, (196, 116, 81, 255), pygame.Rect(291, 285, 1, 1))

#Rectangle drawn with color:  Orange Salmon
pygame.draw.polygon(surface, (196, 116, 81, 255), [(259, 470), (70, 227), (199, 134), (291, 285)])


pygame.display.update()
pygame.time.delay(3000)
pygame.image.save(surface, 'house_101147632.bmp')