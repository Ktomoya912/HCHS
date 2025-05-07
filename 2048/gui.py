import time

import pygame
from game_2048 import State
from pygame.locals import K_DOWN, K_LEFT, K_RIGHT, K_UP, KEYDOWN, QUIT

# 定数の定義
WIDTH, HEIGHT = 400, 400
TILE_SIZE = 100
FONT_SIZE = 36
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = {
    0: (204, 192, 179),
    1: (238, 228, 218),
    2: (237, 224, 200),
    3: (242, 177, 121),
    4: (245, 149, 99),
    5: (246, 124, 95),
    6: (246, 94, 59),
    7: (237, 207, 114),
    8: (237, 204, 97),
    9: (237, 200, 80),
    10: (237, 197, 63),
    11: (237, 194, 46),
}


# ボードを描画する関数
def draw_board(screen, bd, move=None, progress=0):
    screen.fill((204, 192, 179))
    for i in range(bd.size):
        for j in range(bd.size):
            tile_value = bd.board[i * bd.size + j]
            color = COLORS.get(tile_value, (60, 58, 50))
            x, y = j * TILE_SIZE, i * TILE_SIZE
            if move:
                if (
                    move == "up"
                    and i < bd.size - 1
                    and bd.board[(i + 1) * bd.size + j] == tile_value
                ):
                    y += TILE_SIZE * (1 - progress)
                elif (
                    move == "down"
                    and i > 0
                    and bd.board[(i - 1) * bd.size + j] == tile_value
                ):
                    y -= TILE_SIZE * (1 - progress)
                elif (
                    move == "left"
                    and j < bd.size - 1
                    and bd.board[i * bd.size + (j + 1)] == tile_value
                ):
                    x += TILE_SIZE * (1 - progress)
                elif (
                    move == "right"
                    and j > 0
                    and bd.board[i * bd.size + (j - 1)] == tile_value
                ):
                    x -= TILE_SIZE * (1 - progress)
            pygame.draw.rect(screen, color, (x, y, TILE_SIZE, TILE_SIZE))
            if tile_value > 0:
                text = FONT.render(
                    str(2**tile_value), True, BLACK if tile_value <= 2 else WHITE
                )
                text_rect = text.get_rect(
                    center=(x + TILE_SIZE // 2, y + TILE_SIZE // 2)
                )
                screen.blit(text, text_rect)
    pygame.display.flip()


# アニメーションを描画する関数
def animate_move(screen, bd, direction):
    for progress in range(1, 11):
        draw_board(screen, bd, move=direction, progress=progress / 10.0)
        pygame.display.flip()
        time.sleep(0.01)


# メイン関数
def main():
    pygame.init()
    global FONT
    FONT = pygame.font.Font(None, FONT_SIZE)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("2048 Player")
    bd = State()  # ゲームの状態を初期化
    bd.init_game()  # ゲームの開始
    while not bd.is_game_over:
        draw_board(screen, bd)  # ボードの描画
        pygame.event.pump()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
            elif event.type == KEYDOWN:
                if event.key == K_UP and bd.can_move_up():
                    bd.move("up")  # 上に移動
                    animate_move(screen, bd, "up")
                    bd.put_new_tile()  # 新しいタイルを配置
                elif event.key == K_DOWN and bd.can_move_down():
                    bd.move("down")  # 下に移動
                    animate_move(screen, bd, "down")
                    bd.put_new_tile()  # 新しいタイルを配置
                elif event.key == K_LEFT and bd.can_move_left():
                    bd.move("left")  # 左に移動
                    animate_move(screen, bd, "left")
                    bd.put_new_tile()  # 新しいタイルを配置
                elif event.key == K_RIGHT and bd.can_move_right():
                    bd.move("right")  # 右に移動
                    animate_move(screen, bd, "right")
                    bd.put_new_tile()  # 新しいタイルを配置
                else:
                    continue
                draw_board(screen, bd)  # ボードの描画


if __name__ == "__main__":
    main()
