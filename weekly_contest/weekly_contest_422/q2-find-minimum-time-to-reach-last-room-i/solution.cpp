#include <cassert>
#include <queue>
#include <vector>

using namespace std;

struct Point {
  int x;
  int y;
};

class Solution {
public:
    int minTimeToReach(vector<vector<int>>& moveTime) {
        int row = moveTime.size();
        int collum = moveTime[0].size();

        // 记录每个店的最小到达时间
        vector<vector<int>> reached_times(row, vector<int>(collum, -1));
        reached_times[0][0] = 0;

        // 接下来需要访问的点
        queue<Point> to_visit_points;
        to_visit_points.push(Point{0, 0});

        while (!to_visit_points.empty()) {
          Point cur = to_visit_points.front();
          vector<Point> neighbors = get_neighbors(cur, row, collum);
          for (const auto &n: neighbors) {
            if (reached_times[n.x][n.y] == -1 || reached_times[n.x][n.y] > reached_times[cur.x][cur.y] + 1) {
              reached_times[n.x][n.y] = max(reached_times[cur.x][cur.y], moveTime[n.x][n.y]) + 1;
              to_visit_points.push(n);
            }
          }
          to_visit_points.pop();
        }

        return reached_times[row - 1][collum - 1];
    }

    vector<Point> get_neighbors(const Point &p, int row, int collum) {
      vector<Point> neighbor;
      if (p.x > 0) {
        neighbor.push_back(Point{p.x - 1, p.y});
      }
      if (p.x < row - 1) {
        neighbor.push_back(Point{p.x + 1, p.y});
      }
      if (p.y > 0) {
        neighbor.push_back(Point{p.x, p.y - 1});
      }
      if (p.y < collum - 1) {
        neighbor.push_back(Point{p.x, p.y + 1});
      }
      return neighbor;
    }
};

int main() {
  auto s = Solution();
  vector<vector<int>> move_times;
  int result;

  move_times = vector<vector<int>>{{56, 93}, {3, 38}};
  result = s.minTimeToReach(move_times);
  assert(result == 39);

  move_times = vector<vector<int>>{{0, 4}, {4, 0}};
  result = s.minTimeToReach(move_times);
  assert(result == 6);

  move_times = vector<vector<int>>{{0, 0, 0}, {0, 0, 0}};
  result = s.minTimeToReach(move_times);
  assert(result == 3);

  move_times = vector<vector<int>>{{0, 1}, {1, 2}};
  result = s.minTimeToReach(move_times);
  assert(result == 3);

  return 0;
}