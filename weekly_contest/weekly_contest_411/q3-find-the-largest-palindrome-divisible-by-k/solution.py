class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        if k == 1 or k == 3 or k == 9:
            # 99..9
            return '9' * n

        if k == 2:
            # 89..98
            if n <= 2:
                return '8' * n
            return '8' + '9' * (n-2) + '8'

        if k == 4:
            if n <= 4:
                return '8' * n
            return '88' + '9' * (n-4) + '88'

        if k == 8:
            if n <= 6:
                return '8' * n
            return '8' * 3 + '9' * (n-6) + '8' * 3

        if k == 5:
            # 59..95
            if n <= 2:
                return '5' * n
            return '5' + '9' * (n-2) + '5'

        if k == 6:
            if n <= 2:
                return '6' * n

            if n % 2 == 0:
                # 89..9779..98
                num = (n-4) // 2
                return '8' + '9' * num + '77' + '9' * num + '8'

            # 89..989..98
            num = (n-3) // 2
            return '8' + '9' * num + '8' + '9' * num + '8'

        if k == 7:
            if n <= 2:
                return '7' * n

            # 9..9a9..9
            # or: 9..9aa9..9
            num = (n-1) // 2
            middle = self.get_middle(n, num)
            return '9' * num + middle + '9' * num

    def get_middle(self, n, num):
        # 记录 10^i % 7 的取值（周期位 6）
        factors = [1, 3, 2, 6, 4, 5, 1, 3]
        k = num % 6
        if n % 2 == 1:
            # remainder = (10^c - 1) * (10^(c+1) + 1) + a * 10^c
            # remainder = (f[k] - 1) * (f[k+1] + 1) + a * f[k]
            for i in reversed(range(10)):
                remainder = (factors[k] - 1) * (factors[k+1] + 1) + i * factors[k]
                if remainder % 7 == 0:
                    return str(i)

        # remainder = (10^c - 1) * (10^(c+2) + 1) + 4a * 10^c
        # remainder = (f[k] - 1) * (f[k+2] + 1) + 4a * f[k]
        for i in reversed(range(10)):
            remainder = (factors[k] - 1) * (factors[k+2] + 1) + 4 * i * factors[k]
            if remainder % 7 == 0:
                return str(i) * 2


if __name__ == "__main__":
    s = Solution()
    result = s.largestPalindrome(3, 5)
    assert result == "595"

    result = s.largestPalindrome(1, 4)
    assert result == "8"

    result = s.largestPalindrome(5, 4)
    assert result == "88988"

    result = s.largestPalindrome(6, 4)
    assert result == "889988"

    result = s.largestPalindrome(7, 8)
    assert result == "8889888"

    result = s.largestPalindrome(1, 8)
    assert result == "8"

    result = s.largestPalindrome(3, 6)
    assert result == "888"

    result = s.largestPalindrome(4, 6)
    assert result == "8778"

    result = s.largestPalindrome(5, 6)
    assert result == "89898"

    result = s.largestPalindrome(6, 6)
    assert result == "897798"

    result = s.largestPalindrome(5, 7)
    assert result == "99799"

    result = s.largestPalindrome(6, 7)
    assert result == "999999"

    result = s.largestPalindrome(7, 7)
    assert result == "9994999"

    result = s.largestPalindrome(8, 7)
    assert result == "99944999"

    result = s.largestPalindrome(9, 7)
    assert result == "999969999"