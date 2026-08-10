class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # dp[i] stores whether the player whose turn it is can win with i stones
        dp = [False] * (n + 1)
        
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                if not dp[i - j * j]:
                    dp[i] = True
                    break  # No need to check other moves for this state
                j += 1
                
        return dp[n]

        