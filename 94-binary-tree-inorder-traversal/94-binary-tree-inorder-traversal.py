# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        inorder = []
        nodeStack = []
        current = root
        
        while True:
            if current is not None:
                nodeStack.append(current)
                current = current.left
                
            elif nodeStack:
                current = nodeStack.pop()
                inorder.append(current.val)
                current = current.right
            else:
                break
                
        return inorder