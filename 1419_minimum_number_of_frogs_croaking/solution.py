class Solution(object):
    # 思路：
    # 1. 把蛙鸣当做一个任务，该任务分为5个步骤，分别是：'c', 'r', 'o', 'a', 'k'
    # 2. 把输入视为一个任务清单，输入的每个字母视为一个任务步骤
    # 3. 原问题转化为：把任务步骤列表分配给已有的青蛙或者是新的青蛙，若不能分配，则失败
    # 4. 最后还要保证所有青蛙都处于第5个步骤
    def minNumberOfFrogs(self, croakOfFrogs):
        """
        :type croakOfFrogs: str
        :rtype: int
        """
        # 记录5个步骤的青蛙的总数
        frogs = [0, 0, 0, 0, 0]
        steps = {'c': 0, 'r': 1, 'o': 2, 'a': 3, 'k': 4}
        for croak in croakOfFrogs:
            if croak not in steps:
                return -1
            if croak == 'c':
                # 如果有空闲的青蛙，则将第一个步骤分配给它；否则新增一个青蛙
                if frogs[4] > 0:
                    frogs[4] -= 1
                frogs[0] += 1
            else:
                step = steps[croak]
                # 对于非第一个步骤，如果找不到合适状态的青蛙，则返回失败
                if frogs[step - 1] == 0:
                    return -1
                frogs[step - 1] -= 1
                frogs[step] += 1
        # 最后，如果存在不处于第5个步骤的青蛙，则返回失败
        if any(f > 0 for f in frogs[:-1]):
            return -1
        return frogs[4]