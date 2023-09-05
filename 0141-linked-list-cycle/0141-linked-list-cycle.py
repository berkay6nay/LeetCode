# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        
        node_list = []
        
        while head:
            
            if head in node_list:
                return True
            node_list.append(head)
            
            head = head.next
        
        return False
        