import random


class State:
    def __init__(self, size: int = 4):
        self.size = size
        self.board = [0 for _ in range(size * size)]
        self.score = 0

    @property
    def is_game_over(self):
        if 0 in self.board:
            return
        if self.can_move_dir:
            return False
        return True

    @property
    def can_move_dir(self):
        result = []
        if self.can_move_up():
            result.append("up")
        if self.can_move_down():
            result.append("down")
        if self.can_move_left():
            result.append("left")
        if self.can_move_right():
            result.append("right")
        return result

    def print_board(self):
        for i in range(self.size):
            print(self.board[i * self.size : (i + 1) * self.size])

    def init_game(self):
        self.board = [0 for _ in self.board]
        self.score = 0
        self.put_new_tile()
        self.put_new_tile()

    def put_new_tile(self):
        empty_tiles = [i for i, x in enumerate(self.board) if x == 0]
        if empty_tiles:
            self.board[random.choice(empty_tiles)] = 2 if random.random() < 0.9 else 4

    def move(self, direction: str):
        if direction == "left":
            self.move_left()
        elif direction == "right":
            self.move_right()
        elif direction == "up":
            self.move_up()
        elif direction == "down":
            self.move_down()
        else:
            raise ValueError("Invalid direction")

    def _move_tiles(self, tiles):
        new_tiles = [0 for _ in range(self.size)]
        score = 0
        j = 0
        for i in range(self.size):
            if tiles[i] == 0:
                continue
            if new_tiles[j] == 0:
                new_tiles[j] = tiles[i]
            elif new_tiles[j] == tiles[i]:
                new_tiles[j] += 1
                score += 2 ** new_tiles[j]
                j += 1
            else:
                j += 1
                new_tiles[j] = tiles[i]
        return new_tiles, score, tiles != new_tiles

    def can_move_left(self):
        for i in range(self.size):
            row = self.board[i * self.size : (i + 1) * self.size]
            if self._move_tiles(row)[2]:
                return True
        return False

    def can_move_right(self):
        for i in range(self.size):
            row = self.board[i * self.size : (i + 1) * self.size]
            if self._move_tiles(row[::-1])[2]:
                return True
        return False

    def can_move_up(self):
        for i in range(self.size):
            col = self.board[i :: self.size]
            if self._move_tiles(col)[2]:
                return True
        return False

    def can_move_down(self):
        for i in range(self.size):
            col = self.board[i :: self.size]
            if self._move_tiles(col[::-1])[2]:
                return True
        return False

    def move_left(self):
        for i in range(self.size):
            row = self.board[i * self.size : (i + 1) * self.size]
            new_row, score, _ = self._move_tiles(row)
            self.score += score
            self.board[i * self.size : (i + 1) * self.size] = new_row

    def move_right(self):
        for i in range(self.size):
            row = self.board[i * self.size : (i + 1) * self.size]
            new_row, score, _ = self._move_tiles(row[::-1])
            self.score += score
            self.board[i * self.size : (i + 1) * self.size] = new_row[::-1]

    def move_up(self):
        for i in range(self.size):
            col = self.board[i :: self.size]
            new_col, score, _ = self._move_tiles(col)
            self.score += score
            self.board[i :: self.size] = new_col

    def move_down(self):
        for i in range(self.size):
            col = self.board[i :: self.size]
            new_col, score, _ = self._move_tiles(col[::-1])
            self.score += score
            self.board[i :: self.size] = new_col[::-1]


def main():
    def random_move(state: State):
        if state.can_move_dir:
            return random.choice(state.can_move_dir)
        return None

    state = State(3)
    state.init_game()
    while True:
        state.print_board()
        print(state.score)
        # direction = input("Enter direction: ")
        direction = random_move(state)
        state.move(direction)
        state.put_new_tile()
        if state.is_game_over:
            state.print_board()
            print("Game over!")
            break


if __name__ == "__main__":
    main()
