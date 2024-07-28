import math

class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        count = 0
        for i in range(l, r+1):
            if not is_special(i):
                count += 1
        return count

def is_special(num: int):
    root = int(math.sqrt(num))
    return root ** 2 == num and is_prime(root)

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
