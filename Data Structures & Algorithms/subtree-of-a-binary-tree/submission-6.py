# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        l1 = self.serialize(root)
        l2 = self.serialize(subRoot)

        return l2 in l1
    def serialize(self, root):
        res = []
        self.dfs(root, res)
        return "".join(res)


    def dfs(self, root, res):

        if not root:
            res.append(",#")
            return 
        
        res.append(",V" + str(root.val))

        self.dfs(root.left,res)
        self.dfs(root.right,res)
