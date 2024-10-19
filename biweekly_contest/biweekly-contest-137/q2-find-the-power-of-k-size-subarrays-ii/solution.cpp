#include <cassert>
#include <vector>

using namespace std;

class Solution {
  public:
    vector<int> resultsArray(vector<int>& nums, int k) {
      int size = nums.size();
      int result_size = size - k + 1;
      vector<int> results(result_size);
      // 连续递增的数量
      int consecutive_num = 1;
      // 先完成第一轮统计，以产生结果数组中的第一个元素
      for (int i = 1; i < k; i++) {
        if (nums[i] == nums[i-1] + 1) {
          consecutive_num++;
        } else {
          consecutive_num = 1;
        }
      }

      results[0] = (consecutive_num == k) ? nums[k-1] : -1;

      // 完成后面的统计
      int pos = 1;
      for (int i = k; i < size; i++) {
        if (nums[i] == nums[i-1] + 1) {
          consecutive_num++;
        } else {
          consecutive_num = 1;
        }

        results[pos] = (consecutive_num >= k) ? nums[i] : -1;
        pos++;
      }

      return results;
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