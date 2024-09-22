#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <assert.h>

using std::string;
using std::vector;
using std::set;

class Solution {
public:
    bool reportSpam(vector<string>& message, vector<string>& bannedWords) {
      int count = 0;
      set<string> banned_set(bannedWords.begin(), bannedWords.end());
      for (const auto &word: message) {
          if (banned_set.find(word) != banned_set.end()) {
            count++;
          }
          if (count >= 2) {
            return true;
          }
      }
      return false;
    }
};

int main() {
  Solution sol;
  vector<string> message = {"foo", "bar", "foo", "baz"};
  vector<string> message2 = {"foot", "bar", "fool", "baz"};
  vector<string> bannedWords = {"foo", "bar"};
  assert(sol.reportSpam(message, bannedWords) == true);
  assert(sol.reportSpam(message2, bannedWords) == false);
}