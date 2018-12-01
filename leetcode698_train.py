# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 11:12:37 2018

@author: ljc
"""

class Solution:
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        def dfs(nums,target,cursum,inx,k):
            print(cursum,target)
            if cursum == target:
                return dfs(nums,target,0,0,k-1)
            if k==1:
                return True
            if inx < len(nums) and nums[inx] > target:
                return False
            else:
                for i in range(inx,len(nums)-1):
                    if not visited[i] and cursum + nums[i]<=target:
                        print(visited)
                        cursum += nums[i]
                        inx += 1
                        visited[i] = True
                        if dfs(nums,target,cursum,inx,k):
                            return True
                        else:
                            visited[inx] = False
        
        if k==1:
            return True
        total = sum(nums)
        target = total // k
        if k>len(nums) or target!=total / k or max(nums)>target:
            return False
        visited = [False for _ in nums]
        return dfs(nums,target,0,0,k)
a = Solution()
b = a.canPartitionKSubsets([1,2,3,4],2)
print(b)