# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 15:47:20 2018

@author: ljc
"""

class Solution:
    def wordBreak(self, s, wordDict):
        memo={}
        def dfs(s):
            if s == '':
                return True
            
            if s in memo:
                return memo[s]
            
            for word in wordDict:
                #print("s[:len(word)]",s[:len(word)])
                if word == s[:len(word)]:
                    if dfs(s[len(word):]):
                        memo[s] = True
                        return memo[s]
            memo[s] = False
            return False
        
        return dfs(s)