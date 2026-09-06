#include <vector>

using namespace std;

/*
思路：

1. 为避免溢出，使用 double 来保存 sum 和 half_sum
2. 为避免重复计算，缓存上一次计算的结果
3. 为避免索引溢出，使用求余
*/
class Solution {
public:
  int countGoodRotations(vector<int>& nums) {
    const int size = nums.size();
    const int half_size = size / 2;
    double first_half_sum = 0;
    for (int i = 0; i < half_size; i++) {
      first_half_sum += nums[i];
    }

    double sum = first_half_sum;
    for (int i = half_size; i < size; i++) {
      sum += nums[i];
    }

    double half_sum = sum / 2;

    int good_count = 0;
    for (int i = 0; i < size; i++) {
      if (first_half_sum > half_sum) {
        good_count++;
      }
      first_half_sum += (nums[(i + half_size) % size] - nums[i]);
    }

    return good_count;
  }
};