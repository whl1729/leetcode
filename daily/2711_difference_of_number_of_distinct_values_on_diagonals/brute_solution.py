def abs(n):
    return n if n >= 0 else -n

def min(a, b):
    return a if a < b else b

class Solution(object):
    def differenceOfDistinctValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(grid), len(grid[0])
        answer = [[0] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                top_left = self._get_top_left_distinct_cnt(grid, m, n, i, j)
                right_bottom = self._get_right_bottom_distinct_cnt(grid, m, n, i, j)
                answer[i][j] = abs(top_left - right_bottom)
        return answer
        
    def _get_top_left_distinct_cnt(self, grid, m, n, i, j):
        return len(set([grid[i-k][j-k] for k in range(1, min(i+1, j+1))]))
        

    def _get_right_bottom_distinct_cnt(self, grid, m, n, i, j):
        return len(set([grid[i+k][j+k] for k in range(1, min(m-i, n-j))]))

if __name__ == "__main__":
    solution = Solution()
    grid = [[1,2,3],[3,1,5],[3,2,1]]
    output = [[1,1,0],[1,0,1],[0,1,1]]
    actual = solution.differenceOfDistinctValues(grid)
    print(actual)
    assert actual == output
    grid = [[1]]
    output = [[0]]
    actual = solution.differenceOfDistinctValues(grid)
    print(actual)
    assert actual == output
