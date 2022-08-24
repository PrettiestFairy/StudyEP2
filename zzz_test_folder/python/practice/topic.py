# coding: utf-8
import math
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    filename='./topic_error.log',
                    format='%(asctime)s %(levelname)-4s %(pathname)s %(lineno)d %(message)s',
                    )


class Topics:

    def __init__(self):
        pass

    @classmethod
    def case_001(cls):
        """
        有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
        :return: 
        """
        count: int = 0
        space: list = list()
        for h in range(1, 5):
            for m in range(1, 5):
                for s in range(1, 5):
                    if h != m != s and h != s:
                        result = int(f'{h}{m}{s}')
                        space.append(result)
                        count += 1
        return count, space

    @classmethod
    def case_002(cls, i: float):
        """
        企业发放的奖金根据利润提成
        利润(I)低于或等于10万元时，奖金可提10%; 利润高于10万元，低于20万元时，低于10万元的部分按10%提成; 高于10万元的部分，可提成7.5%;
        20万到40万之间时，高于20万元的部分，可提成5%; 40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%
        高于100万元时，超过100万元的部分按1%提成
        从键盘输入当月利润I，求应发放奖金总数？
        :return: 
        """
        arr = [100, 60, 40, 20, 10, 0]
        rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
        r = 0
        for index in range(0, 6):
            if i > arr[index]:
                r += (i - arr[index]) * rat[index]
                i = arr[index] + 1
        return round((r * 10000), 2)

    @classmethod
    def case_003(cls):
        """
        一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
        :return: 
        """
        num = 0
        while True:
            num += 1
            if math.sqrt(100 + num) % 1 == 0:
                if math.sqrt(100 + 168 + num) % 1 == 0:
                    break
        return num

    @classmethod
    def case_004(cls, year, month, day):
        """
        输入某年某月某日，判断这一天是这一年的第几天？
        :return: 
        """
        try:
            result = time.strptime(f'{year}{month}{day}', '%Y%m%d').tm_yday
            return result
        except Exception as error:
            logging.exception(error)
            return error

    @classmethod
    def case_005(cls, x, y, z: float):
        """
        输入三个整数x,y,z，请把这三个数由小到大输出。
        :return: 
        """
        try:
            list_spaces = [x, y, z]
            list_spaces.sort()
            return tuple(list_spaces)
        except Exception as error:
            logging.exception(error)
            return error

    @classmethod
    def case_006(cls, n=10):
        """
        斐波那契数列
        输出前 10 个斐波那契数列
        :return: 
        """
        list_spaces = []
        a, b = 1, 1
        for i in range(n - 1):
            list_spaces.append(a)
            a, b = b, a + b
        return list_spaces

    @classmethod
    def case_007(cls):
        """
        将一个列表的数据复制到另一个列表中。
        :return: 
        """
        src_list = [1,2, [3, 4], (5, 6), {'index': 7}, {8, 9}]
        target_list = src_list.copy()
        return target_list
    
    @classmethod
    def case_008(cls):
        """
        输出 9*9 乘法口诀表
        :return: 
        """
        for i in range(1,9+1):
            for j in range(1, 9+1):
                print(f'{j}x{i}={i*j}\t', end='')
                if i == j:
                    break
            print('\n', end='')
        return True
    
    @classmethod
    def case_009(cls):
        """
        暂停一秒输出。
        :return: 
        """
        time.sleep(1)
        return 0
    
    @classmethod
    def case_010(cls):
        """
        暂停一秒输出，并格式化当前时间。
        :return: 
        """
        result = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        time.sleep(1)
        return result


if __name__ == '__main__':
    cut_line = '-' * 50
    print(f'case_a: {Topics.case_001()}\n{cut_line}')
    print(f'case_b: {Topics.case_002(i=23)}\n{cut_line}')
    print(f'case_c: {Topics.case_003()}\n{cut_line}')
    print(f'case_d: {Topics.case_004(year=2021, month=12, day=31)}\n{cut_line}')
    print(f'case_d: {Topics.case_005(x=2, y=1, z=3)}\n{cut_line}')
    print(f'case_d: {Topics.case_006()}\n{cut_line}')
    print(f'case_d: {Topics.case_007()}\n{cut_line}')
    print(f'case_d: {Topics.case_008()}\n{cut_line}')
    print(f'case_d: {Topics.case_009()}\n{cut_line}')
    print(f'case_d: {Topics.case_010()}\n{cut_line}')