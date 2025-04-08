import pygame
import sys
import time
import random

# --- メインのゲームループ関数 ---
def game_loop():
    # --- 画面サイズ指定 ---
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("test.game")  # ウィンドウのタイトル設定

    # --- 画像読み込み ---
    background = pygame.image.load("back1.jpg")  # 背景画像
    character = pygame.image.load("image1.png")  # プレイヤー画像
    character = pygame.transform.scale(character, (70, 70))  # プレイヤー画像サイズ変更
    enemy = pygame.image.load("enemy1.png")  # 敵画像
    enemy = pygame.transform.scale(enemy, (60, 60))  # 敵画像サイズ変更

    # --- 敵リストと出現タイマーの初期化 ---
    enemy_list = []  # 敵の位置リスト
    last_spawn_time = time.time()  # 最後に敵が出現した時間
    spawn_interval = random.uniform(1.5, 3.0)  # 次の敵が出るまでのランダムな間隔（秒）

    # --- プレイヤーの初期設定 ---
    char_x, char_y = 100, 100  # プレイヤーの初期位置
    char_speed = 5  # プレイヤーの移動速度

    # --- スコアと開始時間の初期化 ---
    start_time = time.time()
    score = 0

    clock = pygame.time.Clock()  # フレーム管理用タイマー
    running = True  # ゲームループ継続フラグ

    while running:
        clock.tick(60)  # 60FPSでループ実行

        # --- イベント処理 ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # --- キー入力でプレイヤーを動かす処理 ---
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: char_x -= char_speed
        if keys[pygame.K_RIGHT]: char_x += char_speed
        if keys[pygame.K_UP]: char_y -= char_speed
        if keys[pygame.K_DOWN]: char_y += char_speed

        # --- プレイヤーが画面外に出ないように制限 ---
        char_x = max(0, min(char_x, width - 70))
        char_y = max(0, min(char_y, height - 70))

        # --- スコア更新と敵のスピード設定 ---
        score = int(time.time() - start_time)  # 経過時間がスコアになる
        enemy_speed = 5 + score // 5  # スコアに応じて敵の速度が上昇

        # --- 敵のランダム出現処理 ---
        if time.time() - last_spawn_time > spawn_interval:
            x = width + random.randint(0, 300)
            y = random.randint(100, height - 60)
            enemy_list.append([x, y])
            last_spawn_time = time.time()
            spawn_interval = random.uniform(1.5, 3.0)

        # --- 背景を描画 ---
        screen.blit(background, (0, 0))

        # --- プレイヤーの当たり判定用四角形 ---
        player_rect = character.get_rect(topleft=(char_x, char_y)).inflate(-20, -20)

        # --- 敵の移動処理と当たり判定 ---
        for i in range(len(enemy_list)):
            enemy_list[i][0] -= enemy_speed  # 敵を左に移動
            if enemy_list[i][0] < -60:  # 画面外に出たら右端に戻す
                enemy_list[i][0] = width
                enemy_list[i][1] = random.randint(100, height - 60)

            screen.blit(enemy, (enemy_list[i][0], enemy_list[i][1]))  # 敵の描画

            # 敵の当たり判定用四角形
            enemy_rect = enemy.get_rect(topleft=(enemy_list[i][0], enemy_list[i][1])).inflate(-10, -10)
            if player_rect.colliderect(enemy_rect):  # プレイヤーと敵がぶつかったら
                show_game_over(screen, score)  # ゲームオーバー画面を表示
                return  # 現在のゲームループを終了

        # --- プレイヤーの描画 ---
        screen.blit(character, (char_x, char_y))

        # --- スコアの描画 ---
        score_text = pygame.font.SysFont(None, 36).render(f"Score: {score}", True, (0, 255, 255))
        screen.blit(score_text, (10, 10))

        pygame.display.flip()  # 画面更新

# --- ゲームオーバー処理 ---
def show_game_over(screen, score):
    font = pygame.font.SysFont("Arial", 60, bold=True)

    # ゲームオーバー文字表示
    text = font.render("Game Over! Press Enter to Retry", True, (255, 0, 0))
    text_rect = text.get_rect(center=(400, 250))
    screen.blit(text, text_rect)

    # スコア表示
    score_text = font.render(f"Your Score: {score}", True, (0, 255, 255))
    score_rect = score_text.get_rect(center=(400, 320))
    screen.blit(score_text, score_rect)

    pygame.display.flip()  # 表示内容を反映

    # Enterが押されるまで待機
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                waiting = False

# --- ゲーム起動処理 ---
pygame.init()  # Pygameの初期化
while True:
    game_loop()  # ゲーム開始