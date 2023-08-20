class Solution(object):
    def minimumSum(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        s = set()
        total = 0
        size = 0
        cur = 1
        while size < n:
            if (k - cur) not in s:
                s.add(cur)
                total += cur
                size += 1
            cur += 1
        return total

        
if __name__ == "__main__":
    solution = Solution()
    assert solution.minimumSum(5, 4) == 18
    assert solution.minimumSum(2, 6) == 3