#include <algorithm>
#include <vector>

using namespace std;

/**
 * 思路：
 * 1. 方向1：基于 O(n^2) 的算法，要降低时间花销，应该尽早剪枝。比如，假设当前元素小于上一个元素，则不适合作为左边线段
 * 2. 方向2：将问题转化为分别找出左右两边的下标，不妨分别记为 left 和 right
 * 3. 观察1：right 的高度比 right 右边的都要大，否则可以选择更右边的
 * 4. 观察2：left 的高度也比 left 左边的大，否则可以选择更左边的
 * 5. 困惑：不知道怎么确定 left 与 right，不知道 left 与 right 之间是否相互耦合
 * 6. 终于找到突破口了：比较 left 与 right 的高度，从较低的一边遍历，找到新的高点，再来比较
 * 5. 确定 left：初始化为 0，往右找更高的线段，跟当前高值比较：
 */
class Solution {
public:
  int maxArea(vector<int>& height) {
    int left = 0;
    int right = height.size() - 1;
    int max_area = 0;
    int cur_area;
    while (left < right) {
      cur_area = (right - left) * min(height[left], height[right]);
      if (cur_area > max_area) {
        max_area = cur_area;
      }
      if (height[left] <= height[right]) {
        int cur = left;
        // 移动左指针
        while (left < right && height[left] <= height[cur]) {
          left++;
        }
      } else {
        // 移动右指针
        int cur = right;
        while (left < right && height[right] <= height[cur]) {
          right--;
        }
      }
    }

    return max_area;
  }
};