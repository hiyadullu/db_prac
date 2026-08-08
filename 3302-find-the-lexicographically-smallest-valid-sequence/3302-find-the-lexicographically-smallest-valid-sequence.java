class Solution {
    public int[] validSequence(String word1, String word2) {
        int n = word1.length();
        int m = word2.length();
        
        int[] suffix = new int[n + 1];
        suffix[n] = m;
        
        int j = m - 1;
        for (int i = n - 1; i >= 0; i--) {
            if (j >= 0 && word1.charAt(i) == word2.charAt(j)) {
                j--;
            }
            suffix[i] = j + 1;
        }
        
        int[] ans = new int[m];
        int ansIdx = 0;
        j = 0;
        boolean changed = false;
        
        for (int i = 0; i < n; i++) {
            if (j == m) break;
            
            if (word1.charAt(i) == word2.charAt(j)) {
                ans[ansIdx++] = i;
                j++;
            } else if (!changed && suffix[i + 1] <= j + 1) {
                ans[ansIdx++] = i;
                j++;
                changed = true;
            }
        }
        
        return ansIdx == m ? ans : new int[0];
    }
}
