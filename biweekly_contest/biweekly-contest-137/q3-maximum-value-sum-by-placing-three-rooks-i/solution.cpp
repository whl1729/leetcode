#include <cassert>
#include <vector>

using namespace std;

class Solution {
public:
    long long maximumValueSum(vector<vector<int>>& board) {
        
    }
};

int main() {
  auto s = Solution();
  vector<vector<int>> board;
  
  board = vector<vector<int>>{{-3,1,1,1},{-3,1,-3,1},{-3,2,1,1}};
  assert(s.maximumValueSum(board) == 4);

  board = vector<vector<int>>{{1,2,3},{4,5,6},{7,8,9}};
  assert(s.maximumValueSum(board) == 15);

  board = vector<vector<int>>{{1,1,1},{1,1,1},{1,1,1}};
  assert(s.maximumValueSum(board) == 3);

  return 0;
}