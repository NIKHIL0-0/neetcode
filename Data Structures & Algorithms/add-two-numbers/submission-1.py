class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        temp = dummy
        carry = 0

        while l1 and l2:
            tot = l1.val + l2.val + carry

            if tot < 10:
                dummy.next = ListNode(tot)
                carry = 0
            else:
                carry = tot // 10
                dummy.next = ListNode(tot - (carry * 10))

            dummy = dummy.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            tot = l1.val + carry

            if tot < 10:
                dummy.next = ListNode(tot)
                carry = 0
            else:
                carry = tot // 10
                dummy.next = ListNode(tot - (carry * 10))

            dummy = dummy.next
            l1 = l1.next

        while l2:
            tot = l2.val + carry

            if tot < 10:
                dummy.next = ListNode(tot)
                carry = 0
            else:
                carry = tot // 10
                dummy.next = ListNode(tot - (carry * 10))

            dummy = dummy.next
            l2 = l2.next
        if carry:
            dummy.next=ListNode(carry)
            carry=0

        return temp.next