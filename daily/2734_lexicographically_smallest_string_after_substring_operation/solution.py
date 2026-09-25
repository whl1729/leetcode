def prev(s):
    return ''.join([chr(ord('a') + (ord(c) - ord('a') + 25) % 26) for c in s])

class Solution(object):
    def smallestString(self, s):
        """
        :type s: str
        :rtype: str

        Note: 找出第一个不是a的字母作为起点，然后一直往后直到遇到a结束
        """
        start = len(s) - 1
        end = len(s)
        for i, ch in enumerate(s):
            if ch != 'a':
                start = i
                break
        
        for i, ch in enumerate(s[start+1:]):
            if ch == 'a':
                end = start + 1 + i
                break
        
        return s[:start] + prev(s[start: end]) + s[end:]

if __name__ == "__main__":
    solution = Solution()
    assert solution.smallestString('cbabc') == 'baabc'
    assert solution.smallestString('acbbc') == 'abaab'
    assert solution.smallestString('leetcode') == 'kddsbncd'
    assert solution.smallestString('a') == 'z'
    assert solution.smallestString('aa') == 'az'
    assert solution.smallestString('z') == 'y'