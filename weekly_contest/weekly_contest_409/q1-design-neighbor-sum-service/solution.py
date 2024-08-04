from typing import List
from typing import Tuple

class neighborSum:
    def __init__(self, grid: List[List[int]]):
        self._grid = grid
        self._len = len(grid[0])

    def adjacentSum(self, value: int) -> int:
        x, y = self._find(value)
        sum = 0
        if y - 1 >= 0:
            sum += self._grid[x][y-1]

        if y + 1 < self._len:
            sum += self._grid[x][y+1]

        if x - 1 >= 0:
            sum += self._grid[x-1][y]

        if x + 1 < self._len:
            sum += self._grid[x+1][y]

        return sum

    def diagonalSum(self, value: int) -> int:
        x, y = self._find(value)
        sum = 0
        if x - 1 >= 0 and y - 1 >= 0:
            sum += self._grid[x-1][y-1]

        if x + 1 < self._len and y - 1 >= 0:
            sum += self._grid[x+1][y-1]

        if x - 1 >= 0 and y + 1 < self._len:
            sum += self._grid[x-1][y+1]

        if x + 1 < self._len and y + 1 < self._len:
            sum += self._grid[x+1][y+1]

        return sum

    def _find(self, value: int) -> Tuple[int, int]:
        for i in range(self._len):
            for j in range(self._len):
                if self._grid[i][j] == value:
                    return (i, j)
        
        # Never goto here
        return (-1, -1)
        

if __name__ == "__main__":
    # Your neighborSum object will be instantiated and called as such:
    grid = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    obj = neighborSum(grid)
    result = obj.adjacentSum(1)
    assert result == 6
    result = obj.adjacentSum(4)
    assert result == 16
    result = obj.diagonalSum(4)
    assert result == 16
    result = obj.diagonalSum(8)
    assert result == 4