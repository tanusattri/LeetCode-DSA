class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        ans=0
        for i in patterns:
            if word.find(i)!=-1:
                ans+=1
        return ans 