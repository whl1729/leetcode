#include <algorithm>
#include <vector>

using namespace std;

/**
 * 思路：
 * 1. 定义 max_sum，代表目标最大和；定义 cur_sum，代表当前最大和
 * 2. 遍历数组，如果 cur_sum 小于 0，则重置为 0
 */
class Solution {
public:
  int maxSubArray(vector<int>& nums) {
    int max_sum = nums[0];
    int cur_sum = 0;
    for (auto num : nums) {
      cur_sum += num;
      max_sum = max(max_sum, cur_sum);
      if (cur_sum < 0) {
        cur_sum = 0;
      }
    }
    return max_sum;
  }
};