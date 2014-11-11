#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import datetime

def check(left_node, right_node):
    if left_node is None and right_node is None:
        return True
    elif left_node is None or right_node is None:
        return False
    else:
        return left_node == right_node and check(left_node.left, right_node.right) and check(left_node.right, right_node.left)

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if not root:
            return True
        return check (root.left, root.right)
