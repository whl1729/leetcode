import math
from typing import List
from typing import Tuple
from dataclasses import dataclass

DIVISOR = 10**9 + 7

@dataclass
class Item:
    # 数组下标
    index: int
    # 对数值
    log: float
    # 操作次数
    count: int

def modular_pow(initial, base, exponent, modulus):
    result = 1
    base = base % modulus
    
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    
    result = (result * initial) % modulus
    return result

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        """
        算法：
            1. 将列表元素转化为 base 为 multiplier 的对数，从而将乘法转化为加法
            2. 计算出每个元素的操作次数
                2.1 将列表元素排序，记为 a
                2.2 计算任意两个元素的（对数）差值，记为 d[i,j]，代表 a[j] - a[i]
                2.3 将原问题转化为分配操作次数，并分为 n 轮：第 i 轮分配使得前 i 个元素相差小于 1
            3. 计算出每个元素 mod (10^9 + 7) 的结果

        """
        if multiplier == 1:
            return nums

        items = self.sort_nums(nums, multiplier)
        self.operates(items, k)
        items.sort(key=lambda x: x.index)

        final_state = [modular_pow(num, multiplier, items[i].count, DIVISOR) for i, num in enumerate(nums)]
        return final_state

    def sort_nums(self, nums: List[int], multiplier: int) -> List[Item]:
        """将 int 数组转化为 item 数组再排序，以保留数组下标信息"""
        items = [Item(index=i, log=round(math.log(num, multiplier), 10), count=0) for i, num in enumerate(nums)]
        items.sort(key=lambda x: x.log)
        return items

    def operates(self, items: List[Item], k: int) -> None:
        length = len(items)
        round, left = self.calc_round(items, k, length)
        q, r = left // round, left % round
        for i in range(round):
            items[i].count = math.ceil(items[round-1].log - items[i].log) + q
            items[i].log += items[i].count

        allocated_items = items[:round]
        allocated_items.sort(key=lambda x: x.index)
        allocated_items.sort(key=lambda x: x.log)

        for i in range(r):
            allocated_items[i].count += 1
            allocated_items[i].log += 1

    def calc_round(self, items: List[Item], k: int, length: int) -> Tuple[int, int]:
        """计算能够进行几轮分配，返回的 round 代表前 round 个元素已经相差小于1"""
        operation_count = lambda round: sum([math.ceil(items[round].log - items[i].log) for i in range(round)])
        # 使用二分搜索
        left = 1
        right = length - 1
        while left <= right:
            mid = (left + right) // 2
            mid_count = operation_count(mid)
            if mid_count == k:
                return mid+1, 0
            if mid_count < k:
                left = mid + 1
                continue
            mid_minus_one_count = operation_count(mid - 1)
            if mid_minus_one_count <= k:
                return mid, (k - mid_minus_one_count)
            right = mid - 1

        return length, (k - operation_count(length - 1))


if __name__ == "__main__":
    s = Solution()
    nums = [5,1]
    k = 2
    multiplier = 3
    result = s.getFinalState(nums, k, multiplier)
    assert result == [5,9]

    nums = [2,1,3,5,6]
    k = 5
    multiplier = 2
    result = s.getFinalState(nums, k, multiplier)
    assert result == [8,4,6,5,6]

    nums = [100000,2000]
    k = 2
    multiplier = 1000000
    result = s.getFinalState(nums, k, multiplier)
    assert result == [999999307,999999993]

    nums = [3,9,27,81,243,729,2187,6561,19683,59049,177147,531441,1594323,4782969,14348907,43046721,129140163,387420489]
    k = 1000000000
    multiplier = 3
    result = s.getFinalState(nums, k, multiplier)
    assert result == [869770420,623256809,623256809,623256809,623256809,623256809,623256809,623256809,623256809,623256809,623256809,623256809,623256809,623256809,623256809,623256809,623256809,623256809]