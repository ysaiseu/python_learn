#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Given a binary tree, find its maximum depth.

#The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
import datetime

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
         if root == None:
             return 0
         else:
             return max(self.maxDepth(root.left), self.maxDepth(root.right))+1
