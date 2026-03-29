class Solution:
    def removeElements(self, head, val):
        node = ListNode()
        node.next = head
        temp = node
        while temp.next is not None:
            if temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return node.next