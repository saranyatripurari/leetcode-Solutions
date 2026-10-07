# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        st=[]
        temp=head
        while temp!=None:
            st.append(temp.val)
            temp=temp.next
        temp=head

        while temp!=None:
            elem=st.pop()
            if temp.val!=elem:
                return False
            else:
                temp=temp.next
        return True