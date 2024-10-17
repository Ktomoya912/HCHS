import random
import time


class TextColor:
    RED: str = "\033[91m"
    GREEN: str = "\033[92m"
    YELLOW: str = "\033[93m"
    BLUE: str = "\033[94m"
    PINK: str = "\033[95m"
    CYAN: str = "\033[96m"
    WHITE: str = "\033[97m"
    BOLD: str = "\033[1m"
    UNDERLINE: str = "\033[4m"
    END: str = "\033[0m"


class Tile:
    def __init__(self, idx=0):
        self.index = idx
        self.is_opend = False
        self.is_mine = False
        self.is_flagged = False
        self.adjacent_mines = 0


class MineSweeper:
    def __init__(self, width, height, num_mines):
        self.width = width
        self.height = height
        self.num_mines = num_mines
        self.num_flags = num_mines
        self.turn = 0
        self.board = [Tile() for _ in range(width * height)]
        self.is_game_over = False
        self.is_win = False
        self.start_time = time.time()

        self.generate_board()

    def print_board(self, is_debug=False):
        print(
            "   "
            + " ".join(
                [f"{TextColor.RED}{i:2}{TextColor.END}" for i in range(self.width)]
            )
        )
        for i in range(self.height):
            print(f"{TextColor.RED}{i:2}{TextColor.END}", end=" ")
            for j in range(self.width):
                index = i * self.width + j
                if is_debug:
                    if self.board[index].is_mine:
                        print(" M", end=" ")
                    elif self.board[index].is_flagged:
                        print(" F", end=" ")
                    else:
                        print(f"{self.board[index].adjacent_mines:2}", end=" ")
                else:
                    if self.board[index].is_opend:
                        print(f"\033[0m{self.board[index].adjacent_mines:2}", end=" ")
                    elif self.board[index].is_flagged:
                        print(f"{TextColor.CYAN} F{TextColor.END}", end=" ")
                    else:
                        print("\033[1;37;40m X", end=" ")
            print("\033[0m")

    def print_remaining_mines(self):
        print(f"Remaining Mines: {self.num_flags}")

    def get_elapsed_time(self):
        return round(time.time() - self.start_time, 2)

    def generate_board(self):
        self.is_game_over = False
        self.num_flags = self.num_mines
        self.turn = 0
        mines = random.sample(range(self.width * self.height), self.num_mines)
        for mine in mines:
            self.board[mine].is_mine = True
            self.set_adjacent_mines(mine)

    def set_adjacent_mines(self, index: int):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if self.is_tile_left(index) and j == -1:
                    continue
                if self.is_tile_right(index) and j == 1:
                    continue
                if self.is_tile_top(index) and i == -1:
                    continue
                if self.is_tile_bottom(index) and i == 1:
                    continue
                if self.board[index + i * self.width + j].is_mine:
                    continue
                self.board[index + i * self.width + j].adjacent_mines += 1

    def open_tile(self, x, y):
        index = self.width * y + x
        self.open_tile_by_index(index)

    def open_tile_by_index(self, index):
        if self.board[index].is_opend or self.board[index].is_flagged:
            return
        if self.board[index].is_mine:
            self.is_game_over = True
            return
        if self.board[index].adjacent_mines == 0:
            self.open_zero_tiles(index)
        self.board[index].is_opend = True
        self.is_win = (
            len([tile for tile in self.board if not tile.is_opend]) == self.num_mines
        )

    def flag_tile(self, x, y):
        if self.num_flags == 0:
            print("No more flags!")
            return
        index = self.width * y + x
        self.flag_tile_by_index(index)

    def flag_tile_by_index(self, index):
        self.board[index].is_flagged = not self.board[index].is_flagged
        if self.board[index].is_flagged:
            self.num_flags -= 1
        else:
            self.num_flags += 1

    def open_zero_tiles(self, index: int):
        if self.board[index].is_opend:
            return
        self.board[index].is_opend = True
        if self.board[index].adjacent_mines != 0:
            return
        if not self.is_tile_left(index):
            self.open_zero_tiles(index - 1)
        if not self.is_tile_right(index):
            self.open_zero_tiles(index + 1)
        if not self.is_tile_top(index):
            self.open_zero_tiles(index - self.width)
        if not self.is_tile_bottom(index):
            self.open_zero_tiles(index + self.width)
        if not self.is_tile_left(index) and not self.is_tile_top(index):
            self.open_zero_tiles(index - self.width - 1)
        if not self.is_tile_right(index) and not self.is_tile_top(index):
            self.open_zero_tiles(index - self.width + 1)
        if not self.is_tile_left(index) and not self.is_tile_bottom(index):
            self.open_zero_tiles(index + self.width - 1)
        if not self.is_tile_right(index) and not self.is_tile_bottom(index):
            self.open_zero_tiles(index + self.width + 1)

    def is_tile_left(self, index: int):
        return index % self.width == 0

    def is_tile_right(self, index: int):
        return index % self.width == self.width - 1

    def is_tile_top(self, index: int):
        return index < self.width

    def is_tile_bottom(self, index: int):
        return index + self.width >= self.width * self.height

    def play(self):
        while True:
            self.turn += 1
            print(f"Turn: {self.turn}")
            ipt = input("Enter x, y, [option] action (flag): ").split(" ")
            if len(ipt) == 3:
                x, y, action = ipt
            else:
                x, y = ipt
                action = None
            x, y = int(x), int(y)
            if action:
                self.flag_tile(x, y)
            else:
                self.open_tile(x, y)
                if self.is_game_over:
                    if self.turn == 1:
                        self.generate_board()
                        self.open_tile(x, y)
                    print("Game Over!")
                    self.print_board(is_debug=True)
                    break
                if self.is_win:
                    print("You Win!")
                    self.print_board(is_debug=True)
                    break
            self.print_board()
            self.print_remaining_mines()


if __name__ == "__main__":
    game = MineSweeper(10, 10, 18)
    game.print_board()
    game.play()
