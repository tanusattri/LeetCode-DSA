class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n= len(letters)
        if target>= letters[n-1]:
            return letters[0]
        start=0
        end= n-1
        res=-1
        while start<=end:
            mid= start+(end-start)//2
            if target== letters[mid]:
                start= mid+1
            elif target>letters[mid]:
                start= mid+1
            elif target<letters[mid]:
                res= mid
                end= mid-1
        if letters[res]<target:
            return letters[0]
        else:
            return letters[res]