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

            # 1. Save the next node
            nextNode = currNode.next

            # 2. Save the current node
            currNode.next = prevNode

            # 3. Reverse the pointer
            prevNode = currNode

            # 4. Move the curr Node forward
            currNode = nextNode 


        return prevNode