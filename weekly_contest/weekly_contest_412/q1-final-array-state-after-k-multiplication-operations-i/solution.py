from typing import List

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            min_val = min(nums)
            min_pos = nums.index(min_val)
            nums[min_pos] *= multiplier

        return nums
        
if __name__ == "__main__":
    s = Solution()
    nums = [2,1,3,5,6]
    k = 5
    multiplier = 2
    result = s.getFinalState(nums, k, multiplier)
    assert result == [8,4,6,5,6]

    nums = [1,2]
    k = 3
    multiplier = 4
    result = s.getFinalState(nums, k, multiplier)
    assert result == [16, 8]