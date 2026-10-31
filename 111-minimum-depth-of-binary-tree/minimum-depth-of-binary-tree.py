# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        
        # If there is no left child, we must check the right subtree path
        if root.left is None:
            return 1 + self.minDepth(root.right)
            
        # If there is no right child, we must check the left subtree path
        if root.right is None:
            return 1 + self.minDepth(root.left)
            
        # If both children exist, take the minimum of both paths
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
