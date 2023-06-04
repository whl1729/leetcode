class Solution(object):
    def matrixSumQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: int
        """
        written_row = set()
        written_col = set()
        total = 0
        for query in reversed(queries):
            index, val = query[1], query[2]
            if query[0] == 0:
                if index in written_row:
                    continue
                written_row.update([index])
                total += (n - len(written_col)) * val
            else:
                if index in written_col:
                    continue
                written_col.update([index])
                total += (n - len(written_row)) * val
        return total

if __name__ == "__main__":
    solution = Solution()
    n = 3
    queries = [[0,0,1],[1,2,2],[0,2,3],[1,0,4]]
    assert solution.matrixSumQueries(n, queries) == 23
    queries = [[0,0,4],[0,1,2],[1,0,1],[0,2,3],[1,2,1]]
    assert solution.matrixSumQueries(n, queries) == 17
    n = 2
    queries = [[1,1,1],[1,0,7],[0,0,0]]
    assert solution.matrixSumQueries(n, queries) == 8