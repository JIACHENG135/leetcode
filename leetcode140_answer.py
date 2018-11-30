# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 10:42:11 2018

@author: ljc
"""

class Solution:
    def __init__(self):
        self.mem = dict()
    
    def wordBreak(self, s, wordDict, longest_word = 0):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        ret = list()
#        print(self.mem,s)
        if not s or not wordDict:
            return ret
        if s in self.mem:
            return self.mem[s]
        if isinstance(wordDict, list):
            wordDict = set(wordDict)
        longest_word = longest_word or max(map(len, wordDict))
        if s in wordDict:
            ret += [s]
        e = 1
        while e <= longest_word:
            current_word = s[:e]
            if current_word in wordDict:
                sub_words = self.wordBreak(s[e:], wordDict, longest_word)
                print(sub_words,self.mem)
                for ws in sub_words:
                    ret += [current_word + " " + ws]
            e += 1
        
        self.mem[s] = ret
        return ret
    
a = Solution()
#b = a.wordBreak(,)
#s = 'ljcshi'
#wordDict = ['ljc','da','shuai','ge','shi','shid','a'];
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
#s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
#wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
#b = a.wordBreak01(s,wordDict)
b = a.wordBreak(s,wordDict)
#b = a.break_helper(s,'dog')


print(b)