'''
题目：在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
'''

'''
伪代码:1. 借助辅助头结点，可避免单独讨论头结点的情况。设置两个结点 pre 和 cur，
当 cur 和 cur.next 值相等，cur 一直向前走，直到不等退出循环，这时候 cur 指的值还是重复值，
调整 cur 和 pre 的指针再次判断、

思路一：将链表里面所有的数存在一个列表里面，然后把列表里面只出现一次的数提取出来，在新建一个链表放进去

28ms
5632k
'''

# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        res = []
        while pHead:
            res.append(pHead.val)
            pHead = pHead.next

        # filter函数和map相似，但是filter是返回布尔值去去输入列表进行判断
        res = list(filter(lambda c: res.count(c) == 1, res))

        newlist = ListNode(0)
        pre = newlist
        for i in res:
            node = ListNode(i)
            pre.next = node
            pre = pre.next
        return newlist.next

'''
思路二：
是有两个循环判断的控制，上一个是主要对应2 - 3 - 4这种情况的，可以很快的把头指针移过来，下面这个循环是对应
存在相同值的，不断循环找下一个值。
   头指针
   PreNode
    Head - 1 - 1 - 1 - 2 - 2 - 3 - 4 - 4 - 4 - 5 - 5 - 6 - null
         pNode
            NextNode
False
        pToBeDel
                     PreNode

35ms
6008k
'''

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if pHead == None:
            return
        preHead = None
        pNode = pHead
        while pNode != None:
            needDelete = False
            nextNode = pNode.next
            if nextNode != None and nextNode.val == pNode.val:
                needDelete = True
            if needDelete == False:
                preHead = pNode
                pNode = pNode.next
            else:
                nodeVal = pNode.val
                pToBeDel = pNode
                while pToBeDel != None and pToBeDel.val == nodeVal:
                    pToBeDel = pToBeDel.next
                if preHead == None:
                    pHead = pToBeDel
                    pNode = pToBeDel
                    continue
                else:
                    preHead.next = pToBeDel
                pNode = preHead
        return pHead
