import urllib.request
import json
import pygame
import random
import os

FPS = 60

pygame.init()

window = pygame.display.set_mode((800, 600))

def getPokemonImg():
    num_pokemon = random.randint(1, 800)
    pokemon = 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/' + str(num_pokemon) + '.png'
    response = urllib.request.urlopen(pokemon)
    file_name = "pokemon/"+str(num_pokemon)+".png"
    urllib.request.urlretrieve(pokemon, file_name)
    return file_name

pokemon_name = getPokemonImg()
pokemon = pygame.image.load(pokemon_name)

def main():
    clock = pygame.time.Clock()
    running = True
    mouse_pos = pygame.mouse.get_pos()
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #Elimina todas las imagenes de los pokemon
                ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
                os.system("rm " + pokemon_name)
                running = False
        window.fill(pygame.Color('white'))
        if pygame.mouse.get_focused():
           mouse_pos = pygame.mouse.get_pos()
        window.blit(pokemon, (0, 0))
        pygame.display.flip()

main()


