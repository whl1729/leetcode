class Solution(object):
    def semiOrderedPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        index_1 = nums.index(1)
        index_n = nums.index(n)
        if index_1 < index_n:
            return index_1 + n - 1 - index_n
        return index_1 + n - 2 - index_n

if __name__ == "__main__":
    solution = Solution()
    assert solution.semiOrderedPermutation([2,1,4,3]) == 2
    assert solution.semiOrderedPermutation([2,4,1,3]) == 3
    assert solution.semiOrderedPermutation([1,3,4,2,5]) == 0