#include <cassert>
#include <vector>

using namespace std;

class Solution {
  public:
    vector<int> resultsArray(vector<int>& nums, int k) {
      int size = nums.size();
      int result_size = size - k + 1;
      vector<int> results(result_size);
      for (int i = 0; i < result_size; i++) {
        results[i] = calc_power(nums, i, k);
      }
      return results;
    }

    int calc_power(vector<int>& nums, int start, int k) {
      int end = start + k;
      for (int i = start + 1; i < end; i++) {
        if (nums[i] != nums[i-1] + 1) {
          return -1;
        }
      }
      return nums[end-1];
    }
};

int main() {
  auto s = Solution();
  vector<int> result;
  vector<int> expected;

  result = s.resultsArray(vector<int>{1,2,3,4,3,2,5}, 3);
  expected = vector<int>{3,4,-1,-1,-1};
  assert(result == expected);

  result = s.resultsArray(vector<int>{2,2,2,2,2}, 4);
  expected = vector<int>{-1,-1};
  assert(result == expected);

  result = s.resultsArray(vector<int>{3,2,3,2,3,2}, 2);
  expected = vector<int>{-1,3,-1,3,-1};
  assert(result == expected);

  return 0;
}