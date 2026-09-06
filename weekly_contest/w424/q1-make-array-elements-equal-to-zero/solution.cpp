#include <cassert>
#include <numeric>
#include <vector>

using namespace std;

class Solution {
  public:
    int countValidSelections(vector<int>& nums) {
      int sum = reduce(nums.begin(), nums.end());
      if (sum % 2 == 0) {
        return count_valid_selections_with_even_sum(nums, sum);
      } else {
        return count_valid_selections_with_odd_sum(nums, sum);
      }
    }

    int count_valid_selections_with_even_sum(vector<int> &nums, int sum) {
      int half_sum = sum / 2;
      int size = nums.size();
      int selections = 0;
      int cur_sum = 0;
      for (int i = 0; i < size; i++) {
        cur_sum += nums[i];
        if (nums[i] == 0 && cur_sum == half_sum) {
          selections += 2;
        } else if (cur_sum > half_sum) {
          return selections;
        }
      }
        
      return selections;
    }

    int count_valid_selections_with_odd_sum(vector<int> &nums, int sum) {
      int half_sum = (sum + 1) / 2;
      int size = nums.size();
      int selections = 0;
      int cur_sum = 0;
      for (int i = 0; i < size; i++) {
        cur_sum += nums[i];
        if (nums[i] == 0 && (cur_sum == half_sum || cur_sum == half_sum - 1)) {
          selections++;
        } else if (cur_sum > half_sum) {
          return selections;
        }
      }
        
      return selections;
    }
};

int main() {
  auto s = Solution();
  vector<int> nums;
  int result;

  nums = vector<int>{1, 0, 2, 0, 3};
  result = s.countValidSelections(nums);
  assert(result == 2);

  nums = vector<int>{2, 3, 4, 0, 4, 1, 0};
  result = s.countValidSelections(nums);
  assert(result == 0);

  return 0;
}