# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        res = []

        while q:
            level = []

            for _ in range(len(q)):
                h = q.popleft()

                level.append(h.val)
                if h.left:
                    q.append(h.left)
                if h.right:
                    q.append(h.right)
            
            res.append(level)
        return res


