# LeetCode Top 100 刷题记录

## 易忘的知识点

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