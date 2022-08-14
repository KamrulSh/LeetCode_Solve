# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        # iterative
        if not root:
            return None

        while (root != None):
            if root.val == val:
                return root
            elif val < root.val:
                root = root.left
            else:
                root = root.right

        return None
