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
player_dead = False
player_color = (3, 25, 255)
#fruit
fruit_color = (255, 2, 25)
fruit_coord_list = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400]
#score
score_font = pygame.font.SysFont("comicsansms", 35)
score = 0

def game_loop():
    #player
    player_x = displaysurf_width/2
    player_y = displaysurf_height/2
    player_loc = player_x, player_y
    player_speed = 25
    player_direction = "north"
    #fruit
    fruit_x = random.choice(fruit_coord_list)
    fruit_y = random.choice(fruit_coord_list)
    score = 0
    while not player_dead:
        displaysurf.fill(black)
        score_text = score_font.render("Score: "+str(score), True, green)
        fruit_loc = fruit_x, fruit_y
        player_loc = player_x, player_y
        player_speed = 25

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
        pygame.draw.rect(displaysurf, fruit_color, pygame.Rect(fruit_x, fruit_y, 75, 75))
        pygame.draw.rect(displaysurf, green, pygame.Rect(fruit_x+25, fruit_y+25, 25, 25))
        pygame.draw.rect(displaysurf, player_color, pygame.Rect(player_x, player_y, 75, 75))
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
        pygame.display.update()
    while player_dead:
        pass

running = True
if __name__ == "__main__":
    while running == True:
        game_loop()
        pygame.display.update()