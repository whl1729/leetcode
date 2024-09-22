class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        if n % 2 == 0:
            return self._count_good_integers_even(n, k)

        return self._count_good_integers_even(n, k)

    def _count_good_integers_even(self, n: int) -> int:
        half = n // 2
        start = 10 ** half
        end = start * 10 - 1
        good_nums = set()
        for i in range(start, end):
            palindrome = self._get_palindrome(i)
            cur_good_nums = self._get_good_nums(palindrome)
            good_nums.update(cur_good_nums)
        return len(good_nums)

    def _get_palindrome(self, half: int) -> int:
        pass

    def _get_good_nums(self, palindrome: int) -> int:
        pass

    def _is_divided(self, palindrome) -> bool:
        pass

    def _count_good_integers_odd(self, n: int) -> int:
        half = (n - 1) // 2
        start = 10 ** half
        end = start * 10 - 1
        good_nums = set()
        for i in range(start, end):
            palindrome = self._get_palindrome(i)
            cur_good_nums = self._get_good_nums(palindrome)
            good_nums.update(cur_good_nums)
        return len(good_nums)

    def _get_half(self, n: int) -> int:
        for


if __name__ == "__main__":
    s = Solution()
    assert s.countGoodIntegers(1, 1) == 9
    assert s.countGoodIntegers(2, 1) == 9
    assert s.countGoodIntegers(3, 1) == 90
    # assert s.countGoodIntegers(3, 5) == 27
    # assert s.countGoodIntegers(1, 4) == 2
    # assert s.countGoodIntegers(5, 6) == 2468