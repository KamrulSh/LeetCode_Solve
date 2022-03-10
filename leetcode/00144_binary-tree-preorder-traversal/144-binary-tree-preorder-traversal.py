# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        preorder = []
        if not root:
            return

        nodeStack = []
        nodeStack.append(root)

        while nodeStack:
            node = nodeStack.pop()
            preorder.append(node.val)

            if node.right is not None:
                nodeStack.append(node.right)
            if node.left is not None:
                nodeStack.append(node.left)

        return preorder
