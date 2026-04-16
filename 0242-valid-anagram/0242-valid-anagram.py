class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m= len(s)
        n= len(t)
        if m!=n:
            return False
        countS= {}
        countT= {}
        for i in range(m):
            countS[s[i]]= countS.get(s[i],0)+1
            countT[t[i]]= countT.get(t[i],0)+1
        return countS== countT