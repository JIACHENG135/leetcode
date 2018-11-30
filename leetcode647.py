# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 16:29:17 2018

@author: ljc
"""

class Solution:
    def __init__(self):
        self.mem= dict()
    def countSubstrings(self, s,l=0,r=-1):
        """
        :type s: str
        :rtype: int
        """
        def isp(s):
#            print(s)
            if len(s)<=1:
                return True
            if s[0]==s[-1]:
                return isp(s[1:-1])
            else:
                return False
#        r = len(s)
        if (l,r) in self.mem:
            return self.mem[(l,r)]
        if isp(s[l:r]):
            self.mem[(l,r)] = s[l:r]
            return s[l:r]
        elif len(s[l:r])==2:
            self.mem[(l,r)] = ''
            return ''
        else:
            res_1 = self.countSubstrings(s,l+1,r)
            len_res_1 = len(res_1)
            res_2 = self.countSubstrings(s,l,r-1)
            len_res_2 = len(res_2)
        max_len = max(len_res_1,len_res_2)
        if max_len == len_res_1:
            self.mem[(l,r)] = res_1
            return res_1
        else:
            self.mem[(l,r)] = res_2
            return res_2

    
a = Solution()
b = a.countSubstrings('')
print(b)