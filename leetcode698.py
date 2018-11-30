# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 08:51:43 2018

@author: ljc
"""

class Solution:
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        def cal_if_divide(nums,target,result=[]):
#            print(target,nums)
            if target == 0:
                return nums
            elif len(nums)==1 and nums[0]!=target:
                return nums
            else:
                for i in range(len(nums)):
#                    print(target,nums)
                    if target - nums[i]>=0:
#                        print(nums[i])
                        if cal_if_divide(nums[0:i]+nums[i+1:],target-nums[i]):
                            return cal_if_divide(nums[0:i]+nums[i+1:],target-nums[i])
                        
#                return False
        test = cal_if_divide([10,8],6)
        print('test',test)
#        k_ori = [i for i in [k]]
#        nums_ori = [i for i in nums]
        if sum(nums)//k != sum(nums)/k or k>len(nums):
            return False
        else:
            target = sum(nums) // k
            while cal_if_divide(nums,target) and len(nums)>1:
                nums = cal_if_divide(nums,target)
#                print(target,nums,'ori',nums_ori)
#            target = sum(nums_ori) // k_ori[0]
#            print(target,nums)

            nums = cal_if_divide(nums,target)
            if not nums:
                return True
            else:
                return False

            
            
            
        
        
a = Solution()
b = a.canPartitionKSubsets([8,10],1)
print(b)