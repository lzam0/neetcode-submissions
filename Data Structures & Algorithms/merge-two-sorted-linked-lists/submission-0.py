# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # iteration

        dummy = node = ListNode()

        # check if there are nodes available in the linkedlist
        while list1 and list2:

            # if list1 val is less than list2 val
            if list1.val < list2.val:
                # make the next node
                node.next = list1
                list1 = list1.next
            else:
                # make the next node
                node.next = list2
                list2 = list2.next
            
            node = node.next
        
        node.next = list1 or list2

        return dummy.next