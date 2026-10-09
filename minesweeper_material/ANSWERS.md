# 解答一覧（教員用）

| 問 | 記入例 |
| --- | --- |
| 01 | `False` |
| 02 | `False` |
| 03 | `False` |
| 04 | `0` |
| 05 | `random.sample(range(self.width * self.height), self.num_mines)` |
| 06 | `True` |
| 07 | `i == 0 and j == 0` |
| 08 | `index + i * self.width + j` |
| 09 | `self.width * y + x` |
| 10 | `self.board[index].is_opend or self.board[index].is_flagged` |
| 11 | `self.board[index].is_mine` |
| 12 | `True` |
| 13 | `self.board[index].adjacent_mines == 0` |
| 14 | `len([tile for tile in self.board if not tile.is_opend]) == self.num_mines` |
| 15 | `not tile.is_flagged` |
| 16 | `1` |
| 17 | `1` |
| 18 | `index - 1` |
| 19 | `index + self.width` |
| 20 | `index % self.width == 0` |
| 21 | `index % self.width == self.width - 1` |
| 22 | `index < self.width` |
| 23 | `index + self.width >= self.width * self.height` |
| 24 | `open_tile_by_index` |
| 25 | `flag_tile_by_index` |
