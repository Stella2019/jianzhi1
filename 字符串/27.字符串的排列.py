'''
题目：输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
'''

'''
依次取一个元素，然后依次和之前递归形成的所有子串组合，形成新的字符串。
33ms
5632k
概念:输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和 cba。

伪代码1:回溯法的经典应用。1. 回溯法其实就是在生成棵树的过程，回溯法:其实对于回溯法， 我们要从反向开始考虑。
我们每次从原始数组中选择一个加入到结果中，当原始数组中(新建的) 没有元素时(也就是len(a)==0，
此时结果为[1,2,3])，我们得到了第一个排列，我们将这个排列 加入到结果集中，然后返回上一步，
也就是我们现在有[1,2]，再返回一步[1]，此时再加入3，再加 入2，得到[1,3,2],

伪代码2:1. abc———->将第一个字符与自己本身还与其他的字符进行交换后得到abc、bac、 cba。注:用一for循环即可实现。
2. 在第一步每种情况的基础上，保持第一个字符不变，求剩余 几位的排列。
以bac为例:保持第一位不变，剩余两位ac的排列为:ac、ca(注:发现与第一步一 样，因此用递归来实现)。
直到保存到只剩下一个字符没有交换后加上前面的不变的字符作为输出 结果，为:bac、bca。
'''

# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        if not len(ss):
            return []
        if len(ss) == 1:
            return list(ss)

        charList = list(ss)
        charList.sort()
        pStr = []
        for i in range(len(charList)):
            if i > 0 and charList[i] == charList[i-1]:
                continue
            temp = self.Permutation(''.join(charList[:i])+''.join(charList[i+1:]))
            for j in temp:
                pStr.append(charList[i]+j)
        return pStr