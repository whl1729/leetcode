class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        sum = 0
        for i, num in enumerate(nums):
            if size % (i+1) == 0:
                sum += num * num
        return sum

if __name__ == "__main__":
    solution = Solution()
    assert solution.sumOfSquares([1,2,3,4]) == 21
    assert solution.sumOfSquares([2,7,1,19,18,3]) == 63
        