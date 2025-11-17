# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        result = []
        q.append(root)

        while q:
            size_o_q = len(q)
            current_level = []
            for i in range(0, size_o_q, 1):
                popped = q.popleft()
                current_level.append(popped.val)
                if popped.left:
                    q.append(popped.left)
                if popped.right:
                    q.append(popped.right)
            result.append(current_level)
        return result


        