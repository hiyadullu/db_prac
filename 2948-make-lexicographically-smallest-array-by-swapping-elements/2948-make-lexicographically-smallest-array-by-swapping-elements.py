from collections import deque

class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        n = len(nums)
        # Pair each number with its original index and sort by value
        sorted_pairs = sorted((val, idx) for idx, val in enumerate(nums))
        
        ans = [0] * n
        
        # We will iterate through sorted pairs and segment them into groups
        i = 0
        while i < n:
            j = i + 1
            # Find the boundary of the current connected component group
            while j < n and sorted_pairs[j][0] - sorted_pairs[j-1][0] <= limit:
                j += 1
            
            # Extract elements belonging to the current group
            group_pairs = sorted_pairs[i:j]
            
            # Extract and sort the original indices for this group
            indices = sorted(idx for val, idx in group_pairs)
            
            # Assign the sorted values to the sorted original indices
            for k in range(len(indices)):
                ans[indices[k]] = group_pairs[k][0]
                
            i = j # Move to the next group
            
        return ans
