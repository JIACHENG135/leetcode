# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 08:55:01 2018

@author: ljc
"""

class Solution:
    def __init__(self):
        self.bigger = dict()
        self.smaller = dict()
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def find_b_s(nums):
            for i in range(len(nums)):
                self.bigger[i] = []
                self.smaller[i] = []
                for j in range(i+1,len(nums)):
                    if nums[j]>nums[i]:
                        self.bigger[i].append(j)
                    if nums[j]<nums[i]:
                        self.smaller[i].append(j)
        find_b_s(nums)
        def bs(nums,counter=0):
            stack = [0]
            minus=1
#            counter = 0
            counter1_all = [0]
            counter_1 =1
            while stack:
                cs = stack.pop(0)
#                print(cs,stack)
                if minus==1:
                    bigger_cs = self.bigger[cs]
                    if not bigger_cs:
#                        print('bigger1',bigger_cs)
                        if not stack:
                            break
                        else:
                            counter1_all.append(counter_1)
                            counter_1=1
                            stack.pop()
                    else:
#                        print(bigger_cs)
                        minus *= -1
                        counter_1+=1
                        for i in bigger_cs:
                            stack.append(i)
#                        print(stack)
                            
                else:
                    smaller_cs = self.smaller[cs]
                    if not smaller_cs:
#                        print('smaller1',smaller_cs,cs)
                        if not stack:
                            break
                        else:
                            counter1_all.append(counter_1)
                            counter_1=1
                            stack.pop()
                    else:
                        minus *=-1
                        counter_1+=1
                        for i in smaller_cs:
                            stack.append(i)
            stack = [0]
            minus=-1
#            counter = 0
            counter2_all = [0]
            counter_2 = 1
            while stack:
                cs = stack.pop(0)
#                print(cs,stack)
                if minus==1:
                    bigger_cs = self.bigger[cs]
                    if not bigger_cs:
#                        print('bigger1',bigger_cs)
                        if not stack:
                            break
                        else:
                            counter2_all.append(counter_2)
                            counter_2=1
                            stack.pop()
                    else:
#                        print(bigger_cs)
                        minus *= -1
                        counter_2+=1
                        for i in bigger_cs:
                            stack.append(i)
#                        print(stack)
                            
                else:
                    smaller_cs = self.smaller[cs]
                    if not smaller_cs:
#                        print('smaller1',smaller_cs,cs)
                        if not stack:
                            break
                        else:
                            counter2_all.append(counter_2)
                            counter_2=1
                            stack.pop()
                    else:
                        minus *=-1
                        counter_2+=1
                        for i in smaller_cs:
                            stack.append(i)
            return max(max(counter1_all),max(counter2_all))

        return bs(nums)
        
        
        
        
a = Solution()
nums = [1,17,5,10,13,15,10,5,16,8]
#nums = [1,7,4,9,2,5]
b = a.wiggleMaxLength(nums)
print(b)
        