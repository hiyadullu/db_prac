class Solution:
    def missingMultiple(self, nums: list[int], k: int) -> int:
        # Convert array to a set for O(1) lookups
        num_set = set(nums)
        
        multiple = k
        # Keep checking subsequent multiples until a gap is found
        while multiple in num_set:
            multiple += k
            
        return multiple

      