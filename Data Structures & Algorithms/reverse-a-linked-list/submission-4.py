# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevNode = None
        currNode = head

        while currNode:
            # firstly we save the next currNode
            nextNode = currNode.next

            # make currNode.next = prevNode
            currNode.next = prevNode

            # prevNode = currNode
            prevNode = currNode

            # move current node forward
            currNode = nextNode

        return prevNode