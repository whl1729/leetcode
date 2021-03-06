# LeetCode 6472 解题报告

## 解题思路

### 思路1：直接法

超时

### 思路2：逆向遍历查询列表，记录已操作过的行或列

超时

### 思路3：

- 每次查询后，立即更新总和
- 问题在于不好更新总和，因为没找到很好的方法记录当前状态
- 目前是以每个元素为单位来考虑问题，可能以行/列为单位来考虑才行

### 思路4：

考虑转化为矩阵运算问题，但似乎有点复杂

### 思路5：

先转化成更简单的问题：

如果只有行运算或列运算，题目都很简单，可以以行/列为单位来处理。

但既有行又有列的时候，似乎只能以每个元素为单位来考虑问题

### 思路6：

先分析当前的时间复杂度，再考虑优化方向：

更新矩阵的时间复杂度为 O(M*n)，其中M为查询次数，n为矩阵的维度
计算矩阵的时间复杂度为 O(n^2)

优化方向：计算矩阵的时间复杂度可以优化掉。

## 总结

最终按照思路6优化代码后 Accept 了。这次解题经历提供了新的经验：

有时候解决超时问题，不一定要从原理层面做优化，可以从代码层面做优化。
事实上，有了思路6后，我回头看代码，从消除内层循环的动机出发，很快就找到优化方案。这个优化方案是看代码才容易想到的，如果不看代码，空想反而不容易想出来。

这也提醒我们，先找到一个可行但不完美的解法，在此基础上进行优化，也是解决问题的一个思路。