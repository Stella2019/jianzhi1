'''
题目：输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
'''

'''
伪代码:1. 创建一个大小为k的数组，遍历n个整数，如果遍历到的数小于大小为k的数组的最大 值，则将此数与其最大值替换。
2. 数组用最大堆保存这k个数，每次遍历只和堆顶比，如果比堆顶 小，删除堆顶，新数入堆。
注意的点:1. 这题可以用所有排序算法实现，
2. O(N) 利用利用快速排序中的获取分割(中轴)点 位置函数getPartitiion，基于数组的第k个数字来调整，使得比第k个数字小的所有数字都位于数
组的左边，比第k个数字大的所有数字都位于数组的右边。调整之后，位于数组左边的k个数字就 是最小的k个数字(这k个数字不一定是排序的)但是会修改输入数组，且一般也不易想到。 3. O(N logK) 利用大顶堆，这个适合

思路1，这一题应用堆排序算法复杂度只有O(nlog k)，堆是完全二叉树的一种，最大堆就是最上面的数是最大的
该方法基于二叉树或者堆来实现，首先把数组前k个数字构建一个最大堆，然后从第k+1个数字开始遍历数组，如果遍历到的
元素小于堆顶的数字，那么久将换两个数字，重新构造堆，继续遍历，最后剩下的堆就是最小的k个数，时间复杂度O(nlog k)。

思路2：排序
'''

# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here、
        import heapq
        if tinput == None or len(tinput) < k or len(tinput) <= 0 or k <= 0:
            return []

        # 建立最小堆，最上面那个数是最小的，返回一个列表，这个列表就是从最小值开始的k个数
        return heapq.nsmallest(k, tinput)


# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here、
        import heapq
        if tinput == None or len(tinput) < k or len(tinput) <= 0 or k <= 0:
            return []

        return sorted(tinput)[:k]




