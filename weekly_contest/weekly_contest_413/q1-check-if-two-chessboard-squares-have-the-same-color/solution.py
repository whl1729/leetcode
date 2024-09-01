class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        # 颜色与坐标之和的奇偶性对应
        letter_to_digits = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
        return ((letter_to_digits[coordinate1[0]] + int(coordinate1[1])) % 2) == ((letter_to_digits[coordinate2[0]] + int(coordinate2[1])) % 2)
        

if __name__ == "__main__":
    s = Solution()
    assert s.checkTwoChessboards("a1", "c3") == True
    assert s.checkTwoChessboards("a1", "h3") == False
