# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tmp = dummy

        carry = 0
        while l1 and l2:
            res = l1.val+l2.val+carry
            print(carry)
            tmp.next = ListNode(res%10)
            carry = res // 10
            l1 = l1.next
            l2 = l2.next
            tmp = tmp.next

        while l1:
            res = l1.val+carry
            tmp.next = ListNode(res%10)
            carry = res // 10
            l1 = l1.next
            tmp = tmp.next

        while l2:
            res = l2.val+carry
            tmp.next = ListNode(res%10)
            carry = res // 10
            l2 = l2.next
            tmp = tmp.next
        
        if carry: tmp.next = ListNode(carry)

        return dummy.next