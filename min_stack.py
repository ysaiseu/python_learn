#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#push(x) -- Push element x onto stack.
#pop() -- Removes the element on top of the stack.
#top() -- Get the top element.
#getMin() -- Retrieve the minimum element in the stack.

class MinStack:
    # @param x, an integer
    # @return an integer
    def __init__(self):
        self.stack = []
        self.minStack = []
    
    def push(self, x):
        self.stack.append(x)
        if len(self.minStack) and x == self.minStack[-1][0]:
            self.minStack[-1] = (x, self.minStack[-1][1] + 1)
        elif len(self.minStack) == 0 or x < self.minStack[-1][0]:
            self.minStack.append((x, 1))

    def pop(self):
        if self.top() == self.getMin():
            if self.minStack[-1][1] > 1:
                self.minStack[-1] = (self.minStack[-1][0], self.minStack[-1][1] - 1)
            else:
                self.minStack.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minStack[-1][0]


