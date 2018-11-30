# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 14:20:29 2018

@author: ljc
"""
#import numpy as np

class Solution:
    def __init__(self):
        self.mem = dict()
    def unique_path(self,m,n):
        if str(m) + ',' + str(n) in self.mem:
            return self.mem[str(m) + ',' + str(n)]
        if m<=2 or n<=2:
            if m==2:
                counter_all = n
            else:
                counter_all = m
            self.mem[str(m) +','+ str(n)] = counter_all
            return counter_all
        else:
            counter_all = self.unique_path(m-1,n) + self.unique_path(m,n-1)
            self.mem[str(m) + ',' + str(n)] = counter_all
            return counter_all
    
a = Solution()
b = a.unique_path(24,13)
print(b)
        