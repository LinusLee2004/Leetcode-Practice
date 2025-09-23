#Definition of ListNode:
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class mergeLists():
    def mergeTwoLists(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


    def mergeLists(self, list1, list2):
        current = head = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        current.next = list1 or list2
        return head.next

# Helper functions
def create_linked_list(arr):
    dummy = current = ListNode()
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def print_linked_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    print(res)

# Test code (runs immediately when script is executed)
list1 = create_linked_list([2, 5, 5, 5])
list2 = create_linked_list([1, 7, 8])

solution = mergeLists()
merged = solution.mergeLists(list1, list2)
print_linked_list(merged)  # Output: [1, 1, 2, 3, 4, 4]

