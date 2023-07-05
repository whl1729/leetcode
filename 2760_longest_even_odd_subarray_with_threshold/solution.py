class Solution(object):
    def longestAlternatingSubarray(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        max_len = 0
        for left in range(0, len(nums)):
            cur_len = self.maxAlternatingArrLen(nums, left, threshold)
            if cur_len > max_len:
                max_len = cur_len
        return max_len
    
    def maxAlternatingArrLen(self, nums, left, threshold):
        max_len = 0
        remainder = 0
        for i in range(left, len(nums)):
            if nums[i] > threshold:
                break
            if nums[i] % 2 != remainder:
                break
            remainder = 1 - remainder
            max_len += 1
        return max_len

if __name__ == "__main__":
    solution = Solution()
    assert solution.longestAlternatingSubarray([3, 2, 5, 4], 5) == 3
    assert solution.longestAlternatingSubarray([3, 2, 5, 4], 1) == 0
    assert solution.longestAlternatingSubarray([1, 2], 2) == 1
    assert solution.longestAlternatingSubarray([2, 3, 4, 5], 4) == 3
    assert solution.longestAlternatingSubarray([2], 4) == 1
    assert solution.longestAlternatingSubarray([2], 1) == 0