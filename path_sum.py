#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root is None:
            return False
        if root.left is None and root.right is None and root.val == sum:
            return True
        Sum = root.val
        return self.isSum(Sum, root.left, root.right, sum)
    def isSum(self, Sum, leftNode, rightNode, sum):
        if leftNode is None and rightNode is None:
            if Sum == sum:
                return True
            else:
                return False
        if leftNode is None:
            return self.isSum(Sum+rightNode.val, rightNode.left, rightNode.right, sum)      
        elif rightNode is None:
            return self.isSum(Sum+leftNode.val, leftNode.left, leftNode.right, sum)
        else:
            return self.isSum(Sum+leftNode.val, leftNode.left, leftNode.right, sum) or self.isSum(Sum+rightNode.val, rightNode.left, rightNode.right, sum)

    def hasPathSum(self, root, sum):
        ret = False
        if root == None:
            return ret
        sum -= root.val
        if sum==0 and root.left==None and root.right==None:
            ret = True
        return ret or self.hasPathSum(root.left,sum) or self.hasPathSum(root.right,sum)
            
