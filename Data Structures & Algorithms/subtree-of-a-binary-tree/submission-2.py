# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True

        if not root:
            return False

        def isSame(rootNode, subNode):
            if not rootNode and not subNode:
                return True

            if rootNode and subNode and rootNode.val == subNode.val:
                return (isSame(rootNode.left, subNode.left) and isSame(rootNode.right, subNode.right))
            return False
                

        if isSame(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        