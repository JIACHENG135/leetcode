# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 10:57:48 2018

@author: ljc
"""

class Solution:
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        def dfs(nums,cursum,idx,target,k):
            # print(visited)
            # print(cursum,idx,k)
            if k == 1:
                return True
            if cursum == target:
                return dfs(nums,0,0,target,k-1)
            if idx < len(nums) and nums[idx] > target:
                return False
            for i in range(idx,len(nums)):
                if not visited[i] and cursum + nums[i] <= target:
                    visited[i] = True
                    if dfs(nums,cursum + nums[i],i+1,target,k):
                        return True
                    visited[i] = False
            return False
        
            
        total = sum(nums)
        if k == 1:
            return True
        target = total//k
        if total % k != 0 or len(nums) < k or max(nums) > target:
            return False
        
        
        nums.sort(reverse = True)
        visited = [False for _ in range(len(nums))]
        return dfs(nums,0,0,target,k)
    
    
a = Solution()
b = a.canPartitionKSubsets([1,2,3,4],2)
print(b)