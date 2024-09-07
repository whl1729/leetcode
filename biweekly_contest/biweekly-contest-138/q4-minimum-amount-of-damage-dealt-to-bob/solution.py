import math
from typing import List

class Solution:
    def minDamage(self, power: int, damage: List[int], health: List[int]) -> int:
        n = len(damage)
        times = [math.ceil(h / power) for h in health]
        costs = [(i, damage[i] / times[i]) for i in range(n)]
        costs.sort(key=lambda x: x[1], reverse=True)
        damage_sum = sum(damage)
        min_damage = 0
        for i in range(n):
            min_damage += damage_sum * times[costs[i][0]]
            damage_sum -= damage[costs[i][0]]

        return min_damage


if __name__ == "__main__":
    s = Solution()
    power = 4
    damage = [1,2,3,4]
    health = [4,5,6,8]
    assert s.minDamage(power, damage, health) == 39

    power = 1
    damage = [1,1,1,1]
    health = [1,2,3,4]
    assert s.minDamage(power, damage, health) == 20

    power = 8
    damage = [40]
    health = [59]
    assert s.minDamage(power, damage, health) == 320