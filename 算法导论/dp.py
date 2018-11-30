# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 22:20:29 2018

@author: ljc
"""

w = [0,4,3,0.5,2]# keep in mind that the w matrix's data should in same datatype
p = [0,3000,2000,1500,2000]
n = len(w) - 1   
m = 4   
v = 0
optp = [[0 for col in range(m + 1)] for raw in range(n + 1)]
import numpy as np
def knapsack_dynamic(w, p, n, m):
    
    # make choice more accurate
#    w_new = list(np.arange(round(min(w[1:]),2),m+round(min(w[1:]),2),round(min(w[1:]),2)))
    w_new = [round(min(w[1:])+min(w[1:])*i,2) for i in range(int(max(w)//min(w[1:])))]
    w_new = [0] + w_new
    print(w_new)
    # initialize optp
    optp = [[0 for col in range(len(w_new))] for raw in range(n + 1)]
    for i in range(1, n + 1):       
        for j in range(1, len(w_new)):   
            print(w_new[j],w[i])
            if w_new[j]>=w[i]: # if the bag is bigger than new item
                if w_new[j] - w[i] >= min(w):# if extra bag room can make more price
                    optp[i][j] = max((p[i] + optp[i-1][w_new.index(max(k for k in w if k<=(w_new[j] - w[i])))]),optp[i-1][j])
                else:
                    optp[i][j] = max(p[i],optp[i-1][j])
            else:
                optp[i][j] = optp[i-1][j]       
    return np.array(optp)
a = knapsack_dynamic(w, p, n, m)
print(a)
