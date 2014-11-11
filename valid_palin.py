#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#For example,
#"A man, a plan, a canal: Panama" is a palindrome.
#"race a car" is not a palindrome.

class Solution:
# @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if s == '':
            return True
        else:
            sTmp = ''
            for i in range(0, len(s)):
                if s[i] >= 'a' and s[i] <= 'z' or s[i] >= '0' and s[i] <= '9' or s[i] >= 'A' and s[i] <= 'Z':
                    sTmp += s[i]
            sTmp = sTmp.lower()
            for i in range(0, len(sTmp)/2):
                if sTmp[i] != sTmp[len(sTmp)-1-i]:
                    return False
            return True

    def isPalindrome2(self, s):
        newS= [i.lower() for i in s if i.isalnum()]
        return newS[:len(newS)/2] == newS[(len(newS)+1)/2:][::-1]
