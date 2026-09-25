#include <algorithm>
#include <vector>

using namespace std;

/**
 * 思路：
 * 很容易想到一个 O(n^2) 的思路：遍历所有 (i, j) 组合，找到最大值
 */
class Solution {
public:
  int maxArea(vector<int>& height) {
    int max_area = 0;
    int cur_area;
    for (int i = 0; i < height.size(); i++) {
      for (int j = i + 1; j < height.size(); j++) {
        cur_area = min(height[i], height[j]) * (j - i);
        if (cur_area > max_area) {
          max_area = cur_area;
        }
      }
    }
    return max_area;
  }
};