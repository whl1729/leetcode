from typing import List

def get_digits(num: int) -> int:
    digits = []
    while num > 0:
        r = num % 10
        num //= 10
        digits.insert(0, r)

    return digits


def swap(num: int, digits: list, i: int, j: int) -> int:
    digit_len = len(digits)
    i = digit_len - 1 - i
    j = digit_len - 1 - j
    # d[i] * (10 ** i) + d[j] * (10 ** j)
    # d[j] * (10 ** i) + d[i] * (10 ** j)
    return num + digits[j] * (10 ** i) + digits[i] * (10 ** j) - digits[i] * (10 ** i) - digits[j] * (10 ** j)

class Solution:
    def countPairs(self, nums: List[int]) -> int:
        size = len(nums)
        count = 0
        for i in range(size):
            for j in range(i, size):
                if self.almost_equal(nums[i], nums[j]):
                    count += 1

        return count

    def almost_equal(self, first: int, second: int) -> bool:
        if first == second:
            return True

        if first < second:
            first, second = second, first

        digits = get_digits(first)
        digit_len = len(digits)
        for i in range(digit_len):
            for j in range(i, digit_len):
                if swap(first, digits, i, j) == second:
                    return True

        return False

if __name__ == "__main__":
    assert get_digits(12345) == [1,2,3,4,5]
    assert get_digits(300) == [3,0,0]
    result = swap(123, [1,2,3], 0, 2)
    print(result)
    assert swap(123, [1,2,3], 0, 2) == 321
    assert swap(1230, [1,2,3, 0], 0, 3) == 231