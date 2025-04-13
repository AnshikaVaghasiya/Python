import pygame
import random
import sys

# Initialize Pygame and Mixer
pygame.init()
pygame.mixer.init()

# Load Shooting Sound
shoot_sound = pygame.mixer.Sound("SHOOT011.mp3")
shoot_sound.set_volume(0.5)  # Optional: Set volume (0.0 to 1.0)

# Set up the screen
WIDTH, HEIGHT = 600, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

# Game settings
FPS = 60
player_speed = 6
bullet_speed = 7
enemy_speed = 2

# Fonts
font = pygame.font.SysFont("Arial", 24)

# Player setup
player = pygame.Rect(WIDTH//2 - 25, HEIGHT - 60, 50, 30)
bullets = []
enemies = []
score = 0
game_over = False

# Clock
clock = pygame.time.Clock()

def draw_window():
    win.fill(BLACK)

    if not game_over:
        pygame.draw.rect(win, CYAN, player)  # Player
        for bullet in bullets:
            pygame.draw.rect(win, YELLOW, bullet)  # Bullets
        for enemy in enemies:
            pygame.draw.ellipse(win, RED, enemy)  # Enemies

        score_text = font.render(f"Score: {score}", True, WHITE)
        win.blit(score_text, (10, 10))
    else:
        game_text = font.render("GAME OVER! Press R to Restart", True, WHITE)
        score_text = font.render(f"Final Score: {score}", True, WHITE)
        win.blit(game_text, (WIDTH//2 - 150, HEIGHT//2 - 20))
        win.blit(score_text, (WIDTH//2 - 80, HEIGHT//2 + 20))

    pygame.display.update()

def main():
    global score, bullets, enemies, game_over, player

    enemy_spawn_timer = 0
    run = True

    while run:
        clock.tick(FPS)

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if game_over and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    # Restart the game
                    player = pygame.Rect(WIDTH//2 - 25, HEIGHT - 60, 50, 30)
                    bullets.clear()
                    enemies.clear()
                    score = 0
                    game_over = False

        keys = pygame.key.get_pressed()
        if not game_over:
            if keys[pygame.K_LEFT] and player.left > 0:
                player.x -= player_speed
            if keys[pygame.K_RIGHT] and player.right < WIDTH:
                player.x += player_speed
            if keys[pygame.K_SPACE]:
                if len(bullets) < 5:
                    bullet = pygame.Rect(player.centerx - 2, player.top - 10, 4, 10)
                    bullets.append(bullet)
                    shoot_sound.play()  # 🔊 Shooting sound

        # Move bullets
        for bullet in bullets[:]:
            bullet.y -= bullet_speed
            if bullet.bottom < 0:
                bullets.remove(bullet)

        # Move enemies
        for enemy in enemies[:]:
            enemy.y += enemy_speed
            if enemy.top > HEIGHT:
                game_over = True
            for bullet in bullets[:]:
                if enemy.colliderect(bullet):
                    bullets.remove(bullet)
                    enemies.remove(enemy)
                    score += 10
                    break

        # Spawn new enemy
        enemy_spawn_timer += 1
        if enemy_spawn_timer > 60:
            x = random.randint(0, WIDTH - 30)
            enemy = pygame.Rect(x, 0, 30, 30)
            enemies.append(enemy)
            enemy_spawn_timer = 0

        draw_window()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
