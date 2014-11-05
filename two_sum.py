#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Given an array of integers, find two numbers such that they add up to a specific target number.

#The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

#You may assume that each input would have exactly one solution.

#Input: numbers={2, 7, 11, 15}, target=9
#Output: index1=1, index2=2

# @return a tuple, (index1, index2)
import datetime

class Solution:
    def twoSum(self, num, target):
        index = [] 
        numtosort = num[:]
        numtosort.sort() 
        i = 0
        j = len(numtosort) - 1 
        while i < j: 
            if numtosort[i] + numtosort[j] == target: 
                for k in range(0,len(num)): 
                    if num[k] == numtosort[i]: 
                        index.append(k) 
                        break 
                for k in range(len(num)-1,-1,-1): 
                    if num[k] == numtosort[j]: 
                        index.append(k) 
                        break 
                index.sort() 
                break 
            elif numtosort[i] + numtosort[j] < target: 
                i = i + 1 
            elif numtosort[i] + numtosort[j] > target:
                j = j - 1 
        return (index[0]+1,index[1]+1)

    def twoSum2(self, num, target):
        index1 = 0
        index2 = 0
        numberDict = dict()
        for indexCurrent, number in enumerate(num):
        # 使用dict缓存所有数据和对应的index
            numberDict[number] = indexCurrent
        for indexCurrent, number in enumerate(num):
            diff = target - number
            index2 = numberDict.get(diff, 0)
            if index2 == indexCurrent:
                continue
            if index2:
                index1 = indexCurrent
                break
        return index1 + 1, index2 + 1

    def twoSum3(self, num, target):
        # 使用双重循环，时间复杂度O(n^2)
        index1 = 0
        index2 = 0
        bingo = False
        for i in range(len(num)):
            for j in range(i + 1, len(num)):
                if target - num[i] == num[j]:
                    index1 = i
                    index2 = j
                    bingo = True
                    break
                if bingo:
                    break
        return index1 + 1, index2 + 1

bar = Solution()
number = [2,7,11,15]
target = 9
begin = datetime.datetime.now().microsecond
print(bar.twoSum(number, target))
end = datetime.datetime.now().microsecond
print('run time = %d' %(end-begin))
begin = datetime.datetime.now().microsecond
print(bar.twoSum2(number, target))
end = datetime.datetime.now().microsecond
print('run time2 = %d' %(end-begin))
begin = datetime.datetime.now().microsecond
print(bar.twoSum3(number, target))
end = datetime.datetime.now().microsecond
print('run time2 = %d' %(end-begin))


