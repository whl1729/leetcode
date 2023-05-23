# 思路：初始化时对前k个元素排序，每次插入新元素时也重新排序
class KthLargest(object):
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        nums.sort(reverse=True)
        self._nums = nums[:k]
        self._len = k
        # 数组长度最小为 k - 1，此时为便于处理先添加一个哨兵
        if len(nums) < k:
            self._nums.append(-10000)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        index = self._search(val)
        if index >= self._len:
            return self._nums[-1]
        for i in range(self._len - 1, index, -1):
            self._nums[i] = self._nums[i - 1]
        self._nums[index] = val
        return self._nums[-1]

    def _search(self, val):
        """Return the index to insert val
        :type val: int
        :rtype: int
        """
        for i in range(0, self._len):
            if val > self._nums[i]:
                return i
        return self._len


if __name__ == "__main__":
    # case 1
    kthLargest = KthLargest(3, [4, 5, 8, 2])
    assert kthLargest.add(3) == 4
    assert kthLargest.add(5) == 5
    assert kthLargest.add(10) == 5
    assert kthLargest.add(9) == 8
    assert kthLargest.add(4) == 8

    # case 2
    kthLargest = KthLargest(5, [4, 5, 8, 2])
    assert kthLargest.add(3) == 2
    assert kthLargest.add(5) == 3
    assert kthLargest.add(10) == 4
    assert kthLargest.add(9) == 5
    assert kthLargest.add(4) == 5
