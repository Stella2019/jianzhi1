'''
题目：从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
'''

'''
思路：两个栈，分二级，第一级存一行的数curStack，第二级存着一行数所对应的left，right的值nextStack，每次结束
一轮循环，把curStack的值给result，然后再将nodes设成nextStack继续进行循环

伪代码:就是层次遍历 1. 每一次打印一个节点的时候，如果该节点有子节点，则把该节点的子节 点放到一个队列的尾部。
接下来到对队列的头部取出最早进入队列的节点放到list中，重复前面的 操作，直至队列中所有的节点都存到list中。

28ms
5632k
'''

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        result,nodes,right = [],[pRoot],True
        while nodes:
            curStack,nextStack = [],[]
            for node in nodes:
                curStack.append(node.val)
                if node.left:
                    nextStack.append(node.left)
                if node.right:
                    nextStack.append(node.right)
            result.append(curStack)
            nodes = nextStack
        return result