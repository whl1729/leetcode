#include <vector>
#include <string>
#include <cassert>

using namespace std;

class Solution {
  public:
    vector<int> validSequence(string word1, string word2) {
      auto back_matched_pos = calc_back_matched_pos(word1, word2);
      int len1 = word1.length();
      int len2 = word2.length();
      // 是否已经修改了一次字符
      bool changed = false;
      // 正在匹配 word2 的子字符串的位置
      int matching_pos = 0;
      vector<int> indices(len2);

      for (int i = 0; i < len1; i++) {
        if (word1[i] == word2[matching_pos]) {
          indices[matching_pos] = i;
          matching_pos++;
        } else if ((!changed) && (back_matched_pos[i+1] <= matching_pos + 1)) {
          // 如果 word1 后面的字符串还能够匹配 word2 剩余的字符串，就用掉修改机会
          indices[matching_pos] = i;
          matching_pos++;
          changed = true;
        }
        if (matching_pos == len2) {
          return indices;
        }
      }

      return vector<int>{};
    }

    // 返回数组 L[n]，其中 L[i] 表示从 word1 第 i 位开始能够后向匹配 word2 的下标
    // 所谓后向匹配，指从 word1 和 word2 的最后一位往回匹配
    vector<int> calc_back_matched_pos(string word1, string word2) {
      int len1 = word1.length();
      int len2 = word2.length();
      // 加1是用作哨兵
      vector<int> matched_pos(len1+1, 0);

      // 已经匹配 word2 的子字符串的位置
      int cur_matched_pos = len2;
      for (int i = len1 - 1; i >= 0 && cur_matched_pos > 0; i--) {
        if (word1[i] == word2[cur_matched_pos - 1]) {
          cur_matched_pos--;
        }

        matched_pos[i] = cur_matched_pos;
      }

      return matched_pos;
    }
};

int main() {
  vector<int> result;
  vector<int> expected;
  auto s = Solution();

  result = s.validSequence("cbcbccbbcbcbbbb", "bb"); 
  expected = vector<int>{0, 1};
  assert(result == expected);

  result = s.validSequence("vbcca", "abc"); 
  expected = vector<int>{0, 1, 2};
  assert(result == expected);

  result = s.validSequence("bacdc", "abc"); 
  expected = vector<int>{1, 2, 4};
  assert(result == expected);

  result = s.validSequence("aaaaaa", "aaabc"); 
  expected = vector<int>{};
  assert(result == expected);

  result = s.validSequence("abc", "ab"); 
  expected = vector<int>{0, 1};
  assert(result == expected);

  return 0;
}