#include <vector>
#include <string>

using namespace std;

class Solution {
  public:
    vector<int> validSequence(string word1, string word2) {
      int len1 = word1.length();
      for (int change_pos = 0; change_pos < len1; change_pos++) {
        auto sequence = find_valid_sequence(word1, word2, change_pos);
        if (!sequence.empty()) {
          return sequence;
        }
      }

      return vector<int>{};
    }

    vector<int> find_valid_sequence(string word1, string word2, int change_pos) {
      int len1 = word1.length();
      int len2 = word2.length();
      // 正在匹配 word2 的子字符串的位置
      int matched_pos = 0;
      vector<int> indices(len2);

      for (int i = 0; i < len1; i++) {
        if (word1[i] == word2[matched_pos]) {
          indices[matched_pos] = i;
          matched_pos += 1;
          // 如果 change_pos 的位置刚好不需要修改，那么就将修改机会留给后面的元素
          if (i == change_pos) {
            change_pos += 1;
          }
        } else if (i == change_pos) {
          indices[matched_pos] = i;
          matched_pos += 1;
        }
        if (matched_pos == len2) {
          return indices;
        }
      }

      return vector<int>{};
    }
};