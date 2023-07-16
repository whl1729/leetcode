class Solution(object):
    # 思路：
    # - 若 k = 0，则 beauty 就是原数组的众数的数量
    # - 若 k >= max(nums)/2，则 beauty 就是 len(nums)
    # - 关键是确定最终这个相同的数字是什么（为简便期间，不妨称之为 target）
    # - 这道题与元素的顺序无关，因而可以先排序
    # - 排序后，遍历每个元素，找出取值相差2k以内的最大长度
    def maximumBeauty(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        delta = 2 * k
        beauty = 1
        size = len(nums)
        for i in range(size):
            end = self.find_no_more_than(nums, i+beauty, size, nums[i]+delta)
            if end - i > beauty:
                beauty = end - i
        return beauty

    # find the maximum index starting with `start` whose value is no more than target
    def find_no_more_than(self, nums, start, end, target):
        for i in range(start, end):
            if nums[i] > target:
                return i
        return end

if __name__ == "__main__":
    solution = Solution()
    assert solution.maximumBeauty([4,6,1,2], 2) == 3
    assert solution.maximumBeauty([1,1,1,1], 10) == 4
    assert solution.maximumBeauty([1,2,3,4], 0) == 1
    assert solution.maximumBeauty([1,7,11,12], 1) == 2