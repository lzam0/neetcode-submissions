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
            # save the next node
            nextNode = currNode.next

            # save the current node
            currNode.next = prevNode

            # reverse the pointer
            prevNode = currNode
            
            # move current Node forward
            currNode = nextNode

        return prevNode
            