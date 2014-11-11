#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Implement atoi to convert a string to an integer.

import datetime

class Solution:
    def atoi(self, str):
        if len(str) == 0:
            return 0
        sign, num, p = 0, 0, 0
        imin, imax = -1<<31, (1<<31)-1
        while str[p] == ' ':
            p += 1
        if str[p] == '+':
            sign = 1
            p += 1
        elif str[p] == '-':
            sign = -1
            p += 1
        while p< len(str) and str[p] >= '0' and str[p] <= '9':
            num = num*10 + ord(str[p]) - ord('0')
            p += 1
        if sign == -1:
            num = -num
        if num > imax:
            num = imax
        elif num < imin:
            num =  imin
            return num

