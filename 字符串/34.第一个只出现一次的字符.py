'''
题目：在一个字符串(1<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置
'''

'''
伪代码:1. 建立一个哈希表，第一次扫描的时候，统计每个字符的出现次数。
第二次扫描的时 候，如果该字符出现的次数为1，则返回这个字符的位置。
时间复杂度为O(2n) 
注意的点:python的哈希表建立有序字典用 collections.OrderedDict()


思路一：先遍历一遍字符串，用一个hash表存放每个出现的字符和字符出现的次数。再遍历一遍字符串，找到hash值等于1的输出即可。
40ms
5632k

思路二：利用python函数的特性
32ms
5632k
'''

# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if s == None or len(s) <= 0:
            return -1
        alist = list(s)
        blist = {}
        for i in alist:
            if i not in blist.keys():
                blist[i] = 0
            blist[i] += 1
        for i in blist:
            if blist[i] == 1:
                # %d format: a number is required, not str ，i此时返回的是只出现一次的那个字符串是不符合题意的
                # return i
                return s.index(i)
        return -1

# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if s == None or len(s) <= 0:
            return -1
        for i in s:
            if s.count(i) == 1:
                return s.index(i)
        return -1
