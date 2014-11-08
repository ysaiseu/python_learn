#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Reverse digits of an integer.

#Example1: x = 123, return 321
#Example2: x = -123, return -321

import datetime

def fn(x, y):
    return x*10 + y

class Solution:
    # the first method can't AC in leetcode
    def reverse(self, x):
        temp = []
        minus = 1
        if x == 0:
            return 0
        if x < 0:
            x = -x
            minus = -1
        while x!=0:
            temp.append(x-x/10*10)
            x /= 10
        temp = reduce(fn, temp) * minus

    def reverse2(self, x):
        if x<0:
            sign = -1
        else:
            sign = 1
        strx = str(abs(x))
        r = strx[::-1]
        return sign*int(r)

bar = Solution()
d = int(raw_input('an integer:  '))
begin = datetime.datetime.now().microsecond
bar.reverse(d)
end = datetime.datetime.now().microsecond
print ( 'time=%d' %(end-begin))
begin = datetime.datetime.now().microsecond
bar.reverse2(d)
end = datetime.datetime.now().microsecond
print ( 'time=%d' %(end-begin))
