#In order Traversal
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        val = self.val
        left= self.left
        right = self.right
    #recurrsivel
    def inorder(self,root): #visit the left ---> root ---> right
        res = []
        self.helper(root, res)
        return res

    def helper(self,root,res):
        if root:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right, res)

    #iteratively #use stack 
    def inorder1(self, root):
        res, stack = [],[]
        while True:
            while root:
                stack.append(root)
                root = root.left

            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right            

# ZigZag Level Order
    def zigzaglevelorder(self,root):
        curr_level, nxt_level = [],[]
        lefttoright = True
        curr_level.append(root)

        while len(curr_level) >1:
            temp = curr_level.pop(-1)
            if lefttoright:
                if temp.left:
                    nxt_level.append(temp.left)
                if temp.right:
                    nxt_level.append(temp.right)
            else:
                if temp.right:
                    nxt_level.append(temp.right)
                if temp.left:
                    nxt_level.append(temp.left)

        if len(curr_level) == 0:
            lefttoright = not lefttoright
            curr_level, nxt_level = nxt_level, curr_level

#build tree from in-order and pre-order
    def buildtree(self, preorder, inorder):
        if not preorder or inorder:
            return None
        root = TreeNode(preorder[0])
        root_index = inorder.index(preorder[0])
        #from inorder, we wanna all the nodes to the left/right the root
        #from preorder, we want all the node that can potentially become a root!
        root.left = self.buildtree(preorder[1:root_index+1], inorder[:root_index])
        root.right = self.buildtree(preorder[root_index+1:],inorder[root_index+1:]) 

        return root


