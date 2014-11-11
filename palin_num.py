#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Determine whether an integer is a palindrome. Do this without extra space.

class Solution:
    def isPalindrome(self, x):
        len_x = len(x)
        if len_x%2 == 1:
            i = 0
            while i != len_x/2:
                if x[i] == x[-i-1]:
                    i += 1
                    continue
                else:
                    return False
            return True
        if len_x%2 == 0:
            i = 0
            while i != len_x/2+1:
                print i
                if x[i] == x[-i-1]:
                    i += 1
                    continue
                else:
                    return False
            return True

    def isPalindrome2(self, x):
            o = x
            ret = 0
            flag = 1
            if x < 0:
                return False
            while(x!=0):
                ret = ret*10+x%10
                x = x/10
                return ret == o

bar = Solution()
print(bar.isPalindrome(raw_input('input an integer: ')))
print(bar.isPalindrome2(int(raw_input('input an integer: '))))


