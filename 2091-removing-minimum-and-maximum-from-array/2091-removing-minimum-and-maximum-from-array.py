class Solution:
    def minimumDeletions(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
            
        # 1. Locate the indices of the min and max elements
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))
        
        # Ensure i is always the smaller index and j is the larger index
        i = min(min_idx, max_idx)
        j = max(min_idx, max_idx)
        
        # 2. Calculate costs for the three possible options
        from_front_only = j + 1
        from_back_only = n - i
        from_both_sides = (i + 1) + (n - j)
        
        # 3. Return the minimum cost
        return min(from_front_only, from_back_only, from_both_sides)
