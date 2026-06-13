class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result= []
        for word in words:
            total= sum(weights[ord(c) - ord('a')] for c in word)
            remain= total%26
            result.append(chr(ord('z') - remain))
        return "".join(result)