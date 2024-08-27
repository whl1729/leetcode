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
        # print(f'items: {items}')
        diffs = self.calc_diffs(items)
        # print(f'diffs: {diffs}')
        self.operates(items, diffs, k)
        # print(f'operated items: {items}')
        items.sort(key=lambda x: x.index)
        # print(f'sorted items: {items}')

        final_state = [modular_pow(num, multiplier, items[i].count, DIVISOR) for i, num in enumerate(nums)]
        # print(f'final_state: {final_state}')
        return final_state

    def sort_nums(self, nums: List[int], multiplier: int) -> List[Item]:
        """将 int 数组转化为 item 数组再排序，以保留数组下标信息"""
        items = [Item(index=i, log=math.log(num, multiplier), count=0) for i, num in enumerate(nums)]
        items.sort(key=lambda x: x.log)
        return items

    def calc_diffs(self, items: List[Item]) -> List[List[int]]:
        """计算任意两个 item 之间的对数值的差异，并向上取整"""
        length = len(items)
        diffs = [[0 for _ in range(length)] for _ in range(length)]
        for i in range(length):
            for j in range(i+1, length):
                diffs[i][j] = math.ceil(items[j].log - items[i].log)

        return diffs
        
    def operates(self, items: List[Item], diffs: List[List[int]], k: int) -> None:
        length = len(diffs)
        round, left = self.calc_round(diffs, k, length)
        # print(f'round={round}, left={left}')
        q, r = left // round, left % round
        for i in range(round):
            items[i].count = diffs[i][round-1] + q
            items[i].log += items[i].count
        # print(f'after round, items: {items}')

        allocated_items = items[:round]
        allocated_items.sort(key=lambda x: x.index)
        allocated_items.sort(key=lambda x: x.log)

        for i in range(r):
            allocated_items[i].count += 1
            allocated_items[i].log += 1

    def calc_round(self, diffs: List[List[int]], k: int, length: int) -> Tuple[int, int]:
        """计算能够进行几轮分配"""
        last_allocated = 0
        for round in range(1, length):
            cur_allocated = sum(d[round] for d in diffs)
            if cur_allocated > k:
                return round, (k - last_allocated)
            last_allocated = cur_allocated

        return length, (k - last_allocated)


if __name__ == "__main__":
    s = Solution()
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