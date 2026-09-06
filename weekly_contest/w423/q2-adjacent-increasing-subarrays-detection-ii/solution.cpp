#include <algorithm>
#include <cassert>
#include <vector>

using namespace std;

class Solution {
  public:
    int maxIncreasingSubarrays(vector<int>& nums) {
        int max_increasing_len = 0;
        int prev_increasing_len = 0;
        int cur_increasing_len = 1;

        // 当前相邻两个递增数组长度的最小值
        int cur_min_adjacent_len = 0;
        // 相邻两个递增数组长度的最小值的最大值
        int max_min_adjacent_len = 0;

        int size = nums.size();
        for (int i = 1; i < size; i++) {
          if (nums[i] > nums[i-1]) {
            cur_increasing_len++;
          } else {
            max_increasing_len = max(max_increasing_len, cur_increasing_len);
            cur_min_adjacent_len = min(cur_increasing_len, prev_increasing_len);
            max_min_adjacent_len = max(max_min_adjacent_len, cur_min_adjacent_len);
            prev_increasing_len = cur_increasing_len;
            cur_increasing_len = 1;
          }
        }

        max_increasing_len = max(max_increasing_len, cur_increasing_len);
        cur_min_adjacent_len = min(cur_increasing_len, prev_increasing_len);
        max_min_adjacent_len = max(max_min_adjacent_len, cur_min_adjacent_len);
        return max(max_increasing_len / 2, max_min_adjacent_len);
    }
};

int main() {
  auto s = Solution();
  vector<int> nums;
  int result;

  nums = vector<int>{-15, 19};
  result = s.maxIncreasingSubarrays(nums);
  assert(result == 1);

  nums = vector<int>{2,5,7,8,9,2,3,4,3,1};
  result = s.maxIncreasingSubarrays(nums);
  assert(result == 3);

  nums = vector<int>{1,2,3,4,4,4,4,5,6,7};
  result = s.maxIncreasingSubarrays(nums);
  assert(result == 2);

  return 0;
}