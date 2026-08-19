from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        # Map row number to a bitmask of reserved seats
        # We only care about seats 2 to 9
        row_masks = defaultdict(int)
        for row, seat in reservedSeats:
            if 2 <= seat <= 9:
                row_masks[row] |= (1 << (seat - 2))
                
        # Bitmasks for our 3 target blocks (shifted to look at seats 2-9)
        # Left block (2,3,4,5) -> bits 0,1,2,3 -> 0b1111 (15)
        # Middle block (4,5,6,7) -> bits 2,3,4,5 -> 0b111100 (60)
        # Right block (6,7,8,9) -> bits 4,5,6,7 -> 0b11110000 (240)
        left_mask = 15     # 0b00001111
        middle_mask = 60   # 0b00111100
        right_mask = 240   # 0b11110000
        
        ans = 0
        
        # Process only the rows that have reservations
        for mask in row_masks.values():
            # If both Left and Right blocks are clear, we can fit 2 groups
            if (mask & left_mask) == 0 and (mask & right_mask) == 0:
                ans += 2
            # Otherwise, check if we can fit at least 1 group in Left, Middle, or Right
            elif (mask & left_mask) == 0 or (mask & middle_mask) == 0 or (mask & right_mask) == 0:
                ans += 1
                
        # Any row without any reservations automatically fits 2 groups
        empty_rows = n - len(row_masks)
        ans += empty_rows * 2
        
        return ans
    