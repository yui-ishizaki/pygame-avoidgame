import pygame
import sys
import time

def game_loop():
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("test.game")

    background = pygame.image.load("back1.jpg")
    character = pygame.image.load("image1.png")
    character = pygame.transform.scale(character, (70, 70))

    enemy = pygame.image.load("enemy1.png")
    enemy = pygame.transform.scale(enemy, (60, 60))
    enemy_x = width
    enemy_y = 200
    enemy_speed = 5

    char_x = 100
    char_y = 100
    char_speed = 5

    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            char_x -= char_speed
        if keys[pygame.K_RIGHT]:
            char_x += char_speed
        if keys[pygame.K_UP]:
            char_y -= char_speed
        if keys[pygame.K_DOWN]:
            char_y += char_speed

        # 画面の外に出ないように
        if char_x < 0:
            char_x = 0
        if char_x > width - 70:
            char_x = width - 70
        if char_y < 0:
            char_y = 0 
        if char_y > height - 70:
            char_y = height - 70

        # 敵の動き
        enemy_x -= enemy_speed
        if enemy_x < -60:
            enemy_x = width

        # 当たり判定
        player_rect = character.get_rect(topleft=(char_x, char_y))
        enemy_rect = enemy.get_rect(topleft=(enemy_x, enemy_y))

        if player_rect.colliderect(enemy_rect):
            show_game_over(screen)
            return  # このゲームループを終了（次のループでリトライ）

        # 描画
        screen.blit(background, (0, 0))
        screen.blit(enemy, (enemy_x, enemy_y))
        screen.blit(character, (char_x, char_y))
        pygame.display.flip()

def show_game_over(screen):
    font = pygame.font.SysFont(None, 60)
    text = font.render("Game Over! Press Enter to Retry", True, (255, 0, 0))
    text_rect = text.get_rect(center=(400, 300))
    screen.blit(text, text_rect)
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                waiting = False

# ゲームのメインループ（リトライ機能付き）
pygame.init()
while True:
    game_loop()
