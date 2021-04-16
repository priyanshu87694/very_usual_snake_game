import pygame


class Snake:
    def __init__(self, bg_screen):
        self.bg_screen = bg_screen
        self.block = pygame.image.load('resources/block.jpg')
        self.x, self.y = 0, 0

    def draw_snake(self):
        self.bg_screen.fill((110, 110, 5))
        self.bg_screen.blit(self.block, (self.x, self.y))
        # pygame.display.flip()

    def move_up(self):
        self.y -= 10
        pygame.display.flip()
    def move_down(self):
        self.y += 10
        pygame.display.flip()
    def move_right(self):
        self.x += 10
        pygame.display.flip()
    def move_left(self):
        self.x -= 10
        pygame.display.flip()

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((1000, 500))
        self.screen.fill((110, 110, 5))
        self.snake = Snake(self.screen)
    
    def run(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run = False
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_UP:
                        self.snake.move_up()
                    elif event.key==pygame.K_DOWN:
                        self.snake.move_down()
                    elif event.key==pygame.K_RIGHT:
                        self.snake.move_right()
                    elif event.key==pygame.K_LEFT:
                        self.snake.move_left()

            self.snake.draw_snake()
            pygame.display.flip()

if __name__=="__main__":
    game = Game()
    game.run()