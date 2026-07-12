class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr= sorted(arr)
        rank= {}
        curr_rank=1
        for num in sorted_arr:
            if num not in rank:
                rank[num]= curr_rank
                curr_rank+=1
        return [rank[num] for num in arr] 