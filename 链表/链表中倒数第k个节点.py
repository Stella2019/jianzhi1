'''
题目：输入一个链表，输出该链表中倒数第k个结点。
'''

'''

使用列表的切片，还是很快的
24ms
5632k
'''

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        res = []
        while head:
            res.append(head)
            head = head.next
        if k > len(res) or k < 1:
            return
        return res[-k]

"""
伪代码:1. 设置两个指针，p1，p2，先让p2走k-1步，然后再一起走，直到p2为最后一个 时，p1 即为倒数第k个节点
注意的点: 注意在while循环的时候，判断条件

"""