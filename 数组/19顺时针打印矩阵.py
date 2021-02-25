'''
题目：输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，
如果输入如下矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
'''

'''
伪代码: 1. 定义四个变量代表范围边界，up、down、left、right，
2. 向右走存入整行的值，当存 入后，该行再也不会被遍历，代表上边界的 up 加一，同时判断是否和代表下边界的 down 交错
 3. 向下走存入整列的值，当存入后，该列再也不会被遍历，代表右边界的 right 减一，同时判断 是否和代表左边界的 left 交错。 
4. 向左走存入整行的值，当存入后，该行再也不会被遍历，代表 下边界的 down 减一，同时判断是否和代表上边界的 up 交错 
5. 向上走存入整列的值，当存入 后，该列再也不会被遍历，代表左边界的 left 加一，同时判断是否和代表右边界的 right 交错 注意的点:
思路超神：
可以模拟魔方逆时针旋转的方法，一直做取出第一行的操作
例如
1 2 3
4 5 6
7 8 9
输出并删除第一行后，再进行一次逆时针旋转，就变成：
6 9
5 8
4 7
继续重复上述操作即可

24ms
5632k
'''

# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        result = []
        while (matrix):
            result += matrix.pop(0)
            if not matrix:
                break
            matrix = self.turn(matrix)
        return result

    def turn(self, matrix):
        newmat = []
        row = len(matrix)
        col = len(matrix[0])
        for i in range(col):
            newmat1 = []
            for j in range(row):
                newmat1.append(matrix[j][i])
            newmat.append(newmat1)
        newmat.reverse()
        return newmat

