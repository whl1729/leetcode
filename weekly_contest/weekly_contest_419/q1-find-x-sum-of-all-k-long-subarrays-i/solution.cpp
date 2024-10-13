#include <algorithm>
#include <cassert>
#include <numeric>
#include <vector>

using namespace std;

const int MAX_LEN = 50;

class Solution {
  public:
    vector<int> findXSum(vector<int>& nums, int k, int x) {
      int size = nums.size();
      int xsize = size - k + 1;
      vector<int> xsums(xsize, 0);
      for (int i = 0; i < xsize; i++) {
        xsums[i] = find_sub_xsum(nums.begin() + i, nums.begin() + i + k, x);
      }
      return xsums;
    }

    int find_sub_xsum(vector<int>::const_iterator first, vector<int>::const_iterator last, int x) {
      // 计算数字频率
      int occurences[MAX_LEN+1] = {0};
      for (auto v = first; v != last; v++) {
        occurences[*v]++;
      } 

      vector<pair<int, int>> num_occurs;
      for (int i = 0; i < MAX_LEN+1; i++) {
        if (occurences[i] > 0) {
          num_occurs.push_back(make_pair(i, occurences[i]));
        }
      }

      if (num_occurs.size() <= x) {
        return reduce(first, last);
      }

      // 根据数字频率倒序排列
      sort(num_occurs.begin(), num_occurs.end(), [](auto &left, auto &right) {
        if (left.second == right.second) {
          return left.first > right.first;
        }
        return left.second > right.second;
      });

      // 计算 x-sum
      int xsums = 0;
      for (int i = 0; i < x; i++) {
        xsums += num_occurs[i].first * num_occurs[i].second;
      }

      return xsums;
    }
};

int main() {
  auto s = Solution();
  vector<int> nums;
  vector<int> result;
  vector<int> expected;

  nums = vector<int>{1, 1, 2, 2, 3, 4, 2, 3};
  result = s.findXSum(nums, 6, 2);
  expected = vector<int>{6, 10, 12};
  assert(result == expected);

  nums = vector<int>{3, 8, 7, 8, 7, 5};
  result = s.findXSum(nums, 2, 2);
  expected = vector<int>{11, 15, 15, 15, 12};
  assert(result == expected);

  return 0;
}