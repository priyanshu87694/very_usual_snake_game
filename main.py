import pygame
import time
import random

class Snake:
    def __init__(self, bg_screen, length):
        self.SIZE = 40
        self.bg_screen = bg_screen
        self.block = pygame.image.load('resources/block.jpg')
        # self.x, self.y = 100, 100
        self.direction = "right"
        self.length = length
        self.x = [40]*self.length
        self.y = [40]*self.length
        self.rect = self.block.get_rect()

    def draw_snake(self):
        # self.bg_screen.fill((110, 110, 5))
        # background = pygame.image.load('resources/background.jpg')
        # self.screen.blit(background, (0,0))
        for i in range(self.length):
            self.bg_screen.blit(self.block, (self.x[i], self.y[i]))

    def move_up(self):
        self.direction = "up"
    def move_down(self):
        self.direction = "down"
    def move_right(self):
        self.direction = "right"
    def move_left(self):
        self.direction = "left"


    def walk(self):
        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        if self.direction=="up":
            self.y[0] -= self.SIZE
            # pygame.display.flip()
        if self.direction=="down":
            self.y[0] += self.SIZE
            # pygame.display.flip()
        if self.direction=="right":
            self.x[0] += self.SIZE
            # pygame.display.flip()
        if self.direction=="left":
            self.x[0] -= self.SIZE
            # pygame.display.flip()

    def increase_length(self):
        self.length+=1
        self.x.append(-1)
        self.y.append(-1)

class Apple:
    def __init__(self, bg_screen):
        self.bg_screen = bg_screen
        self.apple = pygame.image.load('resources/apple.jpg')
        self.SIZE = 40
        num1, num2 = random.randint(1, 35), random.randint(1, 21)
        self.x, self.y = self.SIZE*num1, self.SIZE*num2
        self.rect = self.apple.get_rect()

    def draw_apple(self):
        self.bg_screen.blit(self.apple, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1, 35)*self.SIZE
        self.y = random.randint(1, 21)*self.SIZE


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((1440, 880))
        self.screen.fill((110, 110, 5))
        self.SIZE = 40
        self.snake = Snake(self.screen, 1)
        self.apple = Apple(self.screen)
        pygame.font.init()
        pygame.mixer.init()
        self.play_bg_music()

    def check_collision(self, x1, x2, y1, y2):
        if x1>=x2 and x1<x2+self.SIZE:
            if y1>=y2 and y1<y2+self.SIZE:
                return True
        return False

    def check_collision_screen(self, x, y):
        if x<0 or x>=1440:
            return True
        if y<0 or y>=880:
            return True
        else:
            return False

    def display_score(self):
        font = pygame.font.Font('freesansbold.ttf', 30)
        score = font.render(f'Score: {self.snake.length-1}', True, (200, 200, 200))
        self.screen.blit(score, (1300, 10))

    def game_over(self):
        time.sleep(1)
        self.screen.fill((110, 110, 5))
        font = pygame.font.Font('freesansbold.ttf', 45)
        text1 = font.render(f'Your Score: {self.snake.length-1}', True, (200, 200, 200))
        self.screen.blit(text1, (450, 350))
        text2 = font.render(f'Enter to play, Esc to exit.', True, (200, 200, 200))
        self.screen.blit(text2, (375, 400))

        pygame.mixer.music.pause()
        pygame.display.flip()

    def play_sound(self, name):
        sound = pygame.mixer.Sound(f'resources/{name}.ogg')
        pygame.mixer.Sound.play(sound)

    def play_bg_music(self):
        song = pygame.mixer.music.load('resources/bg_music_1.ogg')
        pygame.mixer.music.play()

    def play(self):
        background = pygame.image.load('resources/background.jpg')
        self.screen.blit(background, (0,0))
        self.snake.draw_snake()
        self.snake.walk()
        self.apple.draw_apple()
        if self.check_collision(self.snake.x[0], self.apple.x, self.snake.y[0], self.apple.y):
            self.play_sound('ding')
            self.apple.move()
            self.snake.increase_length()
        for i in range(3, self.snake.length):
            if self.check_collision(self.snake.x[0], self.snake.x[i], self.snake.y[0], self.snake.y[i]):
                self.play_sound('crash')
                raise "Game Over"
        if self.check_collision_screen(self.snake.x[0], self.snake.y[0]):
            self.play_sound('crash')
            raise "Game Over"
        self.display_score()
        pygame.display.flip()

    def reset(self):
        self.snake = Snake(self.screen, 1)
        self.apple = Apple(self.screen)

    def run(self):
        run = True
        pause = False
        i=0
        while run:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run = False
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        pause = False
                        pygame.mixer.music.unpause()
                        continue
                    elif event.key==pygame.K_ESCAPE:
                        run = False
                    elif event.key==pygame.K_UP:
                        self.snake.move_up()
                    elif event.key==pygame.K_DOWN:
                        self.snake.move_down()
                    elif event.key==pygame.K_RIGHT:
                        self.snake.move_right()
                    elif event.key==pygame.K_LEFT:
                        self.snake.move_left()

            try:
                if not pause:
                    self.play()
                    i+=1
            except Exception:
                self.game_over()
                pause = True
                i=0
                self.reset()
            time.sleep(0.05-(i/100000))

if __name__=="__main__":
    game = Game()
    game.run()
