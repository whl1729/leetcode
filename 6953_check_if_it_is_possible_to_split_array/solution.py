class Solution(object):
    def canSplitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: bool
        """
        total = sum(nums)
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            if nums[left] < nums[right]:
                total -= nums[left]
                left += 1
            else:
                total -= nums[right]
                right -= 1
            if total < m:
                return False
        return True

if __name__ == "__main__":
    solution = Solution()
    nums = [2, 2, 1]
    m = 4
    assert(solution.canSplitArray(nums, m))
    nums = [2, 1, 3]
    m = 5
    assert(solution.canSplitArray(nums, m) == False)
    nums = [2, 3, 3, 2, 3]
    m = 6
    assert(solution.canSplitArray(nums, m))
    nums = [4, 1, 3, 2, 4]
    m = 6
    assert(solution.canSplitArray(nums, m))