# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 17:45:52 2018

@author: ljc
"""

class Solution:
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        : input [[1,1,1,1,1],
                 [1,0,0,0,1],
                 [1,0,1,0,1],
                 [1,0,0,0,1],
                 [1,1,1,1,1]]
        : input [[0,1,0],
                 [0,0,0],
                 [0,0,1]]
        : input [[0,1],
                 [1,0]]
        """
        
        visited = []

        def get_nei(p):
            i,j = p[0],p[1]
            nei = []
            if (i,j) not in visited:
                visited.append((i,j))
#            print(i+1,j+1)
            if j+1<len(A[0]) and (i,j+1) not in visited and A[i][j+1] == 1:
                nei.append((i,j+1))
                visited.append((i,j+1))
            if i+1<len(A) and (i+1,j) not in visited and A[i+1][j] == 1:
                nei.append((i+1,j))
                visited.append((i+1,j))
            if i-1>=0 and (i-1,j) not in visited and A[i-1][j] == 1 :
                nei.append((i-1,j))
                visited.append((i-1,j))
            if j-1>=0 and (i,j-1) not in visited and A[i][j-1] == 1 :
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
#                print(isalive(cp),cp,len(A))

                qi.append(cp)
#                if isalive(cp) and qi[0]!=-1:
#                    qi.insert(0,-1)
#                print(cp)
                nei = get_nei(cp)
#                print('nei',nei)
                for j in nei:
                    queue.append(j)
                    
                    
            return qi
        m = len(A)
        n = len(A[0])
        il = []
        for i in range(m):
            for j in range(n):
#                print(visited,(i,j))
                if A[i][j] == 1 and  (i,j) not in visited:
#                    il.append(bfs(i,j))
                    il.append(bfs(i,j))
#                    print(il)
#        print('il',il)
        def cal_dst(il1,il2):
            min_value = float('inf')
            min_index = ()
            for i in range(len(il1)):
                for j in range(len(il2)):
                    if abs(il1[i][0]-il1[i][1])+abs(il2[j][0]-il2[j][1])<min_value:
                        min_index = (i,j)
                        min_value = abs(il1[i][0]-il2[j][0])+abs(il1[i][1]-il2[j][1])
                    
                    
            return il1[min_index[0]]
                    
                    
                    
                    
                    
#        def get_start(A):
#            for i in range(len(A)):
#                for j in range(len(A[0])):
#                    if isiland((i,j)):
#                        start = (i,j)
#                        #print(start)
#                        return start
        def get_nei_2(p,visited):
            i,j = p[0],p[1]
            nei = []
#            if (i,j) not in visited:
#                visited.append((i,j))
            if j+1<len(A[0]) and (i,j+1) not in visited:
                if A[i][j+1] == 1 and A[i][j]!=1:
#                    if i-1>=0 and A[i-1][j+1] == 0:
#                        return True
#                    elif i+1<len(A) and A[i+1][j+1] == 0:
#                        return True
                    return True
                else:
                    nei.append((i,j+1))
#                    visited.append((i,j+1))
            if i+1<len(A) and (i+1,j) not in visited:
                if A[i+1][j] ==1 and A[i][j]!=1:
#                    if j-1>=0 and A[i+1][j-1] == 0:
#                        return True
#                    elif j+1<len(A) and A[i+1][j+1] == 0:
#                        return True
                    return True

                else:
                    nei.append((i+1,j))
#                    visited.append((i+1,j))
            if i-1>=0 and (i-1,j) not in visited:
                if A[i-1][j] == 1 and A[i][j]!=1:
#                    if j-1>=0 and A[i-1][j-1] == 0:
#                        return True
#                    elif j+1<len(A) and A[i-1][j+1] == 0:
#                        return True
                    return True

                else:
                    nei.append((i-1,j))
#                    visited.append((i-1,j))
            if j-1>=0 and (i,j-1) not in visited:
                if A[i][j-1] == 1 and A[i][j]!=1:
#                    if i-1>=0 and A[i-1][j-1] == 0:
#                        return True
#                    elif i+1<len(A) and A[i+1][j-1] == 0:
#                        return True
                    return True
                else:
                    nei.append((i,j-1))
#                    visited.append((i,j-1))
            return nei
        def dfs(i,j,visited=[]):
            layer_stack = {}
#            length = float('inf')
            counter = 0
            layer_stack[counter] = []
            layer_stack[counter].append((i,j))
            while True:
                
                layer_stack[counter+1] = []
                
                while layer_stack[counter]:
#                    print(visited)
                    
                    cp = layer_stack[counter].pop(0)
#                    print(layer_stack[counter])
                    visited.append(cp)
#                    qi.append(cp)
    
    #                print(stack,cp)
                    nei = get_nei_2(cp,visited)
#                    print(nei,cp,visited)
                    if isinstance(nei,bool):
#                        print('True',len(qi))
    #                    qi.pop()
    #                    length =  min(length,len(qi))
    #                    break
                        return counter
                    else:
                        for j in nei:
                            layer_stack[counter+1].append(j)
                counter +=1
                
#            return length
#        visited = []
#        start = get_start(A)
        il1 = il[0]
        il2 = il[1]
#        visited = il1+il2
#        print(visited)
        start = cal_dst(il1,il2)
#        print(start)
        return dfs(start[0],start[1])
#        def find_is(A):
A=[[1,1,1,1,1],
   [1,0,0,0,1],
   [1,0,1,0,1],
   [1,0,0,1,1],
   [1,1,1,1,1]]
#A = [[0,1,0,0,0],
#     [0,1,0,1,1],
#     [0,0,0,0,1],
#     [0,0,0,0,0],
#     [0,0,0,0,0]]
#A = [[0,1,0,0],
#     [0,0,0,0],
#     [0,0,0,1]]
a = Solution()
b = a.shortestBridge(A)
print(b)

        