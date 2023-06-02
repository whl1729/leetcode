def binaryReverse(ch):
    return "0" if ch == "1" else "1"


class Solution(object):
    def minimumCost(self, s):
        """
        :type s: str
        :rtype: int
        """
        return min(self._minCostOfAll(s, "0"), self._minCostOfAll(s, "1"))

    def _minCostOfAll(self, s, target):
        """Minimum cost to make all characters equal to target
        Args:
            s: 0-indexed binary string
            target: '0' or '1'
        """
        middle = int(len(s) / 2)
        return self._minCostOfLeft(s, 0, middle, target) + self._minCostOfRight(
            s, middle, len(s), target
        )

    def _minCostOfLeft(self, s, start, end, target):
        cost = 0
        reverse_cnt = 0
        for i in reversed(range(start, end)):
            # 如果当前字符右边的字符共进行了奇数次翻转，则当前字符的值已被翻转，需要先更新
            ch = binaryReverse(s[i]) if reverse_cnt % 2 == 1 else s[i]
            if ch != target:
                # 如果更新后的当前字符与目标字符不同，需要再翻转一次
                cost += i + 1
                reverse_cnt += 1
        return cost

    def _minCostOfRight(self, s, start, end, target):
        cost = 0
        reverse_cnt = 0
        for i in range(start, end):
            # 如果当前字符左边的字符共进行了奇数次翻转，则当前字符的值已被翻转，需要先更新
            ch = binaryReverse(s[i]) if reverse_cnt % 2 == 1 else s[i]
            if ch != target:
                # 如果更新后的当前字符与目标字符不同，需要再翻转一次
                cost += len(s) - i
                reverse_cnt += 1
        return cost


if __name__ == "__main__":
    solution = Solution()
    assert solution.minimumCost("0011") == 2
    assert solution.minimumCost("010101") == 9
    assert solution.minimumCost("110011") == 4
