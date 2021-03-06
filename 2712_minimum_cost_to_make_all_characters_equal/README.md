# LeetCode 2712 解题报告

## 思路分析过程

### 思路1：化简

首先将问题化简一下：先不要求最小代价，如何找到一个解决方案？
这个不难解决，比如以下是一个可行的算法（称为算法1）：

1. 从末尾往回找，当找到 s[i] != s[i-1] 时，将[i, n-1] 翻转
2. 从i-1继续往回找，一直重复步骤1的步骤即可。

这个是单方向的，很容易想到一个双方向的算法（称为算法2）：

1. 从两个方向找，找到跳变的地方，选择代价小的一头进行翻转
2. 重复步骤1，直到没有跳变的地方

### 思路2：观察 Example 2

Example 2 的最优方案跟我的思路1有所不同，主要体现在前2步：
Example 2 的前2步是让中间先出现相同的字符，再来处理两边。
不过按照思路1来做 Example 2 也能得到最小代价。
现在的问题是如何找到最小代价，并且证明它是最小代价。

### 思路3：分治法

思考能否分解成小规模的问题来讨论。

首先，很容易观察到以下两种情况：

- 当长度为2时，如果两个字符不同，那么代价为1
- 当字符串可以分为两部分，每部分的所有字符相同，但这两部分字符不同，那么代价为 min(len(s1), len(s2))

然后，思考长度为 n 的字符串长度增加1后，最小代价会怎样变化：

- 假如第 n+1 个字符跟前n个字符串完成翻转后的字符相同，那么 min_cost(n+1) = min_cost(n)
- 假如第 n+1 个字符跟前n个字符串完成翻转后的字符不同，那么 min_cost(n+1) = min_cost(n) 或 min_cost(n) + 1

这规律不太好推，不容易找出递推式。因为不好确认是哪一种情况。

### 思路4：理论推导各个字符的代价

根据题意，每次只能进行两种操作之一（不妨编号为0和1），要使代价最小，应该尽可能做到以下几点：

- 操作总次数尽可能少
- 对某个字符进行操作时，应该选择较短的一边来反转
- 尽量减少中间的元素的操作次数（因为中间的元素操作一次的代价最大）

还有一个猜想是：

- 选择出现次数不少于一半的字符作为最终翻转目标（假命题，反例：110011）

如果不确定最终翻转目标是0还是1，可以分别计算两种情况的最小代价，取最小值即可。

此时，我好像已经找到解决方案了：

从中间往两边拓展，分别计算每个字符的最小代价即可。

虽然尚未做出严格证明，但已经能看出用贪婪算法来处理就可以了。先写代码试试吧。

## 总结

思路四是正确的。反思一下思路4是怎么推出来的，突破口在哪里：

其实就是围绕目标「最小代价」去思考，思考**最终答案应该具有的特征/模式**