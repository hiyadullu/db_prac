import java.util.*;

class Solution {
    public List<String> maxNumOfSubstrings(String s) {
        int n = s.length();
        int[] first = new int[26];
        int[] last = new int[26];
        Arrays.fill(first, -1);
        Arrays.fill(last, -1);
        
        // Step 1: Record first and last occurrences of each character
        for (int i = 0; i < n; i++) {
            int charIdx = s.charAt(i) - 'a';
            if (first[charIdx] == -1) {
                first[charIdx] = i;
            }
            last[charIdx] = i;
        }
        
        List<int[]> validIntervals = new ArrayList<>();
        
        // Step 2: Expand intervals to meet the validity rule
        for (int i = 0; i < 26; i++) {
            if (first[i] == -1) continue;
            
            int start = first[i];
            int end = last[i];
            boolean isValid = true;
            
            for (int j = start; j <= end; j++) {
                int currCharIdx = s.charAt(j) - 'a';
                
                // If this character appeared before our starting point, 
                // this interval cannot start cleanly at 'start'.
                if (first[currCharIdx] < start) {
                    isValid = false;
                    break;
                }
                // Dynamically extend the right boundary
                end = Math.max(end, last[currCharIdx]);
            }
            
            if (isValid) {
                validIntervals.add(new int[]{start, end});
            }
        }
        
        // Step 3: Greedy Interval Scheduling (Sort by earliest end time)
        Collections.sort(validIntervals, (a, b) -> Integer.compare(a[1], b[1]));
        
        List<String> result = new ArrayList<>();
        int prevEnd = -1;
        
        for (int[] interval : validIntervals) {
            int start = interval[0];
            int end = interval[1];
            
            // If the current interval starts after the last chosen one ends
            if (start > prevEnd) {
                result.add(s.substring(start, end + 1));
                prevEnd = end;
            }
        }
        
        return result;
    }
}
