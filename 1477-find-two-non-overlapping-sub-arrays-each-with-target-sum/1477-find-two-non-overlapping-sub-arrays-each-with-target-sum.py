class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        # dp[i] will store the minimum length of a valid subarray found in arr[0...i]
        dp = [float('inf')] * n
        
        min_total_len = float('inf')
        current_window_sum = 0
        left = 0
        
        # Right pointer expands the window
        for right in range(n):
            current_window_sum += arr[right]
            
            # Shrink the window from the left if the sum is too big
            while current_window_sum > target:
                current_window_sum -= arr[left]
                left += 1
                
            # If we found a subarray that matches the target sum
            if current_window_sum == target:
                current_len = right - left + 1
                
                # Check if there is a valid, non-overlapping subarray before 'left'
                if left > 0 and dp[left - 1] != float('inf'):
                    min_total_len = min(min_total_len, dp[left - 1] + current_len)
                
                # Update the DP entry for the current right index
                dp[right] = min(dp[right], current_len)
            
            # Carry forward the best (minimum) length found so far to the next position
            if right > 0:
                dp[right] = min(dp[right], dp[right - 1])
                
        return min_total_len if min_total_len != float('inf') else -1
   