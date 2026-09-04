# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currNode = head
        prevNode = None

        while currNode:
            # define the next node
            nextNode = currNode.next

            # save the curr node as the previous node
            currNode.next = prevNode
            
            # move the prev node to currNode position
            prevNode = currNode
            
            # move onto the "next" node that we assigned earleir
            currNode = nextNode

        return prevNode