# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        
        first, last = head, prev
        while last:
            fnxt, lnxt = first.next, last.next
            first.next = last
            last.next = fnxt
            first, last = fnxt, lnxt

        # l = []
        # curr = head
        # while curr:
        #     l.append(curr)
        #     curr = curr.next

        # n = len(l)
        # if n == 1:
        #     return

        # first, last = None, None
        # for i in range(n//2):
        #     first, last = l[i], l[n-i-1]
        #     first.next = last
        #     last.next = l[i+1]
        
        # if n % 2:
        #     last.next.next = None
        # else:
        #     last.next = None

