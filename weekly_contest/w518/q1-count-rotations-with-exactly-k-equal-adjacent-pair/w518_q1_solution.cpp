#include <string>

using namespace std;

/*
思路：

1. 首先算出原始字符串的得分 s0
2. 然后判断第一个字符与最后一个字符是否相同，记为 s1。若相同，则 s1 = 1，否则 s1 = 0
3. 假设截取点为 i，并且 str[i] == str[i+1], 则旋转后的得分为 s0 + s1 - 1; 否则得分为 s0 + s1；假设不截取，则得分为 s0
4. 若 s1 == 0，则得分只能为 s0 或 s0 - 1，个数分别为：n - s0 和 s0
5. 若 s1 == 1，则得分只能为 s0 或 s0 + 1，个数分别为 s0 + 1 或 n - s0 - 1
*/
class Solution {
public:
  int countRotations(string s, int k) {
    int score = 0;
    for (int i = 0; i < s.size() - 1; i++) {
      if (s[i] == s[i+1]) {
        score++;
      }
    }

    if (s[0] == s[s.size() - 1]) {
      if (k == score) {
        return score + 1;
      } else if (k == score + 1) {
        return s.size() - score - 1;
      } else {
        return 0;
      }
    } else {
      if (k == score) {
        return s.size() - score;
      } else if (k == score - 1) {
        return score;
      } else {
        return 0;
      }
    }
  }
};
