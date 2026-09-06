from typing import List

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        query_cnt = len(queries)
        result = [0 for _ in range(query_cnt)]
        distances = [i for i in range(n)]
        next = {n-1: []}
        for i in range(n-1):
            next[i] = [i+1]

        for i, (start, end) in enumerate(queries):
            next[start].append(end)
            if distances[end] > distances[start] + 1:
                distances[end] = distances[start] + 1

            to_update = [end]
            while len(to_update) > 0:
                cur = to_update.pop(0)
                for neighbor in next[cur]:
                    if distances[neighbor] > distances[cur] + 1:
                        distances[neighbor] = distances[cur] + 1
                        to_update.append(neighbor)

            result[i] = distances[n-1]

        return result


if __name__ == "__main__":
    solution = Solution()
    n = 5
    queries = [[2,4],[0,2],[0,4]]
    result = solution.shortestDistanceAfterQueries(n, queries)
    print(result)
    assert result == [3, 2, 1]

    n = 4
    queries = [[0,3],[0,2]]
    result = solution.shortestDistanceAfterQueries(n, queries)
    assert result == [1, 1]