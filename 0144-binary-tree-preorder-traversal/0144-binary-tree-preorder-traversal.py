# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def POT(self,root,l):
        if root==None:
            return 
        l.append(root.val)
        self.POT(root.left,l)
        self.POT(root.right,l)
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        l=[]
        self.POT(root,l)
        return l