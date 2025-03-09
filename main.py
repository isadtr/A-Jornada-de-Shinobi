import pygame 

print('Setup Start')
pygame.init()
window = pygame.display.set_mode(size = (600,480))
print('Setup End')


print('Loop Start')
while True:
    #check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #close window
            quit() #end pygame
