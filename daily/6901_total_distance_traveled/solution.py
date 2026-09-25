from json.tool import main
from operator import add


class Solution(object):
    def distanceTraveled(self, main_tank, additional_tank):
        """
        :type main_tank: int
        :type additional_tank: int
        :rtype: int

        思路：
        1. 当 main_tank 还有汽油，则按照5L为一份，烧完最多的份数
        2. 计算 additional_tank 流入的数量，再按照5L为一份来烧
        3. 不断重复，直到 main_tank 为 0
        """
        used_fuel = 0
        while True:
            used_fuel += (main_tank // 5) * 5
            transfered_fuel = min(main_tank // 5, additional_tank)
            main_tank = main_tank % 5 + transfered_fuel
            additional_tank -= transfered_fuel
            if main_tank < 5:
                used_fuel += main_tank
                break
        
        return 10 * used_fuel


if __name__ == "__main__":
    solution = Solution()
    assert solution.distanceTraveled(5, 10) == 60
    assert solution.distanceTraveled(1, 2) == 10
    assert solution.distanceTraveled(0, 100) == 0
    assert solution.distanceTraveled(25, 2) == 270
    assert solution.distanceTraveled(25, 20) == 310
    assert solution.distanceTraveled(9, 2) == 110
    assert solution.distanceTraveled(4, 5) == 40
    # 25 + 5 + 1