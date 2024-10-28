#include <cassert>
#include <numeric>
#include <string>
#include <vector>

using namespace std;

// 英文字母一共有 26 个
const int letter_num = 26;

const int modulo = 1000000007;

class Solution {
  public:
    int lengthAfterTransformations(string s, int t) {
      vector<int> counts = count_letter(s);
      vector<int> lens(t+1, 0);
      init_lens(lens, counts);
      for (int i = letter_num; i <= t; i++) {
        lens[i] = (lens[i- letter_num] + lens[i - letter_num + 1]) % modulo;
      }

      return lens[t];
    }

    // 统计字符串 26 个字母分别有多少个
    vector<int> count_letter(string s) {
      vector<int> counts(26, 0);
      for (char &c: s) {
        counts[c - 'a'] += 1;
      }
      return counts;
    }

    // 初始化 T = 0 ~ min(26,t) 时刻的长度
    void init_lens(vector<int> &lens, vector<int> &counts) {
      lens[0] = accumulate(counts.begin(), counts.end(), 0);
      int init_len = (lens.size() > letter_num) ? letter_num : lens.size();
      for (int i = 1; i < init_len; i++) {
        lens[i] = lens[i-1] + counts[letter_num - i];
      }
    }
};

int main() {
  auto s = Solution();
  int result;

  result = s.lengthAfterTransformations("jqktcurgdvlibczdsvnsg", 7517);
  assert(result == 79033769);

  assert(s.lengthAfterTransformations("abcyy", 2) == 7);
  assert(s.lengthAfterTransformations("azbk", 1) == 5);

  return 0;
}