# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 08:15:33 2018

@author: ljc
"""

class Solution:
    def __init__(self):
        self.mem = dict()
    def wordBreak(self, s, wordDict,longest_word = []):
        ret = list()
        longest_word = longest_word or max(map(len,wordDict))
        if s in self.mem:
            return self.mem[s]
        if s in wordDict:
            ret += [s]
        e = 1
        while e<=longest_word:
            current_word = s[:e]
            if current_word in wordDict:
                sub_word = self.wordBreak(s[e:],wordDict,longest_word)
                for j in sub_word:
                    ret += [current_word +' '+ j]
            e += 1
                    
        self.mem[s] = ret
        return ret
        
    
a = Solution()
b = a.wordBreak('ljcshidashuaige',['ljc','da','shuai','ge','shi','shid','a'])
#s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
#wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
#b = a.wordBreak(s,wordDict)

print(b)