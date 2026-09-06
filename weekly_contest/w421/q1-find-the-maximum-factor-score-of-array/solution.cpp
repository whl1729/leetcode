#include <cassert>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
    long long maxScore(vector<int>& nums) {
        int size = nums.size();
        if (size == 0) {
          return 0;
        }

        if (size == 1) {
          return nums[0] * nums[0];
        }

        long long max_score = 0;
        for (int i = 0; i <= size; i++) {
          long long cur_score = calc_max_score_except(nums, i);
          if (cur_score > max_score) {
            max_score = cur_score;
          }
        }

        return max_score;
    }

    // 计算去掉某个位置的元素后的最大分数
    long long calc_max_score_except(vector<int>& nums, int skip_pos) {
      // 将去掉某个元素后的其他元素存进集合，以去重
      set<int> elems(nums.begin(), nums.begin() + skip_pos);
      if (skip_pos < nums.size()) {
        elems.insert(nums.begin() + skip_pos + 1, nums.end());
      }

      long long gcd = calc_gcd_n(elems);
      long long lcm = calc_lcm_n(elems);
      return gcd * lcm;
    }

    // 计算多个元素的最大公因数
    long long calc_gcd_n(set<int> nums) {
      long long result = *nums.begin();
      for (int n: nums) {
        result = calc_gcd_2(result, n);
      }

      return result;
    }

    // 计算两个元素的最大公因数
    long long calc_gcd_2(long long a, long long b) {
      long long r = a % b;
      while (r > 0) {
        a = b;
        b = r;
        r = a % b;
      }

      return b;
    }

    // 计算多个元素的最小公倍数
    long long calc_lcm_n(set<int> nums) {
      long long result = 1;
      for (int n: nums) {
        result = calc_lcm_2(result, n);
      }

      return result;
    }

    // 计算两个元素的最小公倍数
    long long calc_lcm_2(long long a, long long b) {
      long long gcd = calc_gcd_2(a, b);
      return long long(a / gcd) * b;
    }

};

int main() {
  auto s = Solution();
  long long result;

  result = s.maxScore(vector<int>{16,25,7,27,11,13,17,19,23,29});
  assert(result == 2329089562800);

  result = s.maxScore(vector<int>{2,4,8,16});
  assert(result == 64);

  result = s.maxScore(vector<int>{1,2,3,4,5});
  assert(result == 60);

  result = s.maxScore(vector<int>{3});
  assert(result == 9);

  return 0;
}