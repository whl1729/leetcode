class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # 树叶节点：具有前驱的节点
        leaf = {edge[1] for edge in edges}
        return [i for i in range(0, n) if i not in leaf]


if __name__ == "__main__":
    solution = Solution()
    n = 6
    edges = [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]
    output = [0, 3]
    assert solution.findSmallestSetOfVertices(n, edges) == output
    n = 5
    edges = [[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]
    output = [0, 2, 3]
    assert solution.findSmallestSetOfVertices(n, edges) == output
