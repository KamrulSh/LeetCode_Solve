# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        values = []
        roots = [root]

        while (len(roots)):
            node = roots.pop(0)
            if k - node.val in values:
                return True
            values.append(node.val)
            if node.left != None:
                roots.append(node.left)
            if node.right != None:
                roots.append(node.right)

        return False
