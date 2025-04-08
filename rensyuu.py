import pygame
import sys
import time

pygame.init()

# [画面サイズ指定]
# 関数作成
# タスクバー表示名
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("test_game")

# [画像読み込み]
# 背景
background = pygame.image.load("back.jpg")

# キャラクター
character = pygame.image.load("image1.png")
character = pygame.transform.scale(character, (70, 70))

# 敵
enemy = pygame.image.load("enemy1.png")
enemy = pygame.transform.scale(enemy, (60, 60))

# [キャラの初期設定]
# 画面の右端からスタート
enemy_x = width
enemy_y = 200
enemy_speed = 5

char_x = 100
char_y = 100
char_speed = 5

# [ゲーム処理]
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)
    
    for event in pygame.event.get(): # イベントのリストを取得する関数
        if event.type == pygame.QUIT:
            
            pygame.quit()
            sys.exit
            
            
# [キャラクターの動き設定]            
# [キー入力を受ける]    
# キーの状態がリストとして格納        
keys = pygame.key.get_pressed()

# "←"　x座標　指定速度でマイナス方向に進む
# "→"　x座標　指定速度でプラス方向に進む
# "↑"  y座標　指定速度でマイナス方向に進む
# "↓"  y座標　指定速度でプラス方向に進む
if keys[pygame.K_LEFT]:
    char_x -= char_speed    
if keys[pygame.K_RIGHT]:
    char_x += char_speed
if keys[pygame.K_UP]:
    char_y -= char_speed 
if keys[pygame.K_DOWN]:
    char_y += char_speed       


# [画面外に出ないように処理]
# (左移動)
# x座標 0未満になったら座標0に固定(キャラが左上基準:キャラの大きさ考慮x)
if char_x < 0:
    char_x = 0
# (右移動)
# x座標 最大値 -　(キャラの大きさ)を超過したらそこで固定
if char_x > width - 70:
    char_x = width - 70
# (上移動)
if char_y < 0:
    char_y = 0
    # (下移動)
if char_y > height - 70:
    char_y = height - 70    
 

# [敵の動き設定]
enemy_x -= enemy_speed
if enemy_x < 60:
    enemy_x = width     
    
# [当たり判定]-------
player_rect = character.get_rect(topleft = (char_x, char_y))         