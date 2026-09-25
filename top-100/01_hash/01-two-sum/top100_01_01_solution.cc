#include <vector>
#include <unordered_map>

using namespace std;

/*
  思路：
  1. 定义一个哈希表 num_map，记录取值为 num 的数字对应的同伴的下标
  2. 遍历数组，对于第 i 个元素 num, 如果在 num_map 能找到它，立即返回对应下标；否则计算 target - num 的差值，将 {target - num: i} 存入哈希表
*/
class Solution {
public:
  vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int, int> num_map;
    for (int i = 0; i < nums.size(); ++i) {
      if (num_map.find(nums[i]) != num_map.end()) {
        return vector<int>{num_map[nums[i]], i};
      }

      num_map.insert({target - nums[i], i});
    }

    return vector<int>{-1, -1};
  }
};