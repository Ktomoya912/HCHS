"""マインスイーパーのゲームロジック。
boardは1次元リスト。xは列、yは行で、左上を(0, 0)とする。
is_opendは元コードの変数名を維持している（開いているかを表す）。
"""
import random
import time


class Tile:
    def __init__(self, idx=0):
        self.index = idx
        # 【問01】マスをまだ開いていない状態にする。
        self.is_opend = ____01____
        # 【問02】最初は地雷が置かれていない状態にする。
        self.is_mine = ____02____
        # 【問03】最初は旗が立っていない状態にする。
        self.is_flagged = ____03____
        # 【問04】周囲の地雷数を0から数え始める。
        self.adjacent_mines = ____04____


class MineSweeper:
    def __init__(self, width, height, num_mines):
        if width <= 0 or height <= 0 or not 0 <= num_mines < width * height:
            raise ValueError("盤面サイズと地雷数を確認してください")
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

    def get_elapsed_time(self):
        return round(time.time() - self.start_time, 2)

    def generate_board(self):
        self.board = [Tile(i) for i in range(self.width * self.height)]
        self.is_game_over = False
        self.is_win = False
        self.start_time = time.time()
        self.num_flags = self.num_mines
        self.turn = 0
        # 【問05】全マスの番号から、地雷数だけ重複なしでランダムに選ぶ。random.sample(候補, 個数)を使う。
        mines = ____05____
        for mine in mines:
            # 【問06】選ばれた番号のマスに地雷を置く。
            self.board[mine].is_mine = ____06____
            self.set_adjacent_mines(mine)

    def set_adjacent_mines(self, index: int):
        for i in range(-1, 2):
            for j in range(-1, 2):
                # 【問07】縦と横の移動量が両方0なら、中心のマス自身なので飛ばす。
                if ____07____:
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
                # 【問08】縦にi行、横にj列移動したマスの番号を求め、周囲の地雷数を1増やす。
                self.board[____08____].adjacent_mines += 1

    def open_tile(self, x, y):
        # 【問09】座標(x, y)を1次元リストの番号に変換する。1行あたりwidth個のマスがある。
        index = ____09____
        self.open_tile_by_index(index)

    def open_tile_by_index(self, index):
        if self.is_game_over or self.is_win:
            return
        # 【問10】すでに開いている、または旗があるマスは処理しない。
        if ____10____:
            return
        # 【問11】選んだマスが地雷か調べる。
        if ____11____:
            self.board[index].is_opend = True
            # 【問12】地雷を開いたのでゲームオーバーにする。
            self.is_game_over = ____12____
            return
        # 【問13】周囲の地雷数が0なら、周囲も自動で開く処理を呼ぶ。
        if ____13____:
            self.open_zero_tiles(index)
        self.board[index].is_opend = True
        self.is_win = (
            # 【問14】開いていないマスの個数が地雷数と同じならクリア。lenで個数を求める。
            ____14____
        )

    def flag_tile(self, x, y):
        index = self.width * y + x
        self.flag_tile_by_index(index)

    def flag_tile_by_index(self, index):
        if self.is_game_over or self.is_win:
            return
        tile = self.board[index]
        if tile.is_opend:
            return
        # 旗が残っていなくても、すでにある旗は外せる。
        if not tile.is_flagged and self.num_flags == 0:
            return
        # 【問15】旗の状態を反転する。TrueをFalseに、FalseをTrueにする演算子を使う。
        tile.is_flagged = ____15____
        if tile.is_flagged:
            # 【問16】旗を立てたので、残りの旗を1減らす。
            self.num_flags -= ____16____
        else:
            # 【問17】旗を外したので、残りの旗を1増やす。
            self.num_flags += ____17____

    def open_zero_tiles(self, index: int):
        # 再帰の停止条件。旗や地雷のあるマスも開かない。
        if (self.board[index].is_opend or self.board[index].is_flagged
                or self.board[index].is_mine):
            return
        self.board[index].is_opend = True
        if self.board[index].adjacent_mines != 0:
            return
        if not self.is_tile_left(index):
            # 【問18】左隣のマスを開く。同じ行の番号は左に1減る。
            self.open_zero_tiles(____18____)
        if not self.is_tile_right(index):
            self.open_zero_tiles(index + 1)
        if not self.is_tile_top(index):
            self.open_zero_tiles(index - self.width)
        if not self.is_tile_bottom(index):
            # 【問19】下隣のマスを開く。1行下の番号はwidth増える。
            self.open_zero_tiles(____19____)
        if not self.is_tile_left(index) and not self.is_tile_top(index):
            self.open_zero_tiles(index - self.width - 1)
        if not self.is_tile_right(index) and not self.is_tile_top(index):
            self.open_zero_tiles(index - self.width + 1)
        if not self.is_tile_left(index) and not self.is_tile_bottom(index):
            self.open_zero_tiles(index + self.width - 1)
        if not self.is_tile_right(index) and not self.is_tile_bottom(index):
            self.open_zero_tiles(index + self.width + 1)

    def is_tile_left(self, index: int):
        # 【問20】左端か判定する。widthで割った余りが列番号になる。
        return ____20____

    def is_tile_right(self, index: int):
        # 【問21】右端か判定する。右端の列番号はwidth - 1。
        return ____21____

    def is_tile_top(self, index: int):
        # 【問22】最上段か判定する。最初の1行の番号はwidthより小さい。
        return ____22____

    def is_tile_bottom(self, index: int):
        # 【問23】最下段か判定する。1行下の番号が全マス数以上なら最下段。
        return ____23____

