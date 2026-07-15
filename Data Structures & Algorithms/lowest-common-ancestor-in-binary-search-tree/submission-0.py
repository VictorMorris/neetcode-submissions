# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root.val == p.val or root.val == q.val:
            return root
            
        leftContainsP, rightContainsP = self.containsNode(root.left, p), self.containsNode(root.right, p)
        leftContainsQ, rightContainsQ = self.containsNode(root.left, q), self.containsNode(root.right, q)

        if (leftContainsP and rightContainsQ) or (rightContainsP and leftContainsQ):
            return root
        elif (leftContainsP and leftContainsQ):
            return self.lowestCommonAncestor(root.left, p, q)
        elif (rightContainsP and rightContainsQ):
            return self.lowestCommonAncestor(root.right, p, q)
        
        
    def containsNode(self, root: TreeNode, node: TreeNode) -> Boolean:
        if root == None:
            return False
        elif root.val == node.val:
            return True
        else:
            return self.containsNode(root.left, node) or self.containsNode(root.right, node)