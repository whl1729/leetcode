#include <vector>
#include <cassert>

using std::vector;

class Solution {
  public:
    int minElement(vector<int>& nums) {
      int min_digit_sum = 0;
      for (auto &n: nums) {
        int cur_digit_sum = calc_digit_sum(n);
        if (cur_digit_sum < min_digit_sum) {
          min_digit_sum = cur_digit_sum;
        }
      }

      return min_digit_sum;
    }

    int calc_digit_sum(int num) {
      int sum = 0;
      while (num > 0) {
        sum += num % 10;
        num /= 10;
      }
      return sum;
    }
};

int main() {
  auto s = Solution();
  auto nums = vector<int>{10, 12, 13, 14};
  assert(s.minElement(nums) == 1);
  nums = vector<int>{1, 2, 3, 4};
  assert(s.minElement(nums) == 1);
  nums = vector<int>{999, 19, 199};
  assert(s.minElement(nums) == 1);
}