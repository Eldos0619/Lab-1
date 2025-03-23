import pygame
import random

pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 600
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Font for displaying score and level
font = pygame.font.Font(None, 36)

# Snake class
class Snake:
    def __init__(self):
        self.body = [(100, 100), (80, 100)]
        self.dx, self.dy = CELL_SIZE, 0
        self.alive = True

    def move(self):
        if not self.alive:
            return

        head_x, head_y = self.body[0]
        new_head = (head_x + self.dx, head_y + self.dy)

        # Check for wall collision
        if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
            self.alive = False  # End game if hitting a wall
            return

        # Check for self-collision
        if new_head in self.body:
            self.alive = False  # End game if hitting itself
            return

        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self):
        self.body.append(self.body[-1])  # Extend snake's length when food is eaten

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

# Food class
class Food:
    def __init__(self, snake_body):
        self.position = self.spawn_food(snake_body)

    def spawn_food(self, snake_body):
        while True:
            # Generate random food position
            x = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
            y = random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
            if (x, y) not in snake_body:  # Ensure food does not spawn on the snake
                return (x, y)

    def draw(self):
        pygame.draw.rect(screen, RED, (self.position[0], self.position[1], CELL_SIZE, CELL_SIZE))

# Main game loop
running = True
snake = Snake()
food = Food(snake.body)
clock = pygame.time.Clock()
score = 0
level = 1
FPS = 10

while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Control the snake, preventing reverse movement
            if event.key == pygame.K_LEFT and snake.dx == 0:
                snake.dx, snake.dy = -CELL_SIZE, 0
            elif event.key == pygame.K_RIGHT and snake.dx == 0:
                snake.dx, snake.dy = CELL_SIZE, 0
            elif event.key == pygame.K_UP and snake.dy == 0:
                snake.dx, snake.dy = 0, -CELL_SIZE
            elif event.key == pygame.K_DOWN and snake.dy == 0:
                snake.dx, snake.dy = 0, CELL_SIZE

    snake.move()

    # Check if the snake eats the food
    if snake.body[0] == food.position:
        snake.grow()
        score += 1
        food = Food(snake.body)

        # Level up every 3 food items
        if score % 3 == 0:
            level += 1
            FPS += 2

    # Draw game elements
    snake.draw()
    food.draw()

    # Display score and level
    score_text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)  # Control game speed

    # If the snake dies, delay for a moment and exit
    if not snake.alive:
        pygame.time.delay(1000)
        running = False

pygame.quit()