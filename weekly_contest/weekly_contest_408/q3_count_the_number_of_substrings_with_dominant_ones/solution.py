from typing import List

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        s_len = len(s)
        nums_of_one = numbers_of_one(s, s_len)
        total = 0
        # 注意右边是开区间，即 [i, j)
        for i in range(s_len):
            for j in range(i+1, s_len+1):
                num_of_one = nums_of_one[i][j]
                num_of_zero = j - i - num_of_one
                if num_of_one >= num_of_zero ** 2:
                    total += 1
        return total

def numbers_of_one(s: str, s_len: int) -> List[List[int]]:
    result = [[0 for _ in range(s_len+1)] for _ in range(s_len)]
    for i in range(s_len):
        for j in range(i+1, s_len+1):
            if s[j-1] == '1':
                result[i][j] = result[i][j-1] + 1
            else:
                result[i][j] = result[i][j-1]

    return result

if __name__ == "__main__":
    solution = Solution()
    assert solution.numberOfSubstrings("00011") == 5
    assert solution.numberOfSubstrings("101101") == 16