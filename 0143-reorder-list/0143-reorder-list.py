class Solution:
    def reorderList(self, head):
        if not head or not head.next:
            return

        # Find middle
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        second = slow.next
        slow.next = None

        prev = None

        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        second = prev

        # Merge two halves
        first = head

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2