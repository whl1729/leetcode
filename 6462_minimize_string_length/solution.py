class Solution(object):
    def minimizedStringLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(set(s))

if __name__ == "__main__":
    solution = Solution()
    assert solution.minimizedStringLength('aaabc') == 3
    assert solution.minimizedStringLength('cbbd') == 3
    assert solution.minimizedStringLength('dddaaa') == 2