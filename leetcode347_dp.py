# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 11:15:37 2018

@author: ljc
"""
import time
class Solution:
#    def __init__(self):
#        self.mem = dict()
#        self.smaller = dict()
#    mem = {}
    def wiggleMaxLength_helper(self, nums,index = 0,minus = 1,str_i = '4',mem={}):
#        if (minus,index) in self.mem:        
#        if index in mem:
#
#            print(mem)
##            return self.mem[(minus,index)]
#            return mem[index]

        
        if not nums:
            return 0
        bigger = []
        smaller = []    
        leng = []
        for j in range(1+index,len(nums)):
            if nums[j]>nums[index]:
                bigger.append(j)
            elif nums[j]<nums[index]:
                smaller.append(j)
#        print(self.mem)
#        print(str_i,minus,'bigger',[nums[i] for i in bigger],'smaller',[nums[i] for i in smaller])
#        str_i = str(nums[index])
        if minus == 1 and not bigger:
            return 1
        if minus == -1 and not smaller:
            return 1
        if minus==1:
#            print('minus',1)
            for i in bigger:
                if i in mem:
                    leng.append(1+mem[i])
                else:
                    leng.append(1 + self.wiggleMaxLength_helper(nums,i,-1,str_i +str(nums[i]),mem))
        else:
#            print('minus',-1)
            for i in smaller:
                if i in mem:
                    leng.append(1+mem[i])
                else:
                    leng.append(1 + self.wiggleMaxLength_helper(nums,i,1,str_i +str(nums[i]),mem))
#                time.sleep(1)
#        print(leng)
#        self.mem[(minus,index)] = max(leng)
        mem[index] = max(leng)

#        print(str_i,(minus,index))

        return max(leng)
    def wiggleMaxLength(self,nums):
        return max(self.wiggleMaxLength_helper(nums,0,1),self.wiggleMaxLength_helper(nums,0,-1))
    
    
    
a = Solution()
b = a.wiggleMaxLength([1,17,5,10,13,15,10,5,16,8])
print(b)