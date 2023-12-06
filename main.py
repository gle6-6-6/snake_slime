import pygame
import sys
import random

FRAME_COLOR = (144, 238, 144)
WHITE = (255, 255, 255)
GREEN = (202, 252, 202)
RED = (244, 0, 0)
MARGIN = 1
SIZE_BLOCK = 20
COUNT_BLOCKS = 20
HEADER_MARGIN = 70
COLOR_HEADER = (80, 200, 120)
SNAKE_COLOR = (255, 117, 20)

size = [SIZE_BLOCK * COUNT_BLOCKS + 2 * SIZE_BLOCK + MARGIN * COUNT_BLOCKS,
        SIZE_BLOCK * COUNT_BLOCKS + 2 * SIZE_BLOCK + MARGIN * COUNT_BLOCKS + HEADER_MARGIN]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Python Snake')
timer = pygame.time.Clock()
time

class Snakeblock():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_inside(self):
        return 0 <= self.x < COUNT_BLOCKS and 0 <= self.y < COUNT_BLOCKS

    def __eq__(self, other):
        return isinstance(other, Snakeblock) and self.x == other.x and self.y == other.y


def get_random():
    x = random.randint(0, COUNT_BLOCKS - 1)
    y = random.randint(0, COUNT_BLOCKS - 1)
    empty_block = Snakeblock(x, y)
    while empty_block in snake_blocks:
        empty_block.x = random.randint(0, COUNT_BLOCKS - 1)
        empty_block.y = random.randint(0, COUNT_BLOCKS - 1)
    return empty_block


def draw_block(color, column, row):
    pygame.draw.rect(screen, color, [SIZE_BLOCK + column * SIZE_BLOCK + MARGIN * (column + 1),
                                     HEADER_MARGIN + SIZE_BLOCK + row * SIZE_BLOCK + MARGIN * (row + 1), SIZE_BLOCK,
                                     SIZE_BLOCK])


snake_blocks = [Snakeblock(9, 8), Snakeblock(9, 9), Snakeblock(9, 10)]
apple = get_random()

d_row = buf_row = 1
d_col = buf_col = 0
total = 0
speed = 0

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            print("exit")
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and d_col != 0:
                buf_row = -1
                buf_col = 0
            elif event.key == pygame.K_DOWN and d_col != 0:
                buf_row = 1
                buf_col = 0
            elif event.key == pygame.K_RIGHT and d_row != 0:
                buf_row = 0
                buf_col = 1
            elif event.key == pygame.K_LEFT and d_row != 0:
                buf_row = 0
                buf_col = -1

    screen.fill(FRAME_COLOR)

    pygame.draw.rect(screen, COLOR_HEADER, [0, 0, size[0], HEADER_MARGIN])

    for row in range(COUNT_BLOCKS):
        for column in range(COUNT_BLOCKS):
            if (column + row) % 2 == 0:
                color = WHITE
            else:
                color = GREEN
            draw_block(color, row, column)

    head = snake_blocks[-1]
    if not head.is_inside():
        pygame.quit()
        print("crash")
        sys.exit()
    for block in snake_blocks:
        draw_block(SNAKE_COLOR, block.x, block.y)

    draw_block(RED, apple.x, apple.y)
    pygame.display.flip()
    if apple == head:
        total += 1
        speed += total // 5 + 1
        snake_blocks.append(apple)
        apple = get_random()

    d_col = buf_col
    d_row = buf_row
    new_head = Snakeblock(head.x + d_col, head.y + d_row)
    if new_head in snake_blocks:
        pygame.quit()
        print("crash yourself")
        sys.exit()

    snake_blocks.append(new_head)
    snake_blocks.pop(0)

    timer.tick(3 + speed)
