import pygame, sys, random
pygame.init()
game_icon = pygame.image.load("dialogue_box.png")
resolution = displaysurf_width, displaysurf_height = (1000, 1000)
displaysurf = pygame.display.set_mode((resolution))
pygame.display.set_caption("2D Snake")
pygame.display.set_icon(game_icon)
#colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 5)
#player
player_sprite = pygame.image.load("player_sprite.png")
player_color = (3, 25, 255)
#fruit
fruit_color = (255, 2, 25)
fruit_coord_list = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400]
#enemy
enemy_ai = True
#score
score_font = pygame.font.SysFont("comicsansms", 35)
score = 0
#clock
Clock = pygame.time.Clock()


def game_loop():
    #player
    fps = Clock.get_fps()
    player_dead = False
    player_x = displaysurf_width/2
    player_y = displaysurf_height/2
    player_loc = player_x, player_y
    player_speed = 25
    player_direction = "north"
    #enemy
    enemy_move_choice_list = ["north", "south", "west", "east"]
    enemy_random_move = random.choice(enemy_move_choice_list)
    enemy_x = displaysurf_width/4
    enemy_y = displaysurf_height/4
    default_enemy_speed = 0.01
    enemy_speed = default_enemy_speed
    enemy_color = (255, 0, 15)
    #fruit
    fruit_x = random.choice(fruit_coord_list)
    fruit_y = random.choice(fruit_coord_list)
    score = 0
    while not player_dead:
        score_text = score_font.render("Score: "+str(score), True, green)
        fps_text = score_font.render(str(fps)+" FPS", True, green)
        displaysurf.fill(black)
        enemy_speed += 0.0001
        fruit_loc = fruit_x, fruit_y
        player_loc = player_x, player_y
        player_speed = 25
        enemy_speed = default_enemy_speed

        if fruit_loc == player_loc:
            pygame.draw.rect(displaysurf, black, pygame.Rect(fruit_x, fruit_y, 75, 75))
            fruit_x = random.choice(fruit_coord_list)
            fruit_y = random.choice(fruit_coord_list)
            score += 1
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    pygame.draw.rect(displaysurf, black, pygame.Rect(player_x, player_y, 75, 75))
                    player_y -= player_speed
                    player_direction = "north"
                if event.key == pygame.K_s:
                    pygame.draw.rect(displaysurf, black, pygame.Rect(player_x, player_y, 75, 75))
                    player_y += player_speed
                    player_direction = "south"
                if event.key == pygame.K_a:
                    pygame.draw.rect(displaysurf, black, pygame.Rect(player_x, player_y, 75, 75))
                    player_x -= player_speed
                    player_direction = "west"
                if event.key == pygame.K_d:
                    pygame.draw.rect(displaysurf, black, pygame.Rect(player_x, player_y, 75, 75))
                    player_x += player_speed
                    player_direction = "east"
        #enemy hard-coded movement
        if enemy_ai:
            enemy_random_move = random.choice(enemy_move_choice_list)
            if enemy_random_move == "north":
                enemy_y -= enemy_speed
            if enemy_random_move == "south":
                enemy_y += enemy_speed
            if enemy_random_move == "west":
                enemy_x -= enemy_speed
            if enemy_random_move == "east":
                enemy_x += enemy_speed

        enemy_rect = pygame.draw.rect(displaysurf, enemy_color, pygame.Rect(enemy_x, enemy_y, 100, 100))
        pygame.draw.rect(displaysurf, fruit_color, pygame.Rect(fruit_x, fruit_y, 75, 75))
        pygame.draw.rect(displaysurf, green, pygame.Rect(fruit_x+25, fruit_y+25, 25, 25))
        player_rect = pygame.draw.rect(displaysurf, player_color, pygame.Rect(player_x, player_y, 75, 75))
        if player_rect.colliderect(enemy_rect):
            player_dead = True
        if player_direction == "north":
            pygame.draw.rect(displaysurf, white, pygame.Rect(player_x, player_y, 25, 25))
            pygame.draw.rect(displaysurf, white, pygame.Rect(player_x+50, player_y, 25, 25))
        if player_direction == "south":
            pygame.draw.rect(displaysurf, white, pygame.Rect(player_x, player_y+50, 25, 25))
            pygame.draw.rect(displaysurf, white, pygame.Rect(player_x+50, player_y+50, 25, 25))
        if player_direction == "west":
            pygame.draw.rect(displaysurf, white, pygame.Rect(player_x, player_y, 25, 25))
            pygame.draw.rect(displaysurf, white, pygame.Rect(player_x, player_y+50, 25, 25))
        if player_direction == "east":
            pygame.draw.rect(displaysurf, white, pygame.Rect(player_x+50, player_y+50, 25, 25))
            pygame.draw.rect(displaysurf, white, pygame.Rect(player_x+50, player_y, 25, 25))
        displaysurf.blit(score_text, (displaysurf_width / 100, displaysurf_height / 100))
        fps = Clock.get_fps()
        fps = round(fps)
        displaysurf.blit(fps_text, (displaysurf_width / 100, displaysurf_height / 20))
        Clock.tick(60)
        displaysurf.blit(player_sprite, (player_x, player_y))
        pygame.display.update()


    displaysurf.fill(black)
    while player_dead:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        
running = True
if __name__ == "__main__":
    while running == True:
        game_loop()