#include <cassert>
#include <string>

using namespace std;

class Solution {
  public:
    bool isBalanced(string num) {
        int odd_sum = 0;
        int even_sum = 0;
        int end = num.size();
        if (end % 2 == 1) {
          end--;
          even_sum += (num[end] - '0');
        }
        for (int pos = 0; pos < end; pos += 2) {
          even_sum += (num[pos] - '0');
          odd_sum += (num[pos+1] - '0');
        }
        return odd_sum == even_sum;
    }
};

int main() {
  auto s = Solution();
  bool result;
  result = s.isBalanced("24123");
  assert(result == true);
  return 0;
}