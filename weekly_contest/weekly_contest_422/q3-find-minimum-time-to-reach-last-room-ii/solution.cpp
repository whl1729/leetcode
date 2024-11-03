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

        // 接下来需要访问的点
        queue<Point> to_visit_points;
        to_visit_points.push(Point{0, 0});

        while (!to_visit_points.empty()) {
          Point cur = to_visit_points.front();
          int move_time = (cur.x + cur.y) % 2 == 0 ? 1 : 2;
          int next_reached_time = reached_times[cur.x][cur.y] + move_time;
          vector<Point> neighbors = get_neighbors(cur, row, collum, move_time, start_times, reached_times);
          for (const auto &n: neighbors) {
            if (reached_times[n.x][n.y] == -1 || (reached_times[n.x][n.y] > next_reached_time)) {
              reached_times[n.x][n.y] = max(next_reached_time, start_times[n.x][n.y] + move_time);
              to_visit_points.push(n);
            }
          }
          to_visit_points.pop();
        }

        return reached_times[row - 1][collum - 1];
    }

    vector<Point> get_neighbors(const Point &p, int row, int collum, int move_time, const vector<vector<int>> &start_times, const vector<vector<int>> &reached_times) {
      vector<Point> neighbor;
      if (p.x > 0 && reached_times[p.x - 1][p.y] != start_times[p.x - 1][p.y] + move_time) {
        neighbor.push_back(Point{p.x - 1, p.y});
      }
      if (p.x < row - 1 && reached_times[p.x + 1][p.y] != start_times[p.x + 1][p.y] + move_time) {
        neighbor.push_back(Point{p.x + 1, p.y});
      }
      if (p.y > 0 && reached_times[p.x][p.y - 1] != start_times[p.x][p.y - 1] + move_time) {
        neighbor.push_back(Point{p.x, p.y - 1});
      }
      if (p.y < collum - 1  && reached_times[p.x][p.y + 1] != start_times[p.x][p.y + 1] + move_time) {
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