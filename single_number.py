#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Given an array of integers, every element appears twice except for one. Find that single one.

#Note:
#    Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
import datetime

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        lenA = len(A)
        if lenA == 1:
            return A[0]
        A_sort = A[:]
        A_sort.sort()
        i = 0
        while i<lenA:
            if i == lenA-1:
                return A_sort[i]
            if A_sort[i] == A_sort[i+1]:
                i += 2
            else:
                return A_sort[i]

    def singleNumber2(self, A):
        lenA = len(A)
        i = 1
        result = A[0]
        for i in range(1,lenA):
            result = result ^ A[i]
        return result

bar = Solution()
number = [2,2,3,3,4,4,5,6,6,7,7,8,8]
#number = [2,2,1]
begin = datetime.datetime.now().microsecond
print(bar.singleNumber(number))
end = datetime.datetime.now().microsecond
print('run time = %d' %(end-begin))
begin = datetime.datetime.now().microsecond
print(bar.singleNumber2(number))
end = datetime.datetime.now().microsecond
print('run time = %d' %(end-begin))


