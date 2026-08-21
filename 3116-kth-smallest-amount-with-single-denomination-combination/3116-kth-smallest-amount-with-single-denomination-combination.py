import math

class Solution:
    def findKthSmallest(self, coins: list[int], k: int) -> int:
        # Precompute the LCM for all possible subsets to save time during binary search
        n = len(coins)
        subsets = [] # Stores tuple of (lcm, size_of_subset)
        
        # There are 2^n - 1 non-empty subsets
        for i in range(1, 1 << n):
            current_lcm = 1
            subset_size = 0
            overflow = False
            
            for j in range(n):
                if (i >> j) & 1:
                    subset_size += 1
                    # Calculate LCM: (a * b) // gcd(a, b)
                    current_lcm = (current_lcm * coins[j]) // math.gcd(current_lcm, coins[j])
                    # Optimization: If LCM exceeds upper limit, it won't impact our count
                    if current_lcm > 10**11: 
                        overflow = True
                        break
            
            if not overflow:
                subsets.append((current_lcm, subset_size))
                
        # Helper function to count unique multiples <= mid
        def count_multiples(mid: int) -> int:
            total = 0
            for lcm, size in subsets:
                if size % 2 == 1:
                    total += mid // lcm
                else:
                    total -= mid // lcm
            return total

        # Binary search for the exact kth amount
        low = min(coins)
        high = min(coins) * k
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            if count_multiples(mid) >= k:
                ans = mid
                high = mid - 1  # Try to find a smaller valid amount
            else:
                low = mid + 1   # Increase the amount limit
                
        return ans
  