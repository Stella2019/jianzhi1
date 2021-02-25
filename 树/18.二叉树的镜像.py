'''
题目：操作给定的二叉树，将其变换为源二叉树的镜像。
'''

'''
伪代码: 1. 交换两个子树，2. 递归左右子树的镜像，终止条件为当前结点为叶结点
递归
23ms
5492k
'''

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if not root:
            return root
        root.left,root.right = root.right,root.left
        self.Mirror(root.left)
        self.Mirror(root.right)
        return root


