# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 15:05:57 2018

@author: ljc
"""
import time
class Solution:
    def __init__(self):
        self.mem_body = dict()
    def solve(self, board):
        def get_nei(p):
            i,j = p[0],p[1]
            nei = []
            if (i,j) not in visited:
                visited.append((i,j))
#            print(i+1,j+1)
            if j+1<len(board[0]) and (i,j+1) not in visited and board[i][j+1] == 'O':
                nei.append((i,j+1))
                visited.append((i,j+1))
            if i+1<len(board) and (i+1,j) not in visited and board[i+1][j] == 'O':
                nei.append((i+1,j))
                visited.append((i+1,j))
            if i-1>=0 and (i-1,j) not in visited and board[i-1][j] == 'O':
                nei.append((i-1,j))
                visited.append((i-1,j))
            if j-1>=0 and (i,j-1) not in visited and board[i][j-1] == 'O':
                nei.append((i,j-1))
                visited.append((i,j-1))
            return nei
        def bfs(i,j):
            queue = []
            queue.append((i,j))
            qi = []
            while queue:
#                print(visited)
                cp = queue.pop(0)
                print(isalive(cp),cp,len(board))

                qi.append(cp)
                if isalive(cp) and qi[0]!=-1:
                    qi.insert(0,-1)
#                print(cp)
                nei = get_nei(cp)
#                print('nei',nei)
                for j in nei:
                    queue.append(j)
                    
            return qi
        def isalive(p):
            i = p[0]
            j = p[1]
            if i==0 or j==0 or j==len(board[0])-1 or i==len(board)-1:
                return True
            else:
                return False
        if not board:
            pass
        else:
            new_board = [[0 for i in board[0]] for j in board]
            visited = []
            m = len(board)
            n = len(board[0])
            for i in range(m):
                for j in range(n):
                    if board[i][j] == 'O' and  (i,j) not in visited:
                        qi = bfs(i,j)

                        if qi[0] == -1:
                            for _ in qi[1:]:
                                new_board[_[0]][_[1]] = 1
            for i in range(m):
                board.pop(i)
                row_str =[]
                for j in range(n):
                    k = new_board[i][j]
                    if k == 0:
                        row_str.append('X')
                    else:
                        row_str.append('O')
                board.insert(i,row_str)
        
        print(board)
a = Solution()
#board = ['XXXXX',
#         'XOOXX',
#         'XOXOX',
#         'XOXXX']
board = [["X","X","X","X"],
         ["X","O","O","X"],
         ["X","X","O","X"],
         ["X","O","X","X"]]
b = a.solve(board)
#print(b)
