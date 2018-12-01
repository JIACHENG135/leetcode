# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 19:47:47 2018

@author: ljc
"""

class Solution:
    
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        BFS
        """
        """
        if not board:
            return
        import collections
        m = len(board)
        n = len(board[0])
        
        q = collections.deque()
        
        for i in range(m):
            for j in range(n):
                if (i in [0, m-1] or j in [0, n-1]) and board[i][j] == "O":
                    q.append((i,j))
        
        
        while q:
            r,c = q.popleft()
            if 0 <= r <m and 0 <= c <n and board[r][c] == 'O':
                board[r][c]  = 'S'          
                q.append((r-1, c))       
                q.append((r+1, c))
                q.append((r, c-1))
                q.append((r, c+1))
                
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "S":
                    board[i][j] = "O"
        """
        def dfs(i,j):
            if i >= 0 and i < len(board) and j >= 0 and j < len(board[0]) and board[i][j] == "O":
                board[i][j] = "S"
                dfs(i-1,j)
                dfs(i+1,j)
                dfs(i,j-1)
                dfs(i,j+1)
        
        if not board:
            return
        
        for i in range(len(board)):
            for j in [0, len(board[0])-1]:
                if board[i][j] == "O":
                    dfs(i,j)
        
        for j in range(1, len(board[0])-1):
            if board[0][j] == "O":
                dfs(0, j)
            if board[len(board)-1][j] == "O":
                dfs(len(board)-1, j)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "S":
                    board[i][j] = "O"