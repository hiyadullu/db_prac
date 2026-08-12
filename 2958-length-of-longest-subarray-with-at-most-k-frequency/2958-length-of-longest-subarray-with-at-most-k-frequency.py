class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        max_len = 0
        left = 0
        frequencies = {}
        
        for right in range(len(nums)):
            # Add right element to frequency map
            frequencies[nums[right]] = frequencies.get(nums[right], 0) + 1
            
            # Shrink window from left if current element exceeds frequency k
            while frequencies[nums[right]] > k:
                frequencies[nums[left]] -= 1
                left += 1
                
            # Calculate current valid window size
            max_len = max(max_len, right - left + 1)
            
        return max_len
