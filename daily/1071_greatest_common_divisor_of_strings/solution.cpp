#include <stdio.h>
#include <string>

using namespace std;

class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
      if (str1.length() < str2.length()) {
        return gcdOfOrderedStrings(str2, str1);
      }

      return gcdOfOrderedStrings(str1, str2);
    }

    string gcdOfOrderedStrings(string longer, string shorter) {
      int llen = longer.length();
      int slen = shorter.length();
      string cur;
      for (int i = slen; i > 0; i--) {
        if ((llen % i) > 0 || (slen % i ) > 0) {
          continue;
        }

        cur = shorter.substr(0, i);
        if (divides(longer, cur) && (divides(shorter, cur))) {
          return cur;
        }
      }

      return "";
    }

    bool divides(string longer, string shorter) {
      int slen = shorter.length();
      int llen = longer.length();
      for (int i = 0; i < llen; i += slen) {
        if (longer.substr(i, slen) != shorter) {
          return false;
        }
      }
      return true;
    }
};

int main() {
  Solution s = Solution();
  printf("%s\n", s.gcdOfStrings("ABABAB", "ABAB").c_str());
  return 0;
}