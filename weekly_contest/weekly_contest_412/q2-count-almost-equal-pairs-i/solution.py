from typing import List

def swap_set(num: int) -> List[int]:
    num_str = list(str(num))
    result = []
    for i in range(len(num_str)):
        for j in range(i+1, len(num_str)):
            cur_str = [c for c in num_str]
            cur_str[i], cur_str[j] = num_str[j], num_str[i]
            result.append(int(''.join(cur_str)))

    return result

class Solution:
    def countPairs(self, nums: List[int]) -> int:
        size = len(nums)
        count = 0
        for i in range(size):
            for j in range(i+1, size):
                if self.almost_equal(nums[i], nums[j]):
                    count += 1

        return count

    def almost_equal(self, first: int, second: int) -> bool:
        if first == second:
            return True

        if first in swap_set(second) or second in swap_set(first):
            return True

        return False

if __name__ == "__main__":
    s = Solution()
    nums = [3,12,30,17,21]
    assert s.countPairs(nums) == 2
    nums = [1,1,1,1,1]
    assert s.countPairs(nums) == 10
    nums = [123,231]
    assert s.countPairs(nums) == 0
