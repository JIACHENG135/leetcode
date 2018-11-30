# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 20:45:46 2018

@author: ljc
"""

class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 or n == 0:
            return 0

        dp = [1 for i in range(m)]
        for i in range(1,n):
            for j in range(1,m):
                dp[j]+= dp[j-1]
        return dp[-1]
    
a = Solution()
b = a.uniquePaths(24,13)
print(b)