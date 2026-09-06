from typing import List

class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        n = len(energyDrinkA)
        # boost_a[i+1] 代表第第 i 小时选择 A 饮料能获得的能量最大值
        boost_a = [0 for _ in range(n+1)]
        # boost_b[i+1] 代表第第 i 小时选择 B 饮料能获得的能量最大值
        boost_b = [0 for _ in range(n+1)]
        for i in range(n):
            # 使用动态规划来解决
            boost_a[i+1] = boost_a[i] + energyDrinkA[i]
            boost_b[i+1] = boost_b[i] + energyDrinkB[i]
            if boost_a[i+1] < boost_b[i]:
                boost_a[i+1] = boost_b[i]
            if boost_b[i+1] < boost_a[i]:
                boost_b[i+1] = boost_a[i]

        return max(boost_a[n], boost_b[n])

if __name__ == "__main__":
    s = Solution()

    energyDrinkA = [1,3,1]
    energyDrinkB = [3,1,1]
    result = s.maxEnergyBoost(energyDrinkA, energyDrinkB)
    assert result == 5

    energyDrinkA = [4,1,1]
    energyDrinkB = [1,1,3]
    result = s.maxEnergyBoost(energyDrinkA, energyDrinkB)
    assert result == 7