##find duplication
from typing import Counter
def findDuplication(nums):
    a = set(nums) #yani tekrari nadare
    if len(a) != len(nums): #agar len mosavi nabashe yani tek dare!
        return True
    else: False    
#find Duplicated number and return it!
#Solution1
def FindDuplicatedNum(nums):
    k = sorted(nums) #vase in k adad tekraria biad kenare ham
    return [i for i, j in zip(k, k[1:]) if i == j][0] 
    #zip mikoni, uni k ezafas mimune va adade tekrari ro mikhay
#Solution2
def FinduplicatedNum2(nums):
    a = Counter(nums)
    for i in a:
        if a[i]>1: #age indexesh>1 yani tekrar shode!
            return i

def FinduplicatedNum3(nums):
    a = Counter(nums)
    return [i for i in a if a[i]>1] 


##find missing
def FindMissing(nums): 
    return [i for i in range(len(nums) +1) if i not in nums]

#Solution 1
def FindPositiveMissing1(nums):
    #start nums from 1 (ignore - & 0)
    smallest = 1
    #no repeated
    n = set(nums)
    while True:
        #IF its in the array, then try the nxt possitive
        if smallest in n:
            smallest = smallest + 1
        else: #if not in array!
            return smallest 

def FindPossitiveMissing2(nums):
    i = 0
     # Cyclic Sort by ignoring numbers which are less then 1 or greater than or equalt to length of array. This is done because cyclic sort sorts an array in o(n) iff numbers are in a proper range.
    while i < len(nums):
            correct = nums[i] - 1
            if nums[i] <= 0 or nums[i] > len(nums) or nums[i] == nums[correct]:
                i += 1
            else:
                nums[i], nums[correct] = nums[correct], nums[i]
                
		# Now if at any index i the number present is not equal to i+1 then return i+1
    for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
		# If all the numbers in the range are already in the array then just return the next number
    return len(nums) + 1




if __name__ == '__main__':
    print(findDuplication([1,3,4,2,2]))
    print(FindDuplicatedNum([1,3,4,7,5,3]))
    print(FinduplicatedNum3([1,3,4,7,5,3,7]))
    print(FindMissing([0,1,2,4,5,6,8]))
    print(FindPossitiveMissing2([0,1,2]))