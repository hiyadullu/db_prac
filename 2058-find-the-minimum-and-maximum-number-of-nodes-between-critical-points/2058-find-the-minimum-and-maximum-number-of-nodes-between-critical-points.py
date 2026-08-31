# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> list[int]:
        # We need at least 3 nodes to have a critical point
        if not head or not head.next or not head.next.next:
            return [-1, -1]
            
        first_cp = -1
        prev_cp = -1
        
        min_dist = float('inf')
        
        # Start scanning from the second node (index 1)
        prev_val = head.val
        curr = head.next
        pos = 1
        
        while curr.next:
            next_val = curr.next.val
            
            # Check if current node is a local maxima or local minima
            is_maxima = curr.val > prev_val and curr.val > next_val
            is_minima = curr.val < prev_val and curr.val < next_val
            
            if is_maxima or is_minima:
                if first_cp == -1:
                    first_cp = pos
                else:
                    # Update minimum distance with adjacent critical point
                    min_dist = min(min_dist, pos - prev_cp)
                    
                prev_cp = pos
                
            prev_val = curr.val
            curr = curr.next
            pos += 1
            
        # If we didn't find at least two critical points
        if first_cp == prev_cp:
            return [-1, -1]
            
        max_dist = prev_cp - first_cp
        return [min_dist, max_dist]
