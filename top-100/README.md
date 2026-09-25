# LeetCode Top 100 刷题记录

## 没有思路的题目

- 0103 最长连续序列：只想到排序，复杂度是 O(nlogn)，超出要求。最终看了官方思路

## 易忘的知识点

- 查询集合中是否包含某个元素

```cpp
#include <iostream>
#include <unordered_set>

std::unordered_set<int> us{1, 3, 5, 7};
if (us.count(1)) {
  std::cout << " The set contains 1" << std::endl;
}
```

- 字符串排序

```cpp
#include <algorithm>
#include <string>

std::string str = "hello, world";
std::sort(str.begin(), str.end());
```

- 遍历 unordered_map

```cpp
#include <iostream>
#include <unordered_map>
#include <string>

std::unordered_map<std::string, int> myMap;
for (const auto& [key, value] : myMap) {
  std::cout << key << ": " << value << "\n";
}
```