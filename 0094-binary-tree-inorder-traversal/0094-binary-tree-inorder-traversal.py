# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        def inorder_dfs(root):
            if not root:
                return
            inorder_dfs(root.left)
            arr.append(root.val)
            inorder_dfs(root.right)
        inorder_dfs(root)
        return arr