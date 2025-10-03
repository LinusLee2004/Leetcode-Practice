# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ReverseLinkedList():
    def reverseList(self, head):
        previous = None
        head = head
        next = head.next
        while head:
            