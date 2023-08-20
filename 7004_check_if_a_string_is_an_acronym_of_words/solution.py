class Solution(object):
    def isAcronym(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: bool
        """
        acronym = ''.join([w[0] for w in words])
        return acronym == s

if __name__ == "__main__":
    solution = Solution()
    words = ["alice","bob","charlie"]
    s = "abc"
    assert solution.isAcronym(words, s)
    words = ["an","apple"]
    s = "a"
    assert solution.isAcronym(words, s) == False
    words = ["never","gonna","give","up","on","you"]
    s = "ngguoy"
    assert solution.isAcronym(words, s)
