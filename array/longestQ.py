#Longest SubString
from bisect import bisect, bisect_left


def longestsubstring(words):
    longest =""
    n_longest=0
    for chr in words:
        if chr not in longest: #if the chr not in the longest str
            longest += chr #add it
        else: longest = longest.split(chr)[1]+chr #split the same chr in first position then concate the char to it
        n_longest= max(n_longest, len(longest)) #het the max len
    return n_longest

#Longest SubSequence : 1)iterative 2)recurssive
def longestSubsequence1(txt1,txt2):
    dp = [[0 for i in range(len(txt2)+1)] for j in range(len(txt1)+1)]
    for i in range(len(txt1) -1, -1,-1): #end i indice of the matrix
        for j in range(len(txt2) -1,-1,-1): #end j indice of the matrix
            if txt1[i] == txt2[j]: #they have same charactor
                dp[i][j]= 1 + dp[i+1][j+1] #1 bc we have same chr in both
            else: dp[i][j]= max(dp[i][j+1], dp[i+1][j])# go to nxt cell in i n j
    return dp[0][0]

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



if __name__ =="__main__":
   # print(longestincreasingSub([10,9,2,5,3,7,101,18]))
    #print(liSub1([43,0,5,-1,3,45]))
     print(lIS2([8,-1,4,0,65,0,88]))