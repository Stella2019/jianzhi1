'''
题目：输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。
假设输入的数组的任意两个数字都互不相同。
'''

'''
二叉搜索树即是二叉排序树，
1. 后序遍历序列的最后一个元素为二叉树的根节点；
2. 二叉搜索树左子树上所有的结点均小于根结点、右子树所有的结点均大于根结点。

算法步骤如下：
1. 找到根结点；
2. 遍历序列，找到第一个大于等于根结点的元素i，则i左侧为左子树、i右侧为右子树；
3. 我们已经知道i左侧所有元素均小于根结点，那么再依次遍历右侧，看是否所有元素均大于根结点；若出现小于根结点的元素，则直接返回false；若右侧全都大于根结点，则：
4. 分别递归判断左/右子序列是否为后序序列；

25ms
5632k
伪代码:对于一个序列S，最后一个元素是x (也就是根)，如果去掉最后一个元素的序列为T， 那么T满足:T可以分成两段，前一段(左子树)小于x，后一段(右子树)大于x，且这两段(子 树)都是合法的后序序列。完美的递归定义 : ) 。
步骤1. 得到最后一个元素x 
2. 左子树(序列左边 部分)节点小于根节点 
3. 右子树的节点(序列右边部分)都大于根节点。
4. 递归判断左右子树。
'''


# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False

        root = sequence[-1]

        i = 0
        for node in sequence[:-1]:
            if node > root:
                break
            i += 1

        for node in sequence[i:-1]:
            if node < root:
                return False

        left = True
        # i>0 意味i =0 或者1 的时候，两个元素在二叉树没有排序之分的，但是3个元素就有了左右子树之分
        if i > 0:
            left = self.VerifySquenceOfBST(sequence[:i])

        right = True
        # len(sequence)>3才有左右之分的
        if i < len(sequence) - 2 and left:
            right = self.VerifySquenceOfBST(sequence[i + 1:])

        return left and right


