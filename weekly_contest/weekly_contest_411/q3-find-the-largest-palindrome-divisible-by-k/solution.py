class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        largest = 10 ** n
        for n in reversed(range(k, largest)):
            if is_palindrome(n) and n % k == 0:
                return str(n)

def is_palindrome(n: int) -> bool:
    return reverse(n) == n

def reverse(n: int) -> int:
    result = 0
    while n > 0:
        r = n % 10
        n = n // 10
        result = result * 10 + r

    return result


if __name__ == "__main__":
    assert reverse(123) == 321
    assert reverse(12) == 21
    assert is_palindrome(1) == True
    assert is_palindrome(22) == True
    assert is_palindrome(121) == True
    assert is_palindrome(3883) == True

    s = Solution()
    result = s.largestPalindrome(3, 5)
    assert result == "595"

    result = s.largestPalindrome(1, 4)
    assert result == "8"

    result = s.largestPalindrome(5, 6)
    assert result == "89898"