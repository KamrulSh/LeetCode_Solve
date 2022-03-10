# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return

        postorder = []
        nodeStack = []
        nodeStack.append(root)

        while nodeStack:

            node = nodeStack.pop()
            postorder.append(node.val)

            if node.left:
                nodeStack.append(node.left)
            if node.right:
                nodeStack.append(node.right)

        postorder = postorder[::-1]
        return postorder
