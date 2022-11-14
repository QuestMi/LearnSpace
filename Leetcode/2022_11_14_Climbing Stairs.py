# -*- coding: utf-8 -*- 
"""
Create on : 2022/11/14
@Author   : Xiao QingLin 
@File    : 2022_11_14_Climbing Stairs  
"""
"""
2022-11-14 [Leetcode] 70. Climbing Stairs (爬楼梯)
爬楼梯
70、https://leetcode.com/problems/climbing-stairs/
假设： 楼梯阶数 - 5 
5级：
爬1级，剩下 4级可爬；
爬2级，剩下5级可爬；
"""

from functools import lru_cache


class Solution:
    def climb_stairs(self, n):
        assert isinstance(n, int) and n > 0, f'{n} 必须是正整数'
        a, b = 1, 1
        for i in range(n):
            a, b = b, a + b
        return a

    def climb_stairs_1(self, n):
        assert isinstance(n, int) and n > 0, f'{n} 必须是正整数'
        dic = {}
        dic[1], dic[2] = 1, 2
        for i in range(3, n + 1):
            dic[i] = dic[i - 1] + dic[i - 2]
        return dic[n]

    @lru_cache()
    def climb_stairs_2(self, n):
        assert isinstance(n, int) and n > 0, f'{n} 必须是正整数'
        if n < 3:
            return n
        return self.climb_stairs_2(n - 1) + self.climb_stairs_2(n - 2)

    def test_climb_stairs(self):
        test_case = {3: 3, 2: 2, 1: 1, 5: 8}
        for k, v in test_case.items():
            assert self.climb_stairs(k) == v, f'{k} test failed !'
            assert self.climb_stairs_1(k) == v, f'{k} test failed !'
            assert self.climb_stairs_2(k) == v, f'{k} test failed !'


if __name__ == '__main__':
    s = Solution()
    s.test_climb_stairs()
