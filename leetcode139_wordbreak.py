# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 14:15:03 2018

@author: ljc
"""

class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        memo={}
        def dfs(s):
#            print(memo)
            if s=='':
                return True
            if s in memo:
                return memo[s]
            for word in wordDict:
                print(word,memo)
                if s[:len(word)]==word:
                    if dfs(s[len(word):]):
                        memo[s] = True
                        return memo[s]
            memo[s] = False
            return False
        return dfs(s)
    
    
a = Solution()
b = a.wordBreak('adaaaaaaaaaaaaaaacaaab',['a','adaa','aca','aaaaa','aaaaaaa','ab','aaaa'])
print(b)