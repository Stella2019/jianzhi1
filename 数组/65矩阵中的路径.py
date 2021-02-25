'''
题目：请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个
格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则该路
径不能再进入该格子。 例如 a b c e s f c s a d e e 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含
"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
'''

'''
题目补充路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移
动一个格子。如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。
矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路
径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格 子。

思路：优化版回溯法
1.将matrix字符串模拟映射为一个字符矩阵(但并不实际创建一个矩阵)
2.取一个boolean[matrix.length]标记某个字符是否已经被访问过,用一个布尔矩阵进行是否存在该数值的标记。
3.如果没找到结果，需要将对应的boolean标记值置回false,返回上一层进行其他分路的查找。

36ms
5697k
'''

# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if not matrix and rows <= 0 and cols <= 0 and path == None:
            return False
        # 模拟的字符矩阵
        markmatrix = [0] * (rows * cols)
        pathlength = 0
        # 从第一个开始递归，当然第一二个字符可能并不位于字符串之上，所以有这样一个双层循环找起点用的，一旦找到第一个符合的字符串，就开始进入递归，
        # 返回的第一个return Ture就直接跳出循环了。
        for row in range(rows):
            for col in range(cols):
                if self.hasPathCore(matrix, rows, cols, row, col, path, pathlength, markmatrix):
                    return True
        return False

    def hasPathCore(self, matrix, rows, cols, row, col, path, pathlength, markmatrix):
        # 说明已经找到该路径，可以返回True
        if len(path) == pathlength:
            return True

        hasPath = False
        if row >= 0 and row < rows and col >= 0 and col < cols and matrix[row * cols + col] == path[pathlength] and not \
                markmatrix[row * cols + col]:
            pathlength += 1
            markmatrix[row * cols + col] = True
            # 进行该值上下左右的递归
            hasPath = self.hasPathCore(matrix, rows, cols, row - 1, col, path, pathlength, markmatrix) \
                      or self.hasPathCore(matrix, rows, cols, row, col - 1, path, pathlength, markmatrix) \
                      or self.hasPathCore(matrix, rows, cols, row + 1, col, path, pathlength, markmatrix) \
                      or self.hasPathCore(matrix, rows, cols, row, col + 1, path, pathlength, markmatrix)

            # 对标记矩阵进行布尔值标记
            if not hasPath:
                pathlength -= 1
                markmatrix[row * cols + col] = False
        return hasPath


def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]  # 定义上下左右四个方向
    m = len(maze)  # 获取矩阵大小
    n = len(maze[0])

    queue = [(start[0], start[1])]  # 构造队列，并将起始位置包含其中
    # distance保存从起点到每个点的距离
    distance = [[float('inf')] * n for _ in range(m)]
    distance[start[0]][start[1]] = 0

    while queue:
        i, j = queue.pop(0)  # 弹出坐标值i,j
        # 如果坐标为终点坐标，返回True，程序结束

        for dx, dy in directions:  # 对四个方向进行遍历
            x, y, step = i + dx, j + dy, distance[i][j]
            while 0 <= x < m and 0 <= y < n and maze[x][y] != 1:
                # 当x,y坐标合法，并且对应值为0或-1时
                x = x + dx  # 继续前进，模拟小球的滚动过程
                y = y + dy  # 其中0为空地，而-1为之前遍历过的空地
                step += 1

            x = x - dx
            y = y - dy

            if distance[x][y] > step:  # 如果起点到该点的距离比当前距离大
                # 更新该距离，并将坐标加入队列
                maze[x][y] = -1  # 在maze中标记已经遍历过
                distance[x][y] = step
                queue.append((x, y))  # 并将其坐标添加到队列中
                # 如果遍历所有可能性都无法达到目的地
    return distance[destination[0]][destination[1]] if distance[destination[0]][destination[1]] != float('inf') else -1

