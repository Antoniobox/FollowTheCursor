import pygame
import random
import os
import urllib.request
import threading

#TODO: Usar clases para poder acceder al valor de retorno de un metodo

FPS = 30
URL_POKEAPI = 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-vii/ultra-sun-ultra-moon/'
pygame.init()

window = pygame.display.set_mode((800, 600))

def getPokemonImg():
    num_pokemon = random.randint(1, 800)
    pokemon = URL_POKEAPI + str(num_pokemon) + '.png'
    response = urllib.request.urlopen(pokemon)
    file_name = "pokemon/"+str(num_pokemon)+".png"
    urllib.request.urlretrieve(pokemon, file_name)
    return file_name

def movePokemonsToMouse(pokemons, mouse_pos, pokemon_speed = 10):
    positions = []
    pokemon_speed += 0.1
    
    for pokemon, position in pokemons:
        pokemon_rect = pokemon.get_rect(center=(position[0], position[1]))
        dx = mouse_pos[0] - position[0]
        dy = mouse_pos[1] - position[1]
        
        distance = pygame.math.Vector2(dx, dy).length()
        
        if distance > pokemon_speed:
            direction = pygame.math.Vector2(dx, dy).normalize()
            new_position = (position[0] + direction.x * pokemon_speed,
                            position[1] + direction.y * pokemon_speed)
        else:
            new_position = mouse_pos
        
        positions.append((pokemon, new_position))
    
    return positions

def checkCollision(pokemons, mouse_pos):
    mouse_rect = pygame.Rect(mouse_pos[0], mouse_pos[1], 1, 1) 
    for pokemon, position in pokemons:
        pokemon_rect = pokemon.get_rect(center=position)
        if pokemon_rect.colliderect(mouse_rect):
            return True
    return False


def createPokemon(need_reference=False, pokemon_return=None):
    pokemon_name = getPokemonImg()
    pokemon_image = pygame.image.load(pokemon_name)
    pokemon_rect = pygame.Rect(0, 0, pokemon_image.get_width(), pokemon_image.get_height())
    pokemon_rect.center = (random.randint(0, 800), random.randint(0, 600))
    if need_reference:
        pokemon_return[0] = (pokemon_image, (0, 0))
    else:
        return (pokemon_image, pokemon_rect.center)

def main():
    clock = pygame.time.Clock()
    pokemon_speed = 10
    pygame.mouse.set_visible(True)
    pokemons = []
    running = True
    pokemons.append(createPokemon())
    while running:
        pokemon_speed += 0.1
        clock.tick(FPS)
        return_pokemon = [None] * 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Elimina todas las imágenes de los Pokémon
                os.system("rm pokemon/*")
                running = False
                break
        
        window.fill(pygame.Color('white'))
        pygame.mouse.set_visible(True)
        mouse_pos = pygame.mouse.get_pos()

        
        if checkCollision(pokemons, mouse_pos):
            pokemons.append(createPokemon())
            pokemon_speed = 10
        
        pokemons = movePokemonsToMouse(pokemons, mouse_pos, pokemon_speed)
        
        for pokemon, position in pokemons:
            thread2 = threading.Thread(target=window.blit, args=(pokemon, pokemon.get_rect(center=position).topleft),)
            thread2.start()
        
        pygame.display.flip()

main()
