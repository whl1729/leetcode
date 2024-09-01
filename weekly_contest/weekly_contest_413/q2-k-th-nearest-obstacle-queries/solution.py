from typing import List

class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        distances = []
        results = []
        for i, query in enumerate(queries, 1):
            cur_distance = abs(query[0]) + abs(query[1])
            pos = self.find_pos(cur_distance, distances)
            distances.insert(pos, cur_distance)
            kth_distance = distances[k-1] if i >= k else -1
            results.append(kth_distance)

        return results

    def find_pos(self, target, arr: List[int]) -> int:
        length = len(arr)
        if length == 0:
            return 0

        left, right = 0, length
        while left < right:
            mid = (left + right) // 2
            if target <= arr[mid]:
                if (mid == 0) or (target >= arr[mid-1]):
                    return mid
                right = mid - 1
            else:
                left = mid + 1

        return right


if __name__ == "__main__":
    s = Solution()
    queries = [[1,2],[3,4],[2,3],[-3,0]]
    k = 2
    output = [-1,7,5,3]
    result = s.resultsArray(queries, k)
    assert result == output

    queries = [[5,5],[4,4],[3,3]]
    k = 1
    output = [10,8,6]
    result = s.resultsArray(queries, k)
    assert result == output