import pygame
import random

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catch the Falling Apples")

# Colours for Display
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()
FPS = 60

basket_img = pygame.image.load("basket.png")
apple_img = pygame.image.load("apple.png")
bomb_img = pygame.image.load("bomb.png")

# Resizing the images
basket_img = pygame.transform.scale(basket_img, (100, 100))
apple_img = pygame.transform.scale(apple_img, (50, 50))
bomb_img = pygame.transform.scale(bomb_img, (50, 50))

# Objects
class Basket:
    def __init__(self):
        self.image = basket_img
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speed = 10

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Apple:
    def __init__(self):
        self.image = apple_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.speedy = random.randint(5, 10)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randint(-100, -40)
            self.speedy = random.randint(5, 10)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Bomb:
    def __init__(self):
        self.image = bomb_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.speedy = random.randint(5, 10)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randint(-100, -40)
            self.speedy = random.randint(5, 10)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# Create player and object lists
player = Basket()
apples = [Apple() for i in range(5)]
bombs = [Bomb() for i in range(3)]

score = 0
lives = 3

game_over = False

# Collision detection function
def IsCollision(player, objects):
    for obj in objects:
        if player.rect.colliderect(obj.rect):
            objects.remove(obj)
            return True
    return False

def game_loop():
    global score, lives, game_over
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not game_over:
            # Update player and objects
            player.update()

            for apple in apples:
                apple.update()

            for bomb in bombs:
                bomb.update()

            if IsCollision(player, apples):
                score += 1
                apples.append(Apple())

            if IsCollision(player, bombs):
                lives -= 1
                bombs.append(Bomb())

            if lives <= 0:
                game_over = True

        screen.fill(WHITE)
        player.draw(screen)

        for apple in apples:
            apple.draw(screen)

        for bomb in bombs:
            bomb.draw(screen)

        # Display score and lives
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))
        lives_text = font.render(f"Lives: {lives}", True, BLACK)
        screen.blit(lives_text, (10, 50))

        # Display Game Over message
        if game_over:
            game_over_text = font.render("GAME OVER!", True, RED)
            screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))

        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()

# Run the game
game_loop()
