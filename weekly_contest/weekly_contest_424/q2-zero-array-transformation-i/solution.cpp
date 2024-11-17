#include <algorithm>
#include <cassert>
#include <numeric>
#include <vector>

using namespace std;

class Solution {
  public:
    bool isZeroArray(vector<int>& nums, vector<vector<int>>& queries) {
      int size = nums.size();
      // 差分数组
      vector<int> diffs(size+1, 0);
      diffs[0] = nums[0];
      for (int i = 1; i < size; i++) {
        diffs[i] = nums[i] - nums[i-1];
      }

      int query_count = queries.size();
      for (int i = 0; i < query_count; i++) {
        diffs[queries[i][0]]--;
        diffs[queries[i][1] + 1]++;
      }

      if (diffs[0] > 0) {
        return false;
      }

      vector<int> result = diffs;
      for (int i = 1; i < size; i++) {
        result[i] = result[i-1] + diffs[i];
        if (result[i] > 0) {
          return false;
        }
      }

      return true;
    }
};

int main() {
  auto s = Solution();
  vector<int> nums;
  vector<vector<int>> queries;

  nums = vector<int>{1, 0, 1};
  queries = vector<vector<int>>{{0, 2}};
  assert(s.isZeroArray(nums, queries));

  nums = vector<int>{4, 3, 2, 1};
  queries = vector<vector<int>>{{1, 3}, {0, 2}};
  assert(s.isZeroArray(nums, queries) == false);

  return 0;
}