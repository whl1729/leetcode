#include <string>
#include <unordered_map>

using namespace std;

/**
 * 思路：
 * 1. 定义一个 map，记录每个字母的最新下标。
 * 2. 定义 start 和 end，分别对应当前子串的起始和终止位置
 * 3. 遍历字符串，若当前字符没出现在 map 中，则更新子串的长度；否则更新 start
 */
class Solution {
public:
  int lengthOfLongestSubstring(string s) {
    if (s.empty()) {
      return 0;
    }

    unordered_map<char, int> char_index_map;
    int start = 0;
    int max_len = 0;

    for (int i = 0; i < s.size(); i++) {
      auto it = char_index_map.find(s[i]);
      if (it != char_index_map.end() && it->second >= start) {
        max_len = max(max_len, i - start);
        start = it->second + 1;
      }
      char_index_map[s[i]] = i;
    }

    max_len = max(max_len, int(s.size()) - start);

    return max_len;
  }
};