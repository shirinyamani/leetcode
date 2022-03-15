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

class Solution(object):
    def alienOrder(self, words):
        adj = {c:set() for w in words for c in w} # build graph for all adjacent nodes: for words in list of the words n for each charactor in those words
        for i in range(len(words) - 1): #go thro every pair of the words
            w1 , w2 = words[i] , words[i+1] #create the pair 
            minlen = min(len(w1), len(w2)) #find the min length of the two words for the edge cases
            if len(w1) > len(w2) and w1[:minlen] == w2[:minlen]: #if the prefixes exact same, e.g; 'abc' and 'abd'
                return "" #return empty string
            for j in range(minlen): #then if its not the case then we will go thro every single charactor
                if w1[j] != w2[j]:# goal is to find the first different charactor
                    adj[w1[j]].add(w2[j]) #word 1 is the key(come before word 2) and word 2 is the value(come after word 1)
                    break #break out of the loop

        visited ={} #False: not visited, True: visited
        res = [] #all we need to do is to passing the visited nodes to the result list
        def dfs(c):
            if c in visited: return visited[c] #if the node is visited, return the visited value
            visited[c] = True

            for nei in adj: #go for every charactor "after" the current char
                if c in adj[nei]: #if the current char is in the adj list of the nei
                    if not dfs(nei): #run dfs on it and if it is false
                        return True
                visited[c] = False #if it is false
                res.append(c) #append the current char to the result list
        for c in adj:
            if dfs(c):
                return "" #if there is a cycle, return empty string
        res.reverse() #reverse the result list
        return "".join(res) #return the result list
                    

