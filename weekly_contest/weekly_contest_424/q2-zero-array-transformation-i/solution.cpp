#include <cassert>
#include <numeric>
#include <vector>

using namespace std;

class Solution {
  public:
    bool isZeroArray(vector<int>& nums, vector<vector<int>>& queries) {
      int size = nums.size();
      vector<int> decrements(size);
      int query_count = queries.size();
      for (int i = 0; i < query_count; i++) {
        for (int j = queries[i][0]; j <= queries[i][1]; j++) {
          decrements[j]++;
        }
      }

      for (int i = 0; i < size; i++) {
        if (decrements[i] < nums[i]) {
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