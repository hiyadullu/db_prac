class Solution {
    public boolean stoneGameIX(int[] stones) {
        // Array to store the frequency of remainders: index 0, 1, and 2
        int[] counts = new int[3];
        for (int stone : stones) {
            counts[stone % 3]++;
        }
        
        // Scenario 1: Even number of Type 0 stones
        if (counts[0] % 2 == 0) {
            // Alice needs at least one Type 1 and one Type 2 stone to force a win
            return Math.min(counts[1], counts[2]) > 0;
        }
        
        // Scenario 2: Odd number of Type 0 stones
        // Alice needs the difference between Type 1 and Type 2 stones to be greater than 2
        return Math.abs(counts[1] - counts[2]) > 2;
    }
}
