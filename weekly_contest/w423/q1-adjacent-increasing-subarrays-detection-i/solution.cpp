#include <cassert>
#include <vector>

using namespace std;

class Solution {
  public:
    bool hasIncreasingSubarrays(vector<int>& nums, int k) {
        int size = nums.size();
        int max_start = size - 2 * k;
        for (int i = 0; i <= max_start; i++) {
          if (is_adjacent_increasing(nums, i, k)) {
            return true;
          }
        }
        return false;
    }
    bool is_adjacent_increasing(vector<int> &nums, int start, int k) {
      int middle = start + k;
      for (int i = start + 1; i < middle; i++) {
        if (nums[i] <= nums[i-1]) {
          return false;
        }
      }
      int end = middle + k;
      for (int i = middle + 1; i < end; i++) {
        if (nums[i] <= nums[i-1]) {
          return false;
        }
      }
      return true;
    }
};

int main() {
  auto s = Solution();
  vector<int> nums;

  nums = vector<int>{-15,19};
  assert(s.hasIncreasingSubarrays(nums, 1) == true);

  nums = vector<int>{2,5,7,8,9,2,3,4,3,1};
  assert(s.hasIncreasingSubarrays(nums, 3));

  nums = vector<int>{1,2,3,4,4,4,4,5,6,7};
  assert(s.hasIncreasingSubarrays(nums, 5) == false);

  return 0;
}