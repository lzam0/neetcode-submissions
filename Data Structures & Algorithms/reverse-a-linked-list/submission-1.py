# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currNode = head
        prev = None

        # print the linked list
        while currNode:
            # save the next node before we override
            nextNode = currNode.next

            # reverse the pointer
            currNode.next = prev

            # move the prev forward
            prev = currNode

            # move currNode forward
            currNode = nextNode

        return prev
