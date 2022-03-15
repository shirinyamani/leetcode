#Search in a 2D Matrix
class Solution(object):
    def searchMatrix(self, matrix, target):
        if not len(matrix) or not len(matrix[0]):
            return False
        
        m, n = len(matrix) , len(matrix[0])
        
        #Start adaptive search from left bottom corner 
        
        x,y = m-1 , 0
        
        while True:
            
            if x < 0 or y >= n:
                break
                
            current = matrix[x][y]
            
            
            if target < current:
                #target is smaller ---> go up
                x -= 1
        
            elif target > current:
                #target is greater ----> go to right                
                y += 1
                
            else:  return True  #hit the target
            
        return False
                