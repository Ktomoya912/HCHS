import random


class State:
    def __init__(self, size: int = 4):
        self.size = size
        self.board = [0 for _ in range(size*size)]
        self.score = ...

    @property
    def is_game_over(self):
        """ゲームオーバーであるかを確認する関数"""
        if 0 in self.board:
            return
        if self.can_move_dir:
            return False
        return True

    @property
    def can_move_dir(self):
        """
        動かせる方向を返す関数
        """
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
        """
        現在の盤面を表示する関数"""
        for i in range(self.size):
            print(self.board[i * self.size : (i + 1) * self.size])

    def init_game(self):
        """ゲームを初期化する関数。
        ボードの中身をすべて0にして、スコアも0にする。
        また、ランダムでタイルを二つ配置する。
        """
        pass

    def put_new_tile(self):
        """盤面にタイルを配置する関数。
        初めに何も置かれていないタイルを取ってきて、その中に10%の確率で4を、90%の確率で2を配置する。
        """
        empty_tiles = [i for i, x in enumerate(self.board) if x == 0]
        if empty_tiles:
            self.board[random.choice(empty_tiles)] = 2 if random.random() < 0.9 else 4

    def move(self, direction: str):
        """方向を指定したら、タイルが動く関数を呼び出す。"""
        pass

    def _move_tiles(self, tiles):
        """実際にタイルを動かす関数。
        ここは触らなくていい。
        """
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
        """タイルが左に動かせるかを確認する関数"""
        for i in range(self.size):
            row = self.board[i * self.size : (i + 1) * self.size]
            if self._move_tiles(row)[2]:
                return True
        return False

    def can_move_right(self):
        """タイルが右に動かせるかを確認する関数"""
        for i in range(self.size):
            row = self.board[i * self.size : (i + 1) * self.size]
            if self._move_tiles(row[::-1])[2]:
                return True
        return False

    def can_move_up(self):
        """タイルが上に動かせるかを確認する関数"""
        for i in range(self.size):
            col = self.board[i :: self.size]
            if self._move_tiles(col)[2]:
                return True
        return False

    def can_move_down(self):
        """タイルが下に動かせるかを確認する関数"""
        for i in range(self.size):
            col = self.board[i :: self.size]
            if self._move_tiles(col[::-1])[2]:
                return True
        return False

    def move_left(self):
        """タイルを左に動かす関数"""
        for i in range(self.size):
            row = self.board[i * self.size : (i + 1) * self.size]
            new_row, score, _ = self._move_tiles(row)
            self.score += score
            self.board[i * self.size : (i + 1) * self.size] = new_row

    def move_right(self):
        """タイルを右に動かす関数"""
        for i in range(self.size):
            row = self.board[i * self.size : (i + 1) * self.size]
            new_row, score, _ = self._move_tiles(row[::-1])
            self.score += score
            self.board[i * self.size : (i + 1) * self.size] = new_row[::-1]

    def move_up(self):
        """タイルを上に動かす関数"""
        for i in range(self.size):
            col = self.board[i :: self.size]
            new_col, score, _ = self._move_tiles(col)
            self.score += score
            self.board[i :: self.size] = new_col

    def move_down(self):
        """タイルを下に動かす関数"""
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

    # ゲームをインスタンス化する(Stateを使えるようにする)
    
    # ゲームを初期化する

    # ゲームオーバーになるまでループする。

    # 現在の盤面を表示する
        # direction = input("Enter direction: ")
        # direction = random_move(state)
    # 選択された方向にタイルを動かす関数を呼び出す。
    # タイルを動かし終わった後に新しいタイルを配置する。
    # もし、タイルを配置したときにゲームオーバー」状態であったらボードを表示して、
    # "Game over!"と表示して、ループを抜ける


if __name__ == "__main__":
    main()
