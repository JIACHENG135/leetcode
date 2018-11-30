# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 16:36:54 2018

@author: ljc
"""

class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        import copy
        def hash_board(board):
            table = {}
            for i in range(len(board)):
                for j in range(len(board[0])):
                    table[str(i)+','+str(j)] = []
                    if j+1<=len(board[0])-1:
                        table[str(i)+','+str(j)].append(str(i)+','+str(j+1))
                    if i+1<=len(board)-1:
                        table[str(i)+','+str(j)].append(str(i+1)+','+str(j))
                    if i-1>=0:
                        table[str(i)+','+str(j)].append(str(i-1)+','+str(j))
                    if j-1>=0:
                        table[str(i)+','+str(j)].append(str(i)+','+str(j-1))
                        
            return table
        def dfs(i,j,l,stack=[]):
            print(i,j)
            if i==1 and j==1:print(table_l)
#            print(board[i][j]) 
            if str(i)+','+str(j) in table_l:
                if table_l[str(i)+','+str(j)]:
#                    print(stack)
                    index_temp = table_l[str(i)+','+str(j)]
                    print(stack,index_temp,l)
#                    print(table_l[str(i)+','+str(j)])
                    for k in index_temp:
                        if str(i)+','+str(j) in table_l[k]:
                            table_l[k].pop(table_l[k].index(str(i)+','+str(j)))
                        w = 0
                        int_1 =''
                        while k[w]!=',':
                            int_1 += k[w]
                            w+=1
                        int_2 = k[w+1:]
                        if i==1 and j==1:
                            print('==',int_1,int_2)
                        word_wait = board[int(int_1)][int(int_2)]   
#                        print(word_wait)
                        if word_wait == word[l]:
                            print(l,word_wait)
#                            print(word[l],l)
                            if l==len(word)-1:
                                return True
                            else:
                                l += 1
                                index_temp.pop(0)
                                stack.append(k)
#                                if l<=len(word)-1:
                                return dfs(int(k[0]),int(k[2]),l,stack)
#                    print(stack)
                    l -= 1
                    if stack:
                        stack.pop()
                    if not stack:
                        return False
                    else:
                        index_temp = stack[-1]
                        k = index_temp
                        return dfs(int(k[0]),int(k[2]),l,stack)
                                    
#                        return False
            else:
#                print('!=',table_l,str(i)+','+str(j))
                stack.pop()
                index_temp = stack[-1]
                return dfs(int(index_temp[0]),int(index_temp[2],l-1,stack))
            
        def get_start(board,word_0):
            res=[]
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == word_0:
                        res.append([i,j])
                        
            return res
        if not word:
            return False
        if len(word)==1:
            start = get_start(board,word[0])
            if start:
                return True
            else:
                return False
        start = get_start(board,word[0])
        print(start)
        table=hash_board(board)
#        print(table)
#        table_l = copy.deepcopy(table)
        if start:
            for i in start:
                l=1
                table_l = copy.deepcopy(table)
                if dfs(i[0],i[1],l):
                    return True
            return False
        else:
            return False
#        return dfs(1,0,1))
#        return hash_board(board)
    
    
a= Solution()
#board =[
#  ['A','B','C','E'],
#  ['S','F','C','S'],
#  ['A','D','E','E']
#]
#board = [["b","b","a","a","b","a"],
#         ["b","b","a","b","a","a"],
#         ["b","b","b","b","b","b"],
#         ["a","a","a","b","a","a"],
#         ["a","b","a","a","b","b"]]
# "abbbababaa"
board = [["C","A","A"],
         ["A","A","A"],
         ["B","C","D"]]
print(len(board),len(board[0]))
b = a.exist(board,"AAB")
print(b)
#print(b['0,0'][0][2])
#b['0,0'].pop(b['0,0'].index('0,1'))
#print(b)
