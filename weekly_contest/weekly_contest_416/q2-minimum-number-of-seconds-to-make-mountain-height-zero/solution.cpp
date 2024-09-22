#include <algorithm>
#include <cassert>
#include <cmath>
#include <vector>

using std::vector;

class Solution {
  public:
    long long minNumberOfSeconds(int mountainHeight, vector<int>& workerTimes) {
      std::sort(workerTimes.begin(), workerTimes.end());
      int left = 1;
      int right = mountainHeight;
      while (left < right) {
        int mid = left + (right - left) / 2;
        if (can_reduce_to_zero(mountainHeight, workerTimes, mid)) {
          right = mid;
        } else {
          left = mid + 1;
        }
      }
      return workerTimes[0] * right * (right + 1) / 2;
    }

  private:
    bool can_reduce_to_zero(int mountainHeight, vector<int>& workerTimes, int firstHeight) {
      int totalHeight = 0;
      for (auto &t : workerTimes) {
        totalHeight += get_reduced_height(firstHeight, workerTimes[0], t);
      }
      return totalHeight >= mountainHeight;
    }

    int get_reduced_height(int firstHeight, int firstTime, int targetTime) {
      long long time_bound = firstTime * firstHeight * (firstHeight + 1);
      long long targetHeight = floor(sqrt(time_bound / targetTime));
      if ((targetHeight + 1) * (targetHeight + 2) * targetHeight <= time_bound) {
        return targetHeight + 1;
      }
      return targetHeight;
    }
};

int main() {
  Solution s;
  vector<int> workerTimes = {4};
  int mountainHeight = 3;
  assert(s.minNumberOfSeconds(mountainHeight, workerTimes) == 24);

  workerTimes = {2, 1, 1};
  mountainHeight = 4;
  assert(s.minNumberOfSeconds(mountainHeight, workerTimes) == 3);

  mountainHeight = 10;
  workerTimes = {3, 2, 2, 4};
  assert(s.minNumberOfSeconds(mountainHeight, workerTimes) == 12);

  mountainHeight = 5;
  workerTimes = {1};
  assert(s.minNumberOfSeconds(mountainHeight, workerTimes) == 15);
}