﻿'''

给定一个 32 位有符号整数，将整数中的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。根据这个假设，如果反转后的整数溢出，则返回 0。



'''



class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        c = 0
        if abs(x)>2**31:
            return 0
        if x<0:
            x = abs(x)
            while x>0:
                b=x%10
                x=int(x/10)
                c=c*10+b
            if abs(c)>2**31:
                return 0
            return (-c)
        else:
            while x>0:
                b=x%10
                x=int(x/10)
                c=c*10+b
            if abs(c)>2**31:
                return 0
            return (c)