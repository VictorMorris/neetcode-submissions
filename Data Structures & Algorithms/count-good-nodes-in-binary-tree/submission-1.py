# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root: TreeNode, largest: int) -> int:

            if not root:
                return 0

            if root.val >= largest:
                largest = root.val
                return 1 + dfs(root.left, largest) + dfs(root.right, largest)
            else:
                return dfs(root.left, largest) + dfs(root.right, largest)

        return dfs(root, root.val)


        