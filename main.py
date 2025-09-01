import pygame

print('setup Start')
pygame.init()
window = pygame.display.set_mode((600, 400))
print('setup End')

print('loop Start')
clock = pygame.time.Clock()
while True:
    # check for all eventes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #Close Window
            quit() #end pygame

