class Solution {
    public int numDistinct(String s, String t) {
        int m = s.length();
        int n = t.length();
        
        // If s is shorter than t, t cannot be a subsequence of s
        if (m < n) {
            return 0;
        }
        
        // dp[j] stores the number of distinct subsequences matching t[0...j-1]
        int[] dp = new int[n + 1];
        
        // Base case: An empty string t has exactly 1 subsequence match (the empty set)
        dp[0] = 1;
        
        // Iterate through each character of string s
        for (int i = 1; i <= m; i++) {
            char sChar = s.charAt(i - 1);
            
            // Traverse backwards to use the values from the previous row
            for (int j = n; j >= 1; j--) {
                char tChar = t.charAt(j - 1);
                
                // If characters match, we can either:
                // 1. Include sChar to match tChar -> dp[j-1]
                // 2. Exclude sChar and look for matches earlier in s -> dp[j]
                if (sChar == tChar) {
                    dp[j] = dp[j] + dp[j - 1];
                }
                // If characters don't match, dp[j] remains unchanged
            }
        }
        
        return dp[n];
    }
}
