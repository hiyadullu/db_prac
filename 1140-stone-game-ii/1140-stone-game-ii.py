class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        n = len(piles)
        
        # 1. Compute suffix sums for O(1) total remaining stones lookup
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
            
        # Memoization dictionary to store (index, M) -> max stones
        memo = {}
        
        def dp(i: int, m: int) -> int:
            # Base Case: Current player can grab all remaining piles
            if i + 2 * m >= n:
                return suffix_sum[i]
            
            # Return cached result if already computed
            if (i, m) in memo:
                return memo[(i, m)]
            
            # Opponent wants to minimize our score, so find the minimum
            # score the opponent can achieve from the next state.
            min_opponent_score = float('inf')
            for x in range(1, 2 * m + 1):
                min_opponent_score = min(min_opponent_score, dp(i + x, max(m, x)))
            
            # Our max stones = Total available stones - Opponent's min optimal stones
            memo[(i, m)] = suffix_sum[i] - min_opponent_score
            return memo[(i, m)]
        
        # Alice starts at index 0 with M = 1
        return dp(0, 1)
