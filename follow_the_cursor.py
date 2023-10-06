import pygame

pygame.init()

window = pygame.display.set_mode((800, 600))

def main():
    clock = pygame.time.Clock()
    running = True
    mouse_pos = pygame.mouse.get_pos()
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        window.fill((255, 255, 255))
        if pygame.mouse.get_focused():
           mouse_pos = pygame.mouse.get_pos()
        pygame.display.flip()

main()