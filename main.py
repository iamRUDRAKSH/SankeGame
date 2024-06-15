#Snake Game
#Developer : Rudraksh Charhate

import os
import pygame
import random

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
PLAY = (204, 255, 255)
HOME = (255, 255, 153)

# Game Window
WIDTH, HEIGHT = 650, 650
gameWindow = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock
clock = pygame.time.Clock()

# Load Images
front = pygame.image.load('welcome.jpg')
front = pygame.transform.scale(front, (WIDTH, HEIGHT)).convert_alpha()
end = pygame.image.load('gameover.png')
end = pygame.transform.scale(end, (WIDTH, HEIGHT)).convert_alpha()

# Font
font = pygame.font.SysFont("Times New Roman", 24)

# Functions
def text_screen(text, color, x, y):
    """Render text on the screen."""
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])

def show_snake(gameWindow, color, snake_body, snake_size):
    """Draw the snake on the game window."""
    for x, y in snake_body:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def Home_screen():
    """Display the home screen."""
    pygame.mouse.set_visible(True)
    exit_game = False
    while not exit_game:
        gameWindow.blit(front, (0, 0))
        text_screen("Welcome to Snake Game", BLACK, 200, 0)
        text_screen("Press Shift to Play", BLACK, 230, 30)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RSHIFT:
                    Game_loop()

def Game_loop():
    """Main game loop."""
    fps = 30
    snake_size = 20
    snake_speedx = 0
    snake_speedy = 0
    vel = 10
    # Snake Position
    snake_x = 200
    snake_y = 200
    # Food Position
    food_x = 400
    food_y = 400
    score = 0
    snake_body = []
    snake_length = 1

    # Highscore Management
    if not os.path.exists("highscore.txt"):
        with open("highscore.txt", "w") as f:
            f.write("0")

    with open("highscore.txt", "r") as f:
        highscore = int(f.read())

    exit_game = False
    game_over = False
    pause = False

    while not exit_game:
        if game_over:
            pygame.mouse.set_visible(True)
            gameWindow.blit(end, (0, 0))
            text_screen("Your Score : " + str(score), BLACK, 250, 350)
            text_screen("Press Enter To Continue.", BLACK, 200, 380)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        Home_screen()
        elif pause:
            pygame.mouse.set_visible(True)
            while pause:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit_game = True
                        pause = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            pause = False
        else:
            pygame.mouse.set_visible(False)
            gameWindow.fill(PLAY)
            text_screen("Score: " + str(score), BLACK, 5, 5)
            text_screen("Highscore: " + str(highscore), BLACK, 5, 25)
            show_snake(gameWindow, GREEN, snake_body, snake_size)
            pygame.draw.rect(gameWindow, RED, [food_x, food_y, snake_size, snake_size])

            # Snake Collides with Wall
            if snake_x < 0 or snake_x > WIDTH or snake_y < 0 or snake_y > HEIGHT:
                pygame.mixer.music.load('crash.mp3')
                pygame.mixer.music.play()
                game_over = True

            Head = [snake_x, snake_y]
            snake_body.append(Head)

            if len(snake_body) > snake_length:
                del snake_body[0]

            # Snake Collides with Itself
            if Head in snake_body[:-1]:
                pygame.mixer.music.load('bite.mp3')
                pygame.mixer.music.play()
                game_over = True

            clock.tick(fps)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        snake_speedy = -vel
                        snake_speedx = 0
                    if event.key == pygame.K_DOWN:
                        snake_speedy = vel
                        snake_speedx = 0
                    if event.key == pygame.K_RIGHT:
                        snake_speedx = vel
                        snake_speedy = 0
                    if event.key == pygame.K_LEFT:
                        snake_speedx = -vel
                        snake_speedy = 0
                    if event.key == pygame.K_SPACE:
                        pause = True

            snake_x += snake_speedx
            snake_y += snake_speedy

            # Snake Eats Food
            if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) < 10:
                pygame.mixer.music.load('eat.mp3')
                pygame.mixer.music.play()
                score += 10
                food_x = random.randrange(50, WIDTH - 50, 5)
                food_y = random.randrange(50, HEIGHT - 50, 5)
                snake_length += 5
                if score > highscore:
                    highscore = score
                    with open("highscore.txt", "w") as f:
                        f.write(str(highscore))

    quit()

# Start the game
Home_screen()
