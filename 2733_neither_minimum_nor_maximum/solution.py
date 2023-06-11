class Solution(object):
    def findNonMinOrMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return -1
        
        if nums[0] < nums[1]:
            if nums[1] < nums[2]:
                return nums[1]
            elif nums[0] < nums[2]:
                return nums[2]
            else:
                return nums[0]
        elif nums[1] > nums[2]:
            return nums[1]
        elif nums[0] > nums[2]:
            return nums[2]
        else:
            return nums[0]

if __name__ == "__main__":
    solution = Solution()
    assert solution.findNonMinOrMax([3,2,1,4]) == 2
    assert solution.findNonMinOrMax([1,2]) == -1
    assert solution.findNonMinOrMax([2,1,3]) == 2