# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        l = []

        self.dfs(root, root.val,l)
        return len(l)
        
    def dfs(self, root, max_num, l):
        if not root:
            return 
        if root.val >= max_num:
            max_num = root.val
            l.append(root)
        
        if root.right:
            self.dfs(root.right, max_num,l)
        if root.left:
            self.dfs(root.left, max_num,l)

            
