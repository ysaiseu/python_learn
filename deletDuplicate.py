#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def init(self, x):
        for i in range(x-1):
            self.val = x[i]
            self.next = x[i+1]
        

class Solution:
    def deleteDuplicates(self, head):
        if not head:
            return head
        nHead = ListNode(0)
        nHead.next, head = head, nHead
        while head:
            if (head.next and head.next.next and head.next.val == head.next.next.val):
                head.next = head.next.next
            else:
                head = head.next
        return nHead.next

bar = Solution()
List = ListNode({1,1,1})
print bar.deleteDuplicates(List)


