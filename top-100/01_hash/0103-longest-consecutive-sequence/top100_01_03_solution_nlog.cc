#include <algorithm>
#include <vector>

using namespace std;

/*
  思路：
  1. 首先想到一个 O(n*log(n)) 的思路：对数组排序，再遍历一遍，即可找到最长序列的长度。但复杂度超出要求了
  2. 按这道题的分类，应该使用哈希，但我想不到怎么使用：
    1. 如果使用哈希，看上去 value 应该是数字连续的序列
  3. 先按排序来实现
*/
class Solution {
public:
  int longestConsecutive(vector<int>& nums) {
    if (nums.empty()) {
      return 0;
    }
    sort(nums.begin(), nums.end());
    int longest = 0;
    int cur_len = 0;
    int prev = nums[0] - 1;
    for (auto num : nums) {
      if (num == prev + 1) {
        cur_len++;
        if (cur_len > longest) {
          longest = cur_len;
        }
      } else if (num > prev) {
        cur_len = 1;
      }
      prev = num;
    }
    return longest;
  }
};
