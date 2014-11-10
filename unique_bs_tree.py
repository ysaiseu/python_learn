#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

import datetime

class Solution:
    def numTrees(self, n):
        result = [0] * (n+1)
        print result
        temp = 0
        if n>=0:
            result[0] = 1
        if n>=1:
            result[1] = 1
        if n>=2:
            result[2] = 2
        if n>=3:
            for i in range(3, n+1):
                for k in range(0, i):
                    result[i] += result[k] * result[i-k-1]
        return result[n]
			

bar = Solution()
num = int(raw_input("please input an integer: "))
print(bar.numTrees(num))

