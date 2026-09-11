import java.util.HashMap;
import java.util.Map;

class Solution {
    public int totalNumbers(int[] digits) {
        // Step 1: Count available digits
        int[] available = new int[10];
        for (int d : digits) {
            available[d]++;
        }
        
        int validCount = 0;
        
        // Step 2: Loop through all possible 3-digit even numbers
        for (int num = 100; num < 1000; num += 2) {
            int d1 = num / 100;
            int d2 = (num / 10) % 10;
            int d3 = num % 10;
            
            // Track needed counts for this specific number
            int[] needed = new int[10];
            needed[d1]++;
            needed[d2]++;
            needed[d3]++;
            
            // Step 3: Verify availability
            if (available[d1] >= needed[d1] && 
                available[d2] >= needed[d2] && 
                available[d3] >= needed[d3]) {
                validCount++;
            }
        }
        
        return validCount;
    }
}
