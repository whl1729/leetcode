#include <vector>

using namespace std;

class Solution {
public:
  vector<vector<int>> cyclicShift(int n, vector<vector<int>>& grid, vector<int>& rowShift, vector<int>& colShift) {
    auto shifted_grid = doRowShift(n, grid, rowShift);
    return doColShift(n, shifted_grid, colShift);
  }

private:
  vector<vector<int>> doRowShift(int n, vector<vector<int>>& grid, vector<int>& rowShift) {
    vector<vector<int>> output(grid);
    for (int i = 0; i < n; ++i) {
      int k = rowShift[i];
      for (int j = 0; j < n; ++j) {
        output[i][j] = grid[i][(j + k) % n];
      }
    }
    return output;
  }

  vector<vector<int>> doColShift(int n, vector<vector<int>>& grid, vector<int>& colShift) {
    vector<vector<int>> output(grid);
    for (int j = 0; j < n; ++j) {
      int k = colShift[j];
      for (int i = 0; i < n; ++i) {
        output[i][j] = grid[(i + k) % n][j];
      }
    }
    return output;
  }
      
};