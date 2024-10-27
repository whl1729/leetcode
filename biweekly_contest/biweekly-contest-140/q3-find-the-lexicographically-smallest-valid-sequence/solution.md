# LeetCode 题目 3302 解题报告

题目链接：[3302. Find the Lexicographically Smallest Valid Sequence][3302]

## 最终解法

- 首先计算出一个数组 A[n]，其中 A[i] 代表从 word1 的 第 i 位至最后一位能够反向匹配 word2 的最小下标。
  - 所谓「反向匹配」，指从 word1 与 word2 的最后一位开始扫描，维护两个下标 index1 和 index2，分别代表 word1 的扫描位置与 word2 的匹配位置
  - 所谓「最小下标」，指：比如 word2 长度为 4，word1 从后面往回至第 i 位最终能够匹配 word2 的第 1~3 位，则最小下标为 1

- 然后再正向扫描一遍，扫描时如果 word1 与 word2 的当前位置不能匹配，则考虑是否需要用掉修改机会，考虑依据如下：
  - 如果之前已经用掉修改机会，那就不能再用了（因为题目只允许修改一次）
  - 如果 word1 与 word2 的剩余字符串能够匹配（结合数组A判断已匹配下标是否大于反向匹配的下标即可），则立即用掉修改机会（因为修改得越早，字典序越小）

## 解题过程

1. 一开始我先考虑没有修改机会的场景，也就是普通的字符串匹配问题，这个问题很好解决——扫描一遍即可。

2. 然后我假设 word1 的任意一位为修改位置，从而将问题转化为第1点的问题，但由于两层循环，复杂度为 `O(n^2)`，超时了。

3. 6天后，我考虑使用动态规划的思想，试图寻找重复子问题结构，但由于不确定修改位置，导致没法找到递推式。

4. 想了一个多小时，我开始考虑反向匹配的思路，但还是没法形成清晰的算法。

5. 后来我躺在床上想：这道题麻烦的地方在于正向匹配的时候，不知道什么时候使用修改机会，如果提前用掉修改机会，导致后面无法匹配，就会出问题。**有没有办法快速确认当前能否用掉修改机会呢？**

6. 提出这个问题后，我很快发现反向匹配正是解决这个问题的好方法。于是我知道我找到这道题的解法了。

## 解题总结

1. 解题时，如果发现题目跟以前做过的题目有一些相似点，可以先解决旧题目，再思考旧题目与新题目之间的联系。

2. 解题时，多确认现在的困难是什么，围绕如何克服这个困难去寻找可能的解法。

3. 这道题用到「动态规划」，但这道题的关键并非运用「动态规划」，而是找到修改位置的判断依据。

4. 如果题目不容易找到「重复子问题结构」，那么「动态规划」就可能不是突破口了，需要找到其他的突破口。

  [3302]: https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/description/