import collections
import enum
from palindrome import Solution

#sum of three numbers equal to zero 
#LESSON1: define an empty set/list when ya wanna build a new
#LESSON2: use a set to store the numbers
#LESSON3: use list(i) to convert a set to a list
def threeSum1(num):
    num.sort()
    set_num= set()
    for i in range(len(num)):
        l,r=i+1,len(num)-1
        while l<r:
            sum_num= num[i]+num[l]+num[r]
            if sum_num ==0:
                set_num.add((num[i],num[l],num[r])) #be ja print
                l+=1
                r-=1
            elif sum_num<0:
                l +=1
            else:
                r-=1
    return [list(i) for i in set_num]

def groupAnagrams(words):
        anagram = collections.defaultdict(list)
        for word in words:
            key = "".join(sorted(word))
            anagram[key].append(word)
        return anagram.values()
            
def groupAnagram1(arr):
    anagram ={}
    for word in arr:
        sorted_word = "".join(sorted(word))
        if word in anagram:
            anagram[sorted_word].append(word)
    return anagram.values()

#find the longest substring of a list of strings
#LESSON1:when ya wan the longest len, ya can either compare with 0 or use Max
def longestsubstring(s):
    longest=""
    top=0
    for i in s:
        if i not in longest:
            longest +=i
        else:
            longest= longest.split(i)[1]+i
        if len(longest)>top:
            top=len(longest)
    return top

#only longest substring
def longestSubstring2(s):
    longest=""
    len_longest=0
    for i in s:
        if i not in longest:
            longest += i
        else: longest = longest.split(i)[1] + i
        len_longest = max(len_longest, len(longest))
    return len_longest

#find the longest palindrome in a string
s = Solution()
print( s.longestpalindrome("babad"))

#valid palindrome no spaces, punctuation
def validPalindrome(s):
    s ="".join(i for i in s.lower() if i.isalnum())
    if s == s[::-1]:
        return True
    else: False

#find missing range of numbers in a list
def missingRanges(nums, lower, upper):
    nums.append(upper+1) #append upper+1 to nums
    nums.insert(0,lower-1) # add lower and upper to the list
    res=[]
    for i in range(len(nums)-1):
        if nums[i+1]-nums[i]>1:
            res.append(str(nums[i]+1)+"->"+str(nums[i+1]-1))
        elif nums[i+1]-nums[i]==1:
            res.append(str(nums[i]+1))
    return res

#find first unique characters
def firstuniqchar(s):
    count = collections.Counter(s)
    for idx, char in enumerate(s):
        if count[char] == 1:
            return idx

#find the increasing triplet subsequence
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


def longestconsecutive(nums):
    pass









if __name__ == "__main__":
    #print(increasingTriplet([0,-1,3,-50,20]))
    #print(threeSum1([1]))
    #print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(longestSubstring2("abbbbcdddee"))