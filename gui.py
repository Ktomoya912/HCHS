import math
import sys
from tkinter import Tk, messagebox

import pygame
from pygame.locals import QUIT

from mine_sweeper import MineSweeper, Tile

Tk().wm_withdraw()  # to hide the main window


class TileButton:
    def __init__(self, x, y, size, tile: Tile):
        self.button = pygame.Rect(x, y, size, size)
        self.tile = tile
        self.size = size

    def draw(self, screen: pygame.Surface):
        if self.tile.is_opend:
            pygame.draw.rect(screen, (200, 200, 200), self.button)
            if self.tile.is_mine:
                pygame.draw.circle(
                    screen, (0, 0, 0), self.button.center, self.size // 2
                )
            else:
                font = pygame.font.Font(None, 36)
                text = font.render(str(self.tile.adjacent_mines), True, (0, 0, 0))
                screen.blit(text, text.get_rect(center=self.button.center))
        elif self.tile.is_flagged:
            pygame.draw.rect(screen, (0, 0, 200), self.button)
        else:
            pygame.draw.rect(screen, (200, 200, 200), self.button)


def init(board_width, board_height, mines):
    game = MineSweeper(board_width, board_height, mines)
    padding = 5
    button_size = 30
    tile_buttons = [
        TileButton(
            i % board_width * (button_size + padding) + padding,
            i // board_width * (button_size + padding) + padding,
            button_size,
            tile,
        )
        for i, tile in enumerate(game.board)
    ]
    screen = pygame.display.set_mode(
        (
            board_width * (button_size + padding) + padding,
            board_height * (button_size + padding) + padding,
        )
    )
    return game, tile_buttons, screen


def main():
    pygame.init()  # Pygameの初期化
    pygame.display.set_caption("マインスイーパー")
    board_width = 14
    board_height = 18
    mines = math.floor(0.159 * board_width * board_height)
    print(f"board_width: {board_width}, board_height: {board_height}, mines: {mines}")
    game, tile_buttons, screen = init(board_width, board_height, mines)
    while True:
        screen.fill((0, 0, 0))
        for button in tile_buttons:
            button.draw(screen)
        pygame.display.update()  # 画面を更新
        if game.is_game_over:
            if messagebox.askretrycancel(
                "Game Over",
                f"{game.get_elapsed_time()}秒でGAME OVER!!!\n再挑戦しますか?",
            ):
                game, tile_buttons, _ = init(board_width, board_height, mines)
            else:
                break
        if game.is_win:
            if messagebox.askretrycancel(
                "You Win", f"{game.get_elapsed_time()}秒でクリア!!!\n再挑戦しますか?"
            ):
                game, tile_buttons, _ = init(board_width, board_height, mines)
            else:
                break
        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:  # 閉じるボタンが押されたら終了
                pygame.quit()  # Pygameの終了(画面閉じられる)
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in tile_buttons:
                    if button.button.collidepoint(event.pos):
                        if event.button == 1:
                            game.open_tile_by_index(tile_buttons.index(button))
                        elif event.button == 3:
                            game.flag_tile_by_index(tile_buttons.index(button))
                        break


if __name__ == "__main__":
    main()
