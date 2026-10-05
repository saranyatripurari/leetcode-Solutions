# 234. Palindrome Linked List
# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

class Solution:
    def middleNode(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseList(self,head):
         prev = None # two vars None or prev both are same first node next none untundhiii 
         curr = head
         while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
         return prev
    def isPalindrome(self,head):
        middle=self.middleNode(head)
        right=self.reverseList(middle)
        left=head
        while right:
            if left.val != right.val:
                return False
            else:
              left = left.next
              right = right.next
        return True
        
