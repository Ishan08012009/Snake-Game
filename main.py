import pygame
import random

# pygame.mixer.init()
# pygame.mixer.music.load('bg.mp3')

pygame.init()

# Global variable
Screen_width = 700
Screen_Height = 650
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)

# creating window
gameWindow = pygame.display.set_mode((Screen_width, Screen_Height))
pygame.display.set_caption("Snakes with Ishan")

bg_ing = pygame.image.load("bg.png")
bg_ing = pygame.transform.scale(bg_ing, (Screen_width, Screen_Height)).convert_alpha()

def Text_score(text, colour, x, y, size):
    font = pygame.font.SysFont(None, size)
    Screen_Text = font.render(text, True, colour)
    gameWindow.blit(Screen_Text, [x, y])

def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size]) 

def gameloop():
    exit_game = False
    game_over = False
    snake_x = Screen_width//2
    snake_y = Screen_Height//2
    food_x = random.randrange(10, Screen_width-10, step=10)
    food_y = random.randrange(10, Screen_Height-10, step=10)
    snake_size = 10
    x_vilocity = 0
    y_vilocity = 0
    score = 0
    clock = pygame.time.Clock()
    fps = 30
    snk_list = []
    snk_length = 1
    with open ("highscore.txt", "r") as f:
        highscore = f.read()
    # Creating gameloop
    while exit_game != True:
        if game_over == True:
        
            gameWindow.fill(white)
            Text_score(
                f"Game Over.", red, Screen_width//5,Screen_Height//2 - 20, 40)
            Text_score(
                f"Press Enter to continue", red, Screen_width//5,Screen_Height//2 + 20, 40)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        if x_vilocity != -10: 
                            x_vilocity = 10
                            y_vilocity = 0
                    elif event.key == pygame.K_DOWN:
                        if y_vilocity != -10:
                            y_vilocity = 10
                            x_vilocity = 0
                    elif event.key == pygame.K_UP:
                        if y_vilocity != 10:
                            y_vilocity = -10
                            x_vilocity = 0
                    elif event.key == pygame.K_LEFT:
                        if x_vilocity != 10:
                            x_vilocity = -10
                            y_vilocity = 0
                    elif event.key == pygame.K_q:
                        score += 10
            snake_x += x_vilocity
            snake_y += y_vilocity
            if snake_x == food_x and snake_y == food_y:
                # global score
                # pygame.mixer.music.load('point.mp3')
                # pygame.mixer.music.play()
                score += 10
                food_x = random.randrange(10, Screen_width-10, step=10)
                food_y = random.randrange(10, Screen_Height-10, step=10)
                snk_length += 5
                if score>int(highscore):
                    highscore = score
                    with open("highscore.txt", "w")as f:
                        f.write(f"{highscore}")

            gameWindow.fill(black)
            gameWindow.blit(bg_ing, (0, 0))
            # pygame.draw.rect(gameWindow, white, [snake_x, snake_y, snake_size, snake_size])
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if snake_x<0:
                snake_x = Screen_width
            if snake_y<0:
                snake_y = Screen_Height
            if snake_x>Screen_width:
                snake_x = 0
            if snake_y>Screen_Height:
                snake_y = 0

            plot_snake(gameWindow, white, snk_list, snake_size)
            Text_score(f"Score: {score}     highscore: {highscore}", red, 5, 5, 30)
            if len(snk_list)>snk_length:
                del snk_list[0]
            
            if head in snk_list[:-1]:
                # pygame.mixer.music.load('game_over.mp3')
                # pygame.mixer.music.play()
                game_over = True
        pygame.display.update()
        clock.tick(fps)


    pygame.quit()
    quit()
def welcome():
    exit_game = False
    while exit_game != True:
        gameWindow.fill(black)
        Text_score("Welcome To Snakes", red, 100, 50, 70)
        Text_score("By Ishan Gupta", red, 170, 120, 70)
        Text_score("Press any key to Continue", red, 150, 220, 50)
        snake = [pygame.image.load("snake.png"), (00, 250)]
        gameWindow.blit(snake[0], snake[1])
        clock = pygame.time.Clock()
        fps = 45
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            
            if event.type == pygame.KEYDOWN:
                gameloop()
        
        pygame.display.update()
        clock.tick(fps)
welcome()