class Solution(object):
    def removeTrailingZeros(self, num):
        """
        :type num: str
        :rtype: str
        """
        return num.strip('0')

if __name__ == "__main__":
    solution = Solution()
    assert solution.removeTrailingZeros('51230100') == '512301'
    assert solution.removeTrailingZeros('123') == '123'
    assert solution.removeTrailingZeros('1000') == '1'
    assert solution.removeTrailingZeros('1020304050') == '102030405'