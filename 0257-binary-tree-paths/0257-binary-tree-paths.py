# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        paths = []
        def helper(node, path):
            path.append(str(node.val))
            if not node.left and not node.right:
                paths.append("->".join(path))
            else:
                if node.left:
                    helper(node.left, path)
                if node.right:
                    helper(node.right, path)

            path.pop()
        helper(root, [])
        return paths
        