class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_s= set()
        n= len(s)
        left=0
        max_len=0
        for right in range(n):
            while s[right] in window_s:
                window_s.remove(s[left])
                left+=1
            window_s.add(s[right])
            max_len= max(max_len, right-left+1)
        return max_len