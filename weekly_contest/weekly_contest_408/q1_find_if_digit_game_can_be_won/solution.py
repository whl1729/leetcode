from typing import List

class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        total = sum(nums)
        single_sum = sum([n for n in nums if n < 10])
        return single_sum != total / 2

if __name__ == "__main__":
    solution = Solution()
    assert solution.canAliceWin([1,2,3,4,10]) == False
    assert solution.canAliceWin([1,2,3,4,5,14]) == True
    assert solution.canAliceWin([5,5,5,25]) == True