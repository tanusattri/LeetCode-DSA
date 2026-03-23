class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
            memo={}
            def ed(m,n):
                if m==0:
                    return n
                if n==0:
                    return m
                if (m,n) in memo:
                    return memo[(m,n)]
                if word1[m-1]== word2[n-1]:
                    res= ed(m-1,n-1)
                else:
                    res= 1+min(ed(m,n-1),ed(m-1,n),ed(m-1,n-1)) 
                memo[(m,n)]= res
                return res
            return ed(len(word1),len(word2))