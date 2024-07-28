import math

class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        l_root = int(math.sqrt(l))
        if l_root ** 2 < l:
            l_root += 1
        r_root = int(math.sqrt(r))

        special_count = 0
        for root in range(l_root, r_root + 1):
            if is_prime(root):
                special_count += 1
        return r - l + 1 - special_count

def is_prime(num: int):
    if num <= 2:
        return num == 2

    root = int(math.sqrt(num))
    for i in range(2, root+1):
        if num % i == 0:
            return False
    return True

if __name__ == "__main__":
    solution = Solution()
    assert solution.nonSpecialCount(5, 7) == 3
    assert solution.nonSpecialCount(4, 16) == 11
    assert solution.nonSpecialCount(10086764, 96508040) == 86420515
