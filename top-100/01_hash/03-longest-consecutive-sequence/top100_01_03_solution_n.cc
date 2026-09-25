#include <vector>
#include <unordered_set>

using namespace std;

/**
 * 这道题我想不出 O(n) 的思路，最终看了官方题解的思路，然后自己实现一遍。
 * 官方思路：
 * 1. 定义一个集合，保存数组的元素
 * 2. 遍历集合，只需处理属于子序列起点的元素，即：对每个元素 num，如果 num - 1 不在集合中，则它属于起点，需要处理，否则不需要处理
 */
class Solution {
public:
  int longestConsecutive(vector<int>& nums) {
    unordered_set<int> us{nums.begin(), nums.end()};
    int longest_len = 0;
    for (auto num : us) {
      if (us.count(num - 1)) {
        continue;
      }

      int cur_len = 1;
      while (us.count(num + 1)) {
        cur_len++;
        num++;
      }

      if (cur_len > longest_len) {
        longest_len = cur_len;
      }
    }
    return longest_len;
  }
};