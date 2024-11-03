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
    int minTimeToReach(vector<vector<int>>& start_times) {
        int row = start_times.size();
        int collum = start_times[0].size();

        // 记录每个点的最小到达时间
        vector<vector<int>> reached_times(row, vector<int>(collum, -1));
        reached_times[0][0] = 0;

        // 记录每个点移动到邻近点的时间（1或者2）
        vector<vector<int>> move_times(row, vector<int>(collum, 0));
        move_times[0][0] = 1;

        // 接下来需要访问的点
        queue<Point> to_visit_points;
        to_visit_points.push(Point{0, 0});

        while (!to_visit_points.empty()) {
          Point cur = to_visit_points.front();
          vector<Point> neighbors = get_neighbors(cur, row, collum);
          for (const auto &n: neighbors) {
            if (reached_times[n.x][n.y] == -1 || reached_times[n.x][n.y] > reached_times[cur.x][cur.y] + move_times[cur.x][cur.y]) {
              reached_times[n.x][n.y] = max(reached_times[cur.x][cur.y], start_times[n.x][n.y]) + move_times[cur.x][cur.y];
              // 移动时间在 1 或 2 中交替取值
              move_times[n.x][n.y] = 3 - move_times[cur.x][cur.y];
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
  assert(result == 40);

  move_times = vector<vector<int>>{{0, 4}, {4, 4}};
  result = s.minTimeToReach(move_times);
  assert(result == 7);

  move_times = vector<vector<int>>{{0, 0, 0, 0}, {0, 0, 0, 0}};
  result = s.minTimeToReach(move_times);
  assert(result == 6);

  move_times = vector<vector<int>>{{0, 1}, {1, 2}};
  result = s.minTimeToReach(move_times);
  assert(result == 4);

  return 0;
}