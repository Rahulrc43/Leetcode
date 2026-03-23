class Solution(object):
    def isPalindrome(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        prev, curr = None, slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev, curr = curr, nxt
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left, right = left.next, right.next
        return True
