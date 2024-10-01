#include <algorithm>
#include <vector>

using std::vector;

class Solution {
  public:
    long long maximumTotalSum(vector<int>& maximumHeight) {
      std::sort(maximumHeight.begin(), maximumHeight.end());

      long long sum = 0;
      int size = maximumHeight.size();
      // 当前 tower 可被赋予的最大高度
      int cur_max_height = maximumHeight[size - 1];

      for (int i = size - 1; i >= 0; i--) {
        int cur_height = std::min(cur_max_height, maximumHeight[i]);
        if (cur_height <= 0) {
          return -1;
        }
        sum += cur_height;
        cur_max_height = cur_height - 1;
      }

      return sum;
    }
};