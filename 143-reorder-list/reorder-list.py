# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return None
        slow=head
        fast=head.next
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        secondNode=slow.next
        slow.next=None
        temp=secondNode
        prevNode=None
        while temp:
            nextNode=temp.next
            temp.next=prevNode
            prevNode=temp
            temp=nextNode
        firstNode=head
        secondNode=prevNode
        while secondNode:
            temp1=firstNode.next
            temp2=secondNode.next

            firstNode.next=secondNode
            secondNode.next=temp1

            firstNode=temp1
            secondNode=temp2

