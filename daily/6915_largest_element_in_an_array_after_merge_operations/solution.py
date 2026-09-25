class Solution(object):
    def maxArrayValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest = 0
        cur_largest = 0
        for i in reversed(range(len(nums))):
            if nums[i] <= cur_largest:
                cur_largest += nums[i]
            else:
                cur_largest = nums[i]
            if cur_largest > largest:
                largest = cur_largest
        return largest

if __name__ == "__main__":
    solution = Solution()
    assert solution.maxArrayValue([2,3,7,9,3]) == 21
    assert solution.maxArrayValue([5,3,3]) == 11
        