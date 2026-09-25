#include <algorithm>
#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

/*
  思路：
  1. 定义一个 anagram_map, key 为 string, value 是一个数组，每个元素都是 key 的 anagram
*/
class Solution {
public:
  vector<vector<string>> groupAnagrams(vector<string>& strs) {
    unordered_map<string, vector<string>> anagram_map;
    for (const auto &str : strs) {
      string key = str;
      sort(key.begin(), key.end());
      if (anagram_map.find(key) != anagram_map.end()) {
        anagram_map[key].push_back(str);
      } else {
        anagram_map.insert({key, vector<string>{str}});
      }
    }

    vector<vector<string>> result;
    for (const auto& [key, value] : anagram_map) {
      result.push_back(value);
    }
    return result;
  }
};