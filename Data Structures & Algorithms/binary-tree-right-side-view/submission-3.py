# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ln = []
        q = deque([root])

        
        while q:
            level = []
            for _ in range(len(q)):
                h = q.popleft()

                level.append(h.val)
                if h.left:
                    q.append(h.left)
                if h.right:
                    q.append(h.right)
            ln.append(level)
        res = []
        for i, nums in enumerate(ln):
            res.append(nums[-1])

        return res