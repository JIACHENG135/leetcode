# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 09:08:30 2018

@author: ljc
"""
import numpy as np
class Solution:

    def wordBreak01(self, s, wordDict):
        memo={}
        def dfs(s):
            if s == '':
                return 1
            
            if s in memo:
                return memo[s]
            
            for word in wordDict:
                #print("s[:len(word)]",s[:len(word)])
                if word == s[:len(word)]:
                    if dfs(s[len(word):]):
                        memo[s] = 1
                        return memo[s]
            memo[s] = 0
            return 0
        return dfs(s)
    def break_helper(self,s,word):
        k = 0
        while k<=len(s)-1:
            start = 0
#            print(k,len(s)-1,s[k],word[start])
            if s[k] == word[start]:
                k_temp = k
                while k_temp<=len(s)-1 and s[k_temp] == word[start] :
#                    print(k_temp,k)
                    if start == len(word)-1:
                        return [s[:k],s[k+start+1:]]
                    start += 1
                    k_temp += 1
#                print(s[k],word[start])
            k+=1
        return False
    def wordBreak(self,s,wordDict):
        optp =[[0 for i in range(len(s)+1)] for j in range(len(wordDict)+1)]
        for i in range(1,len(optp)):
            for j in range(1,len(optp[0])):
                if j >len(wordDict[i-1]):
                    s_temp = s[:j]
                    
                    
                    if self.break_helper(s_temp,wordDict[i-1]):
                        s_sub = self.break_helper(s_temp,wordDict[i-1])
#                        print(s_sub)
                        sub_res = 1
                        for k in s_sub:
                            sub_res *= self.wordBreak01(k,wordDict[:i])
                    else:
                        sub_res = 0   
    #                    self.wordBreak01(s_temp,wordDict[:i])*self.wordBreak01(s_temp[:len()],wordDict[:i])
                    optp[i][j] = max(optp[i-1][j],sub_res)
#                    print(s_temp,optp[i][j],wordDict[:i])
                else:
                    optp[i][j]=0
#        if optp[-1][-1]:
#            return True
#        else:
#            return False
        return np.array(optp)
        
        
    
#    def wordBreak(self, s, wordDict):
        
    
a = Solution()
#b = a.wordBreak(,)
#s = 'ljcshidashuaige'
#wordDict = ['ljc','da','shuai','ge','shi','shid','a'];
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
#s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
#wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
#b = a.wordBreak01(s,wordDict)
b = a.wordBreak(s,wordDict)
#b = a.break_helper(s,'dog')


print(b)