'''
题目：定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。
'''

'''
我们可以设计两个栈：Stack和StackMin，一个就是普通的栈，另外一个存储push进来的最小值。
首先是push操作：
每次压入的数据newNum都push进Stack中，然后判断StackMin是否为空，如果为空那也把newNum同步压入StackMin里；
如果不为空，就先比较newNum和StackMin中栈顶元素的大小，如果newNum较大，那就不压入StackMin里，只压入一个最小值
否则就同步压入StackMin里。弹出时，同步弹出，这是一个栈结构。

24ms
5760k

伪代码: 双栈法 1. 一个用来存所有的元素“stackTotal”,另一个“stackLittle”用来存加入新的元素后 当前stackTotal中对应的最小值。
2. 两个栈中的元素数量始终保持一致，当新的元素小于 “stackLittle”栈顶元素时，“stackLittle”像栈顶push新来的元素，否则，“stackLittle”向栈顶加入原 栈顶元素。
3. 执行“pop”方法时，两个栈同时弹出各自的栈顶元素。 
注意的点:优化“stackLittle”的空间，当新的元素小于“stackLittle”栈顶元素时，“stackLittle”像栈 顶push新来的元素，
否则，“stackLittle”不变。在执行“pop”方法时，判断时候两个栈顶元素相 同，相同同时弹出，不同取值不弹出“stackLittle”的值。
'''

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, node):
        # write code here
        self.stack.append(node)
        if self.minstack == [] or node < self.min():
            self.minstack.append(node)
        else:
            self.minstack.append(self.min())

    def pop(self):
        # write code here
        if self.minstack == [] or self.stack == []:
            return None
        self.minstack.pop()
        self.stack.pop()

    def top(self):
        # write code here
        return self.stack[-1]

    def min(self):
        # write code here
        return self.minstack[-1]