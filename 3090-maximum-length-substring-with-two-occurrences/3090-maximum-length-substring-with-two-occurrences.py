class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        char_counts = {}
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            # Add the current character to the window
            char_counts[s[right]] = char_counts.get(s[right], 0) + 1
            
            # If a character occurs more than twice, shrink the window from the left
            while char_counts[s[right]] > 2:
                char_counts[s[left]] -= 1
                left += 1
                
            # Calculate and update the maximum valid substring length
            max_len = max(max_len, right - left + 1)
            
        return max_len
