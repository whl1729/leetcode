class Solution:
    def stringHash(self, s: str, k: int) -> str:
        alpha_list = 'abcdefghijklmnopqrstuvwxyz'
        table = {}
        for i, alpha in enumerate(alpha_list):
            table[alpha] = i

        result = ""
        length = len(s)
        count = length // k
        for i in range(count):
            start = i * k
            end = start + k
            hashedChar = sum([table[c] for c in s[start:end]]) % 26
            result += alpha_list[hashedChar]

        return result

if __name__ == "__main__":
    s = Solution()
    assert s.stringHash("abcd", 2) == "bf"
    assert s.stringHash("mxz", 3) == "i"
