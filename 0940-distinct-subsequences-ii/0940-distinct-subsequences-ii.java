class Solution {
    public int distinctSubseqII(String s) {
        int MOD = 1_000_000_007;
        
        // dp[i] will store the number of distinct subsequences ending with character ('a' + i)
        long[] dp = new long[26];
        
        for (int i = 0; i < s.length(); i++) {
            int charIndex = s.charAt(i) - 'a';
            
            // Calculate the total number of distinct subsequences found so far
            long currentTotalSubsequences = 0;
            for (long count : dp) {
                currentTotalSubsequences = (currentTotalSubsequences + count) % MOD;
            }
            
            // The new character can extend all existing subsequences, plus form a single-character subsequence
            dp[charIndex] = (currentTotalSubsequences + 1) % MOD;
        }
        
        // Sum up the distinct subsequences ending with each of the 26 characters
        long finalCount = 0;
        for (long count : dp) {
            finalCount = (finalCount + count) % MOD;
        }
        
        return (int) finalCount;
    }
}
