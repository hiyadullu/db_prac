class Solution:
    def countCommas(self, n: int) -> int:
        # If n < 1000, it returns 0. 
        # If n >= 1000, it counts 1 comma for each number from 1000 to n.
        return max(0, n - 999)
       