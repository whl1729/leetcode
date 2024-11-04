#include <cassert>
#include <climits>
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
        row = start_times.size();
        collum = start_times[0].size();

        // 保存每个点的最小到达时间
        min_reached_times = start_times;
        for (int i = 0; i < row; i++) {
          for (int j = 0; j < collum; j++) {
            min_reached_times[i][j] += (i + j) % 2 == 0 ? 2 : 1;
          }
        }

        // 记录每个点的到达时间
        reached_times = vector<vector<int>>(row, vector<int>(collum, INT_MAX));
        reached_times[0][0] = 0;

        // 接下来需要访问的点
        queue<Point> to_visit_points;
        to_visit_points.push(Point{0, 0});

        while (!to_visit_points.empty()) {
          Point cur = to_visit_points.front();
          int move_time = (cur.x + cur.y) % 2 == 0 ? 1 : 2;
          int cur_reached_time = reached_times[cur.x][cur.y] + move_time;
          update_neighbors(cur);
          for (int i = 0; i < neighbor_cnt; i++) {
            const Point &n = neighbors[i];
            int n_reached_time = max(cur_reached_time, min_reached_times[n.x][n.y]);
            if (reached_times[n.x][n.y] > n_reached_time) {
              reached_times[n.x][n.y] = n_reached_time;
              to_visit_points.push(n);
            }
          }
          to_visit_points.pop();
        }

        return reached_times[row - 1][collum - 1];
    }

    void update_neighbors(const Point &p) {
      neighbor_cnt = 0;
      if (p.x > 0) {
        neighbors[neighbor_cnt++] = Point{p.x - 1, p.y};
      }
      if (p.x < row - 1) {
        neighbors[neighbor_cnt++] = Point{p.x + 1, p.y};
      }
      if (p.y > 0) {
        neighbors[neighbor_cnt++] = Point{p.x, p.y - 1};
      }
      if (p.y < collum - 1) {
        neighbors[neighbor_cnt++] = Point{p.x, p.y + 1};
      }
    }
  
  private:
    int row;
    int collum;
    int neighbor_cnt;
    vector<Point> neighbors = vector<Point>(4);
    vector<vector<int>> reached_times;
    vector<vector<int>> min_reached_times;
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