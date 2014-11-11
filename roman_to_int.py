#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Given a roman numeral, convert it to an integer.
#Input is guaranteed to be within the range from 1 to 3999

class Solution:
    def romanToInt(self, s):
        roval = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result = 0
        for i in range(len(s)):
            if roval[s[i]] <= roval[s[i+1]] and i < len(s)-1:
                result += roval[s[i+1]]
            else:
                result -= roval[s[i+1]]
        return result

