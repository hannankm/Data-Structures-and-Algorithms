# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3=head=ListNode()
        while list1 and list2:
            if list1.val>=list2.val:
                list3.next=list2
                list2=list2.next
            else:
                list3.next=list1
                list1=list1.next
            list3=list3.next

        while list1:
            list3.next=list1
            list1=list1.next
            list3=list3.next
        while list2:
            list3.next=list2
            list2=list2.next
            list3=list3.next
        return head.next
      
        #while there is an element in both the nodes
        #compare the values of both the nodes,
        #set the element in answer node to the least of the two
        #if first > second: third= second
        #increment second
        #else: third= first
        #increment first
        #increement third, out of the if/else block
        #while there is an element in first node
        #increment first and third
        #while there is an element in second node
        #increment second and third
