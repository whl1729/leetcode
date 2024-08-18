class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        s_len = len(s)
        result = 0
        for i in range(s_len):
            num_0 = 0
            num_1 = 0
            for j in range(i, s_len):
                if s[j] == '0':
                    num_0 += 1
                else:
                    num_1 += 1
                if num_0 <= k or num_1 <= k:
                    result += 1

        return result

if __name__ == "__main__":
    count = Solution().countKConstraintSubstrings
    result = count("10101", 1)
    assert result == 12
    result = count("1010101", 2)
    assert result == 25
    result = count("11111", 1)
    assert result == 15