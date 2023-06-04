class Solution(object):
    def matrixSumQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: int
        """
        matrix = [[0] * n for i in range(0, n)]
        for query in queries:
            if query[0] == 0:
                row = query[1]
                for i in range(0, n):
                    matrix[row][i] = query[2]
            else:
                col = query[1]
                for i in range(0, n):
                    matrix[i][col] = query[2]
        return sum([sum(i) for i in matrix])

if __name__ == "__main__":
    solution = Solution()
    n = 3
    queries = [[0,0,1],[1,2,2],[0,2,3],[1,0,4]]
    assert solution.matrixSumQueries(n, queries) == 23
    queries = [[0,0,4],[0,1,2],[1,0,1],[0,2,3],[1,2,1]]
    assert solution.matrixSumQueries(n, queries) == 17