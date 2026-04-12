class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        val_to_indices= {}
        for idx, val in enumerate(nums):
            if val not in val_to_indices:
                val_to_indices[val]= []
            val_to_indices[val].append(idx)
        min_dist= float('inf')
        found= False
        for val in val_to_indices:
            indices= val_to_indices[val]
            if len(indices)<3:
                continue
            for i in range(len(indices)-2):
                curr_dist= 2*(indices[i+2]-indices[i])
                if curr_dist<min_dist:
                    min_dist= curr_dist
                    found= True
        return min_dist if found else -1