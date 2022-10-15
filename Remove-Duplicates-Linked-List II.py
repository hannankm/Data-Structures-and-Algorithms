# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



#Get the first unique element
#Change the next values of the prevoius nodes
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        unique= ListNode(0, next=head)
        slow=unique
        while head:
            if head.next and head.val==head.next.val:
                while head.next and head.val==head.next.val:
                    head=head.next
                slow.next=head.next
            else:
                slow= slow.next
            head=head.next
            
        return unique.next
                    
