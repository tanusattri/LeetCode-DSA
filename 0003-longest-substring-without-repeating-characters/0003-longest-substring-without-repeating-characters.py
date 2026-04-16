class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n= len(s)
        left=0
        max_length= 0
        count= {}
        for right in range(n):
            if s[right] in count and count[s[right]]>=left:
                left= count[s[right]]+1
            count[s[right]]= right
            max_length= max(max_length, right-left+1)
        return max_length