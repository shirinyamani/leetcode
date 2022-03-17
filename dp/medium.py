from bisect import bisect_left
#Unique path
class Solution(object):
    def uniquePaths(self, m, n):
        if not m or not n:
            return 0
        
        dp = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
        return dp[-1][-1]
    
    
    
    
#Longest increasing SubSequence
def longestincreasingSub(nums): #O(n) 
    if not nums: 
        return 0
    
    dp = [1] * len(nums)  #initiate the array
    for i in range(1,len(nums)): #range full arr
        for j in range(i): #from start untill this point(i.e. left side!)
            if nums[i] > nums[j]: #if crr num bigger than nxt num
                dp[i] = max(dp[i], dp[j] +1) #Then we just want to check which is bigger, the current sequence or the nums sequence plus 1
    return max(dp)

def liSub1(nums):
    liSub1 = [1] * len(nums)
    for i in range(len(nums)-1, -1,-1):
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                liSub1[i] = max(liSub1[i], liSub1[j]+1)
    return max(liSub1) 

def lIS2(nums):
    sub = []
    for num in nums:
        i = bisect_left(sub,num) #binary search left side till this point return the position of that point
        if i == len(sub): #if its located at the end of the list
            sub.append(num)

        else: sub[i] = num #otherwise take it as a num then again search

    return len(sub)

#Longest SubSequence : 1)iterative 2)recurssive
def longestSubsequence1(txt1,txt2):
    dp = [[0 for i in range(len(txt2)+1)] for j in range(len(txt1)+1)]
    for i in range(len(txt1) -1, -1,-1): #end i indice of the matrix
        for j in range(len(txt2) -1,-1,-1): #end j indice of the matrix
            if txt1[i] == txt2[j]: #they have same charactor
                dp[i][j]= 1 + dp[i+1][j+1] #1 bc we have same chr in both
            else: dp[i][j]= max(dp[i][j+1], dp[i+1][j])# go to nxt cell in i n j
    return dp[0][0]