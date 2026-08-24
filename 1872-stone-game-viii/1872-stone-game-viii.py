class Solution:
    def stoneGameVIII(self, stones: list[int]) -> int:
        n = len(stones)
        
        # Step 1: Compute total prefix sum
        pref_sum = sum(stones)
        
        # Step 2: Base case - if forced to take all stones up to the last element
        ans = pref_sum
        
        # Step 3: Bottom-up space-optimized DP
        for i in range(n - 2, 0, -1):
            pref_sum -= stones[i + 1]  # Update prefix sum for index i
            ans = max(ans, pref_sum - ans)
            
        return ans
