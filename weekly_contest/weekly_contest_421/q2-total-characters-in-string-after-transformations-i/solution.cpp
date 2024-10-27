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
      int r = t % 26;
      vector<int> counts = count_letter(s);
      int len = accumulate(counts.begin(), counts.end(), 0);
      // 计算时刻 r 的长度
      len += accumulate(counts.end() - r, counts.end(), 0);
      int q = t / 26;
      for (int i = 0; i < q; i++) {
        len = (len * 2) % modulo;
      }

      return len;
    }

    // 统计字符串 26 个字母分别有多少个
    vector<int> count_letter(string s) {
      vector<int> counts(26, 0);
      for (char &c: s) {
        counts[c - 'a'] += 1;
      }
      return counts;
    }
};

int main() {
  auto s = Solution();

  assert(s.lengthAfterTransformations("abcyy", 2));
  assert(s.lengthAfterTransformations("azbk", 1));

  return 0;
}