import sys

def maxDepth(root):
    if root is None:
        return -1
    else:
        ldep = maxDepth(root.left)
        rdep = maxDepth(root.right)

    return 1+ (max(ldep,rdep))

class Solution(object):
##First Solution
    def validBST1(self,root):
        return self.valid(root, -sys.maxsize, sys.maxsize)


    def valid(self,root, l, r):
        if not root:
            return True
        if not (l < root.val < r):
            return False
        return self.valid(root.left,l, root.val) and self.valid(root.right, r, root.val)

### Second Solution
    def validBST2(self, root):
        res = []
        self.dfr(root,res)
        for i in range(len(res)):
            if res[i] >= res[i+1]:
                return False
        return True 


    def dfs(self, root, res):
        if root:
            self.dfs(root.left,res)
            res.append(root.val)
            self.dfs(root.right, res)

#here the ans is the node values that we wanna have and level is the level of each node series
#the idea is keep appending the values of each level then update the level 
# with all the nodes in the next level (kids) until it reaches an empty level
def levelOrder1(root): 
                    
    ans, level = [], [root]
    while root and level:
        ans.append([node.val for node in level])
        level = [kid for n in level for kid in (n.left, n.right) if kid]
    return ans

class TreeNode(object):
    def __init__(self,val=0, left=None, right=None):
        val = self.val
        right = self.right
        left = self.left
        
#idea is just Get the Middle of the array and make it root.
# and Recursively do same for left half and right half.
    def convertArraytoBST(self, nums):
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.convertArraytoBST(nums[:mid])
        root.right = self.convertArraytoBST(nums[mid+1:])
        return root 





if __name__ == '__main__':
    print(maxDepth([3,9,20,None, None, 15,7]))
    print(TreeNode.convertArraytoBST([-10,-3,0,5,9]))