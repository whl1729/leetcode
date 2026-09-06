#include <cmath>
#include <iostream>
#include <vector>
using namespace std;

const long long kModulo = 1e9 + 7;
const int kMaxDigitLen = 16;
/*
1. 思路不难：
  - 遍历数组，对每个元素，分别算出 width, d, x, y，然后执行 x^y
  - 将所有元素的执行结果加起来，module (10^9 + 7)
2. 难点在于大数溢出：
  - 执行 x^y 的时候，可能会溢出
  - 每个元素的运行结果相加的时候，也可能会溢出
3. 解决方案：
  - 每次乘法或加法前，先对双方 module (10^9 + 7)
*/
class Solution {
public:
    int sumDecoded(vector<long long>& nums) {
      int sum = 0;
      int cur_decoded;
      for (int i = 0; i < nums.size(); i++) {
        cur_decoded = decode(nums[i]);
        sum = (sum + cur_decoded) % kModulo;
      }
      return sum;
    }
private:
    int decode(long long num) {
      vector<int> digits(16);
      int ndigits = parse_digits(num, digits);
      int width = digits[ndigits - 1];
      int x = get_num_from_digits(digits, 0, width);
      int y = get_num_from_digits(digits, width, ndigits - 1);
      return power(x, y);
    }

    int parse_digits(long long num, vector<int> &digits) {
      int ndigits = 0;
      while (num > 0) {
        digits[ndigits++] = num % 10;
        num /= 10;
      }
      std::reverse(digits.begin(), digits.begin() + ndigits);
      return ndigits;
    }

    int get_num_from_digits(vector<int> digits, int start, int end) {
      int num = 0;
      for (int i = start; i < end; i++) {
        num = num * 10 + digits[i];
      }
      return num;
    }

    int power(int x, unsigned int y) {
      long long result = (y & 1)? x : 1;
      long long x_power = x;
      y >>= 1;
      while (y > 0) {
        x_power = (x_power * x_power) % kModulo;
        if (y & 1) {
          result = (result * x_power) % kModulo;
        }
        y >>= 1;
      }
      return result;
    }
};

int main() {
  auto s = Solution();
  vector<long long> nums = {231};
  cout << s.sumDecoded(nums) << endl;
  nums = {2522,2101};
  cout << s.sumDecoded(nums) << endl;
  nums = {2301};
  cout << s.sumDecoded(nums) << endl;
  nums = {5182};
  cout << s.sumDecoded(nums) << endl;
  nums = {5075305699744,996431454882,53268980345446,413612416};
  cout << s.sumDecoded(nums) << endl;
  return 0;
}