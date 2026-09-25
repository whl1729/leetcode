#include <vector>

using namespace std;

/**
 * 思路：
 * 1. 定义 read_pos 和 write_pos，分别记录当前待检查的位置、待写入的位置
 * 2. 遍历数组，每次读到非零元素，read_pos 和 write_pos 均更新；读到 0，则更新 read_pos 而不更新 write_pos
 */
class Solution {
public:
  void moveZeroes(vector<int>& nums) {
    int write_pos = 0;
    for (int i = 0; i < nums.size(); i++) {
      if (nums[i] == 0) {
        continue;
      }
      nums[write_pos++] = nums[i];
    }
    for (; write_pos < nums.size(); write_pos++) {
      nums[write_pos] = 0;
    }
  }
};