class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        """
        :type words: List[str]
        :type separator: str
        :rtype: List[str]
        """
        result = []
        for word in words:
           for token in word.split(separator):
               if len(token) > 0:
                   result.append(token)
        return result

if __name__ == "__main__":
    solution = Solution()
    
    words = ["one.two.three","four.five","six"]
    separator = "."
    output = ["one","two","three","four","five","six"]
    assert solution.splitWordsBySeparator(words, separator) == output

    words = ["$easy$","$problem$"]
    separator = "$"
    output = ["easy","problem"]
    assert solution.splitWordsBySeparator(words, separator) == output

    words = ["|||"]
    separator = "|"
    output = []
    assert solution.splitWordsBySeparator(words, separator) == output