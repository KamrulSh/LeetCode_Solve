# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return

        output = []
        current_level = [root]

        while current_level:
            next_level = []
            cur_nodes = []

            for node in current_level:
                cur_nodes.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            output.append(cur_nodes)
            current_level = next_level

        return output
