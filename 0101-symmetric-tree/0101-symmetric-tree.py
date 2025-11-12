# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        left_tree = root.left
        right_tree = root.right

        def left_inorder_traversal(node):
            if not node:
                return [None]
            return [node.val] + left_inorder_traversal(node.left) + left_inorder_traversal(node.right)
        
        def right_inorder_traversal(node):
            if not node:
                return [None]
            return [node.val] + right_inorder_traversal(node.right) + right_inorder_traversal(node.left)

        return right_inorder_traversal(right_tree) == left_inorder_traversal(left_tree)