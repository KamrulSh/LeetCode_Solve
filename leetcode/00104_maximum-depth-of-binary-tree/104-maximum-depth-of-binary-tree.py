# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # dfs
        if not root:
            return 0
        depth = 0
        current_node = [root]
        while current_node:
            stack = []
            depth += 1
            for node in current_node:
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)

            current_node = stack

        return depth
