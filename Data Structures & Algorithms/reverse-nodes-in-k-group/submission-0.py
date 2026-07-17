# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        tmp = head
        n = 0
        while tmp:
            tmp = tmp.next
            n += 1

        head, tail, nxt = self.reverse(head, k)
        sentinel = ListNode(next=head)
        while nxt:
            if n-k < k:
                tail.next = nxt
                break
            nhead, ntail, nnxt = self.reverse(nxt, k)
            tail.next = nhead
            tail = ntail
            nxt = nnxt
            head = nnxt
            n -= k
        return sentinel.next


    def reverse(self, node: ListNode, k: int) -> Tuple[ListNode, ListNode, ListNode]:
        prev, curr = None, node
        while k and curr:
            nxt = curr.next
            curr.next = prev
            prev, curr = curr, nxt
            k -= 1
        return prev, node, curr
