#include <iostream>
#include <vector>

using namespace std;

const int kMaxNumLen = 101;
const int kIndexNotFound = -1;
const int kIndexNotSpecial = -2;

class Solution {
public:
    // 算法实现：
    // 1. 由于数组 nums 的取值范围在 1 ~ 100 之间，因此使用一个长度为 101 的数组 latest_indice 来存储每个数字最后一次出现的下标
    // 2. 遍历数组 nums 时，利用数组 latest_indice 即可轻松判断数字是否 special：
    //    - 如果当前数字第一次出现，则先将其下标更新到 latest_indice
    //    - 如果当前数字不是第一次出现，则其下标为 latest_indice 记录的下标加 1 时，才可能是 special，否则肯定不是 special
    int countSpecialIntegers(vector<int>& nums) {
      vector<int> latest_indice(kMaxNumLen, kIndexNotFound);
      for (int i = 0; i < nums.size(); i++) {
        if (latest_indice[nums[i]] == kIndexNotFound || latest_indice[nums[i]] == i - 1) {
          latest_indice[nums[i]] = i;
        } else {
          latest_indice[nums[i]] = kIndexNotSpecial;
        }
      }

      int special_count = 0;
      for (int i = 1; i < kMaxNumLen; i++) {
        if (latest_indice[i] >= 0) {
          special_count++;
        }
      }

      return special_count;
    }
};

int main() {
  vector<int> nums = {1,2,2,1};
  auto s = Solution();
  cout << s.countSpecialIntegers(nums) << endl;
  return 0;
}