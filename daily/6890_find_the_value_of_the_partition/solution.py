class Solution(object):
    def findValueOfPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        diff = [nums[i+1] - nums[i] for i in range(0, len(nums)-1)]
        return min(diff)

if __name__ == "__main__":
    solution = Solution()
    assert solution.findValueOfPartition([1,3,2,4]) == 1
    assert solution.findValueOfPartition([100,1,10]) == 9
    assert solution.findValueOfPartition([100,1,10,10]) == 0