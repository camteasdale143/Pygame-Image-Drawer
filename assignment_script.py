import pygame

surface = pygame.display.set_mode((500,500))
surface.fill((0, 0, 0))
# Polygon drawn with color: White, (255, 255, 255)
pygame.draw.polygon(surface, (255, 255, 255), [(203, 246), (158, 298), (174, 340), (220, 340), (269, 316), (228, 277), (203, 277)])

# Polygon drawn with color: White, (255, 255, 255)
pygame.draw.polygon(surface, (255, 255, 255), [(192, 264), (264, 112), (328, 183), (356, 216), (425, 122), (253, 58), (178, 177)])


pygame.display.update()
pygame.time.delay(3000)
pygame.image.save(surface, 'house_101147632.bmp')