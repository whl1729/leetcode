from typing import List

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        s_len = len(s)
        # 注意右边是开区间，即 [i, j)
        totals_of_one = get_totals_of_one(s, s_len)
        num = 0
        for i in range(s_len):
            for j in range(i, s_len):
                num_of_one = totals_of_one[j+1] - totals_of_one[i]
                num_of_zero = j - i + 1 - num_of_one
                if num_of_one >= num_of_zero ** 2:
                    num += 1

        return num

def get_totals_of_one(s: str, s_len: int):
    totals = [0 for _ in range(s_len + 1)]
    for i in range(s_len):
        if s[i] == '1':
            totals[i+1] = totals[i] + 1
        else:
            totals[i+1] = totals[i]
    return totals

if __name__ == "__main__":
    solution = Solution()
    s = '00011'
    assert solution.numberOfSubstrings(s) == 5
    s = '101101'
    assert solution.numberOfSubstrings(s) == 16
