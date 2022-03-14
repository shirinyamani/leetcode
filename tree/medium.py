import collections
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

### Number of islands
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
# Recurssive
        
        islands = 0
        for r,row in enumerate(grid): #iterate through all the rows
            for c, col in enumerate(row): #c for the rows
                if grid[r][c] == "1": 
                    self.helper(r,c, grid)
                    islands +=1 #add to the num of island
                    
        return islands
    
    def helper(self, r,c,grid):
        grid[r][c] = 0 #start by the first element then go in all 4 directions! 
        #then check whether in any of those dirctions we have 1, if yes then call the helper func n add it to the islands
        
        if r+1 < len(grid) and grid[r+1][c] == "1": 
            self.helper(r+1,c, grid)
        if c+1 < len(grid[0]) and grid[r][c+1] == "1":
            self.helper(r, c+1, grid)       
        if r-1 >=0 and grid[r-1][c] == "1":
            self.helper(r-1,c,grid)
        if c-1 >=0 and grid[r][c-1] == "1":
            self.helper(r,c-1,grid)
        
# Iterative
        if not grid: return 0
        rows , cols = len(grid), len(grid[0]) #define the rows n cols
        visited = set() #the visited cell 
        islands = 0 #numb of islands
        
        def bfs(r,c):
            q = collections.deque() #for bfs we use que
            visited.add((r,c)) #add the r, c to visited
            q.append((r,c)) #add the r ,c to our que
            
            while q:
                row, col = q.popleft() #while q is not empty, expand the island
                directions = [[1,0], [-1,0], [0,1], [0,-1]] #define left/right/up/bottom directions
                
                for dr, dc in directions: #check all these directions
                    r, c = row + dr, col + dc
                    if (r in range(rows) and #check whether its balanced
                        c in range(cols) and
                        grid[r][c] == "1" and #this position is a land position
                        (r, c) not in visited):
                        
                        q.append((r,c)) #add it to our iland
                        visited.add((r, c))
                
        for r in range(rows): #iterate through rows
            for c in range(cols): #iterate through cols
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands +=1
                    
        return islands