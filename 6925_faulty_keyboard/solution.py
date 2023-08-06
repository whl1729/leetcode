class Solution(object):
    def finalString(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        for ch in s:
            if ch == "i":
                result = "".join(reversed(result))
            else:
                result += ch
        return result

if __name__ == "__main__":
    solution = Solution()
    input = "string"
    output = "rtsng"
    assert(solution.finalString(input) == output)
    input = "poiinter"
    output = "ponter"
    assert(solution.finalString(input) == output)