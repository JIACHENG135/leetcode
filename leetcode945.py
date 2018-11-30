# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 21:28:43 2018

@author: ljc
"""

class Solution:
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A_s = list(set(sorted(A)))
        zero_index = [0 for i in A_s]
        A_ss = sorted(A)
        k = 0
#        A_ss.append(float('inf'))
        while k<len(A_ss)-1:
            k += 1
            counter = 1
            print(k,A_ss)
            while A_ss[k-1]==A_ss[k]:
                print('yes')
#                print(A_ss[k])
                k += 1
                counter += 1
                print(counter)
            
            zero_index[A_s.index(A[k])] = counter
#            k += 1
            
        return zero_index
    
a = Solution()
b = a.minIncrementForUnique([1,2,2,3,3,2,4])
print(b)