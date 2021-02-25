'''
题目：给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素
B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法
'''

'''
伪代码:1. 可以把B[i]=A[0]A[1]....A[i-1]A[i+1]....A[n-1]。看成A[0]A[1].....A[i-1]和A[i+1].....A[n- 2]A[n-1]两部分的乘积。即通过A[i]项将B[i]分为两部分的乘积。效果相当于是个对角矩阵。
2. 第一 个for循环用来计算上图1范围的数，第二个for循环用来计算上图2范围的数。
设有数组大小为5。
对于第一个for循环
第一步:b[0] = 1;
第二步:b[1] = b[0] * a[0] = a[0]
第三步:b[2] = b[1] * a[1] = a[0] * a[1]; 第四步:b[3] = b[2] * a[2] = a[0] * a[1] * a[2]; 第五步:b[4] = b[3] * a[3] = a[0] * a[1] * a[2] * a[3]; 然后对于第二个for循环
第一步
temp *= a[4] = a[4];
b[3] = b[3] * temp = a[0] * a[1] * a[2] * a[4]; 第二步
temp *= a[3] = a[4] * a[3];
b[2] = b[2] * temp = a[0] * a[1] * a[4] * a[3]; 第三步
temp *= a[2] = a[4] * a[3] * a[2];
b[1] = b[1] * temp = a[0] * a[4] * a[3] * a[2]; 第四步
temp *= a[1] = a[4] * a[3] * a[2] * a[1];
b[0] = b[0] * temp = a[4] * a[3] * a[2] * a[1]; 由此可以看出从b[4]到b[0]均已经得到正确计算。

思路：
        B[0] = A[1] * A[2] * A[3] * A[4] *....*A[n-1] ;（没有A[0]）
        B[1 ]= A[0] * A[2] * A[3] * A[4] *....*A[n-1] ;（没有A[1]）
        B[2] = A[0] * A[1] * A[3] * A[4] *....*A[n-1] ;（没有A[2]）
举例：   输入：  1   2  3  4  5
        输出：  120 60 40 30 24
相当于一个矩形，被省去的那个数字设为1，这样的话，先把上三角的数一行一行撑起来，接着在和下三角的数相乘，节省空间

27ms
5632k
'''

# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        if not A or len(A) < 0:
            return 0
        length = len(A)
        B = [1] * length
        # 下三角，从1开始乘的
        for i in range(1, length):
            B[i] = B[i - 1] * A[i - 1]
        temp = 1
        # 上三角，接着下三角从大往小乘，节约空间，最后一位设为1，前面只有一位，在于之前计算好的相乘
        # 画一个矩形就明白了。
        for i in range(length - 2, -1, -1):
            temp = temp * A[i + 1]
            B[i] *= temp
        return B
