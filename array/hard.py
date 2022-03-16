#product array except self
def productExceptSelf(nums):
    p = 1
    n = len(nums)
    output = []
    for i in range(0,n):
        output.append(p)
        p = p * nums[i]
    p = 1
    for i in range(n-1,-1,-1):
        output[i] = output[i] * p
        p = p * nums[i]
        print(p)
    return output

#First Missing Positive
def firstmissingPositive(nums):
    def swap(nums,i,j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    for i in range(len(nums)):
         #Check: 1) num is greter than 1; 2)num is in range of the nums 3) not equal to the nex num; if yes then swap
        while nums[i] > 0 and nums[i] <=len(nums) and nums[nums[i]- 1] != nums[i]:
            swap(nums, i, nums[i]-1)
    
    for i in range(len(nums)):
        if nums[i] != i+1:
            return i+1

    return len(nums)+1

#Longest Consecutive Sequence
def longestConsecutive(nums):
    longest_streak=0 #for comparison purpose
    for num in nums:
        current_num = num 
        current_streak=1
        
        while current_num+1 in nums: #as long as nxt num is in the seq
            current_num +=1 #go to nxt num
            current_streak +=1 #extend the seq space
            longest_streak = max(current_streak, longest_streak) 
    return longest_streak

#Longest Consecutive Sequence
def longestConsecutive2(nums):
    longest_streak = 0
    set_num = set(nums)

    for num in set_num:
        if num-1 not in set_num: #take the current num in hand n check the prev
            current_num = num
            current_streak = 1

            while current_num+1 in set_num: #if nxt num in the set then
                current_num +=1 #go to next num 
                current_streak +=1 #extend the streak

                longest_streak= max(current_streak, longest_streak)
    return longest_streak     

class Solution(object):
    def spiralOrder(self, matrix):
        if matrix == []:
            return matrix
        
        l = 0
        r = len(matrix[0]) - 1
        t = 0 
        b = len(matrix) - 1
        
        res = []
        
        while l < r and t < b: #start move in 4 directions
            
            #top
            for i in range(l,r):
                res.append(matrix[t][i])
            
            #right
            for i in range(t,b):
                res.append(matrix[i][r])
                
            #bottom
            for i in range(r,l,-1):
                res.append(matrix[b][i])
                
            #left
            for i in range(b,t,-1):
                res.append(matrix[i][l])         
            l +=1
            r -=1
            b -=1
            t +=1
        
        #vertical line
        if l == r:
            for i in range(t, b+1):
                res.append(matrix[i][l])
        elif t == b:
            for i in range(l, r+1):
                res.append(matrix[t][i])
                
        return res

#Find Duplicate num
class Solution(object):
    def findDuplicate(self, nums):
        left = 1
        right = len(nums) -1
        
        while left <= right:
            mid = (left + right) // 2
            count = 0
            
            #calculate the nums of repetative nums
            count = sum(num <= mid for num in nums)
            if count > mid:
                duplicate = mid
                right = mid - 1
                
            else:
                left = mid +1
            
        return duplicate
        


if __name__ == "__main__":
    print(productExceptSelf([1,2,3,4]))