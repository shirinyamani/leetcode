### Binary Tree Max Path
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = float('-inf')
        self.helper(root)
        return self.res
        
    def helper(self, root):
        if root is None: return 0
        left , right = self.helper(root.left) , self.helper(root.right)
        self.res = max(self.res, root.val + left+ right)
        return max(root.val + max(left, right), 0)

### longest increasing path
def longestIncreasingPath(matrix):
    pass
