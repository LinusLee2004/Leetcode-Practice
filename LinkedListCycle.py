class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class LinkedListCycle():
    def hasCycle(self, head):
        cycleSet = set()
        while head:
            current = head
            if current not in cycleSet:
                cycleSet.add(current)
            else:
                return True
            head = head.next
        return False