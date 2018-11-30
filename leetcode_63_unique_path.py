# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 17:33:15 2018

@author: ljc
"""

class Solution:
    def __init__(self):
        self.mem = dict()
    def uniquePathsWithObstacles(self, obstacleGrid):
#        print(obstacleGrid)
        if obstacleGrid[0][0]==1:
            return 0

        obstacleGrid_flat = ''
        for i in obstacleGrid:
            for j in i:
                obstacleGrid_flat += str(j)
        counter1 = 0
        counter2 = 0
        if obstacleGrid_flat in self.mem:
            return self.mem[obstacleGrid_flat]
        if len(obstacleGrid_flat) == 1 and (not int(obstacleGrid_flat)):
            print(obstacleGrid_flat)
            counter_all =1
            self.mem[obstacleGrid_flat] = counter_all
            return counter_all
        if len(obstacleGrid[0])>=2:
            if obstacleGrid[0][1]!=1:
                temp_ob = [i[1:] for i in obstacleGrid]
                counter1 = self.uniquePathsWithObstacles(temp_ob)
            
        if len(obstacleGrid)>=2:
            if obstacleGrid[1][0]!=1:
                counter2 = self.uniquePathsWithObstacles(obstacleGrid[1:])
            
        counter = counter1 + counter2
        self.mem[obstacleGrid_flat] = counter
        return counter


a = Solution()
obstacleGrid = [[0,1,0,0,0,1,0,0,0,0,1,1,0,0],[0,1,0,0,0,0,0,0,0,0,0,1,1,0],[0,1,1,1,0,1,0,1,1,0,0,1,1,0],[0,0,0,1,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,1,0,0,0,0,1],[0,1,1,0,1,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,1,0,1,0],[0,0,1,0,0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,1,0,0,0],[1,0,0,0,0,0,0,0,0,1,0,1,0,0],[1,0,0,0,1,0,1,0,1,0,0,1,0,0],[0,0,0,0,0,1,0,0,0,0,0,1,0,0],[0,1,1,1,0,0,0,0,0,0,1,1,1,0],[1,1,0,0,0,0,0,0,0,1,0,0,1,0],[0,0,0,0,1,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,1,0],[0,1,0,0,0,0,0,1,0,1,0,0,0,0],[1,0,0,0,0,1,0,0,0,0,0,0,1,0],[0,1,0,0,0,1,0,0,0,1,0,1,1,0],[0,0,0,0,0,0,0,0,1,0,0,0,0,0],[1,0,1,0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,1,0],[0,0,1,0,0,0,0,0,0,1,1,0,0,0],[1,1,0,0,0,0,0,0,0,0,0,0,0,0]]
b = a.uniquePathsWithObstacles(obstacleGrid)
print(b)