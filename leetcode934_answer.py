# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 01:02:36 2018

@author: ljc
"""
import collections

class Solution:
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        def neighbors(i, j, m, n):
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= x < m and 0 <= y < n:
                    yield x, y
                    
        queue = collections.deque()
        visited = set()
        zeros = collections.deque()
        m, n = len(A), len(A[0])
        found = False
        for i in range(m):
            if found:
                break
            for j in range(n):
                if A[i][j] == 1:
                    queue.append((i, j))
                    visited.add((i, j))
                    found = True
                    break
        while queue:
            size = len(queue)
            for _ in range(size):
                x, y = queue.popleft()
                for nx, ny in neighbors(x, y, m, n):
                    if (nx, ny) not in visited:
                        visited.add((nx, ny))
                        if A[nx][ny] == 1:
                            queue.append((nx, ny))
                        else:
                            zeros.append((nx, ny, 0))
        while zeros:
            size = len(zeros)
            for _ in range(size):
                x, y, steps = zeros.popleft()
                for nx, ny in neighbors(x, y, m, n):
                    if (nx, ny) not in visited:
                        visited.add((nx, ny))
                        if A[nx][ny] == 1:
                            return steps + 1
                        zeros.append((nx, ny, steps + 1))