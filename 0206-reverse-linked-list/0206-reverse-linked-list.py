# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        
        st=[]
        temp=head
        while temp!=None:
            st.append(temp.val)
            temp=temp.next

        temp=head
        while temp!=None:
            temp.val=st.pop()
            temp=temp.next
        return head