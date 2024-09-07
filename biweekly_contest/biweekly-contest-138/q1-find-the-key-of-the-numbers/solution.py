class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        nums = [num1, num2, num3]
        modulo = 1000
        result = 0
        for _ in range(4):
            min_digit = 9
            for i, num in enumerate(nums):
                cur_digit = num // modulo
                nums[i] = num % modulo
                if cur_digit < min_digit:
                    min_digit = cur_digit

            result += min_digit * modulo
            modulo //= 10

        return result


if __name__ == "__main__":
    s = Solution()
    assert s.generateKey(987, 879, 798) == 777
    assert s.generateKey(1,2,3) == 1
    assert s.generateKey(1, 12, 123) == 1
    assert s.generateKey(1, 21, 321) == 1
    assert s.generateKey(31, 21, 321) == 21