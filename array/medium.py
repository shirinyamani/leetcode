#Q1) three Sum 
class Solution(object):
    def threeSum(self, nums):
        if not nums: return None
        #STEP1: Sort + define a set to store the nums
        res = []
        nums.sort()
        set_num = set(nums)
        
        #STEP 2: define a l and r range
        for i in range(len(nums)):
            
            l, r = i + 1 , len(nums) - 1
            
            while l<r:
                sum_nums = nums[i] + nums[l] + nums[r]
                
                if sum_nums == 0:
                    res.append((nums[i], nums[l], nums[r]))
                    set_num.add((nums[l], nums[r]))
                    
                    l +=1
                    r -= 1
                    
                elif sum_nums < 0:
                    l +=1
                    
                else: r -= 1
                    
        return res
            
            
#Q2) longest palindrome
class Solution(object):
    def longestPalindrome(self, s):
        
        longest_palindrom = ''
        dp = [[0]*len(s) for _ in range(len(s))]
        #filling out the diagonal by 1
        for i in range(len(s)):
            dp[i][i] = True
            longest_palindrom = s[i]
			
        # filling the dp table
        for i in range(len(s)-1,-1,-1):
				# j starts from the i location : to only work on the upper side of the diagonal 
            for j in range(i+1,len(s)):  
                if s[i] == s[j]:  #if the chars mathces
                    # if len slicied sub_string is just one letter if the characters are equal, we can say they are palindomr dp[i][j] =True 
                    #if the slicied sub_string is longer than 1, then we should check if the inner string is also palindrom (check dp[i+1][j-1] is True)
                    if j-i ==1 or dp[i+1][j-1] is True:
                        dp[i][j] = True
                        # we also need to keep track of the maximum palindrom sequence 
                        if len(longest_palindrom) < len(s[i:j+1]):
                            longest_palindrom = s[i:j+1]
                
        return longest_palindrom

#Q3) Set Matrix Zeroes
class Solution(object):
    def setZeroes(self, matrix):
        r = len(matrix)
        c = len(matrix[0])  
        #to store the indicies
        rows ,cols = set(), set()    
        #STEP1: Go thro the row n col to see whether they include Zero; if yes, track them
        for i in range(r):
            for j in range(c):
                
                if matrix[i][j] == 0:
                    rows.add(i) #mark the cell as Has Zero
                    cols.add(j) #mark the cell azhas Zero
                    
        #STEP2: Go thro again to set the row n col which has a Zero to Zero            
        for i in range(r):
            for j in range(c):
                if i in rows or j in cols:
                    matrix[i][j] = 0

#Q4) Longest Substring Without Repeating Characters
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        longest = ""
        n_longest = 0
        
        for ch in s:
            if ch not in longest:
                longest += ch
            else:
                longest = longest.split(ch)[1] + ch
                
                n_longest = max(n_longest, len(longest))
                
        return n_longest           

#Q5) Longest Palindromic Substring
#solution 1
class Solution(object):
    def longestPalindrome(self, s):
        
        longest_palindrom = ''
        dp = [[0]*len(s) for _ in range(len(s))]
        #filling out the diagonal by 1
        for i in range(len(s)):
            dp[i][i] = True
            longest_palindrom = s[i]
			
        # filling the dp table
        for i in range(len(s)-1,-1,-1):
				# j starts from the i location : to only work on the upper side of the diagonal 
            for j in range(i+1,len(s)):  
                if s[i] == s[j]:  #if the chars mathces
                    # if len slicied sub_string is just one letter if the characters are equal, we can say they are palindomr dp[i][j] =True 
                    #if the slicied sub_string is longer than 1, then we should check if the inner string is also palindrom (check dp[i+1][j-1] is True)
                    if j-i ==1 or dp[i+1][j-1] is True:
                        dp[i][j] = True
                        # we also need to keep track of the maximum palindrom sequence 
                        if len(longest_palindrom) < len(s[i:j+1]):
                            longest_palindrom = s[i:j+1]
                
        return longest_palindrom
#solution 2: palindrome.py

#Q6) Increasing Triplet Subsequence
def increasingTriplet(nums):
    a=b= float('inf')
    for n in nums:
        if a<b<n:
            return True
        elif a<n:
            a=n
        elif a<n<b:
            b=n
    return False

#Q7) Missing ranges
def missingranges(nums, lower, upper):
    nums.append(upper+1)
    nums.insert(0,lower-1)
    res = []
    for i in range(len(nums)-1):
        if nums[i+1] - nums[i]>1:
            res.append(str(nums[i]+1)+'->'+str(nums[i+1]-1))
        elif nums[i+1]-nums[i]==1:
            res.append(str(nums[i]+1))
    return res

                    