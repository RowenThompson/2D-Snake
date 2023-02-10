import pygame, sys, random
from map import *
pygame.init()
game_icon = pygame.image.load("game_icon.png")
resolution = displaysurf_width, displaysurf_height = (1000, 1000)
displaysurf = pygame.display.set_mode((resolution))
pygame.display.set_caption("2D Snake Fight")
pygame.display.set_icon(game_icon)
#colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 5)
#player
player_sprite = pygame.image.load("player_sprite.png")
player_sprite = pygame.transform.scale(player_sprite, (100, 100))
player_color = (3, 25, 255)
#enemy
enemy_ai = True
#score and font
font = pygame.font.SysFont("comicsansms", 35)
#clock
Clock = pygame.time.Clock()

map1 = """




































ggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg



ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd



ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd"""

map1 = map1.splitlines()

for line in map1:
    print(line)

grass_tile = pygame.image.load("grass_tile.png")
grass_tile = pygame.transform.scale(grass_tile, (75, 75))

dirt_tile = pygame.image.load("dirt_tile.png")
dirt_tile = pygame.transform.scale(dirt_tile, (75, 75))

def tiles(map1):
    global grass_tile
    for y, line in enumerate(map1):
        for x, c in enumerate(line):
            if c == "g":
                displaysurf.blit(grass_tile, (x * 16, y * 16))
            if c == "d":
                displaysurf.blit(dirt_tile, (x * 16, y * 16))

def quit_game():
    pygame.quit()
    sys.exit()

def game_loop():
    #gravity
    player_y_gravity = 1
    player_jump_height = 20
    player_y_velocity = player_jump_height
    #player
    player_jumping = False
    player_dead = False
    player_x = displaysurf_width/2
    player_y = displaysurf_height/2
    player_loc = player_x, player_y
    player_speed = 5
    player_direction = "west"
    player_rect = displaysurf.blit(player_sprite, (player_x, player_y))
    #enemy
    enemy_move_choice_list = ["north", "south", "west", "east"]
    enemy_random_move = random.choice(enemy_move_choice_list)
    enemy_x = displaysurf_width/4
    enemy_y = displaysurf_height/4
    default_enemy_speed = 0.01
    enemy_speed = default_enemy_speed
    enemy_color = (255, 0, 15)
    #fps
    fps = Clock.get_fps()
    while not player_dead:
        fps_text = font.render(str(fps)+" FPS", True, green)
        displaysurf.fill(black)
        enemy_speed += 0.0001
        player_loc = player_x, player_y
        enemy_speed = default_enemy_speed
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        player_x += (keys[pygame.K_d] - keys[pygame.K_a]) * player_speed
        if keys[pygame.K_w]:
            player_jumping = True
        if not player_jumping:
            player_rect = displaysurf.blit(player_sprite, (player_x, player_y))
        if player_jumping:
            player_y -= player_y_velocity
            player_y_velocity -= player_y_gravity
            if player_y_velocity < -player_jump_height:
                player_jumping = False
                player_y_velocity = player_jump_height
            player_rect = displaysurf.blit(player_sprite, (player_x, player_y))
        fps = Clock.get_fps()
        fps = round(fps)
        displaysurf.blit(fps_text, (displaysurf_width / 100, displaysurf_height / 100))
        tiles(map1)
        Clock.tick(60)
        pygame.display.update()


    displaysurf.fill(black)
    while player_dead:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
        pygame.display.update()
        
running = True
if __name__ == "__main__":
    while running == True:
        game_loop()
quit_game()