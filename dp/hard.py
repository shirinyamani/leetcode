#Max Product subarray
class Solution(object): #using Kadane Algo: get the max sum btween the current num index and the prev ones
    def maxProduct(self, nums):
        if len(nums) == 0: #edge case
            return 0 
        max_pro, min_pro = nums[0], nums[0] #start from the first num
        
        result = max_pro #store the max es of the nums in result
        
        for i in range(1, len(nums)): #1 cuz the first num is already done the max between itself n itself
            current = nums[i] #current num index
            temp_max = max(current, current*max_pro, current*min_pro)
            min_pro = min(current, current*max_pro, current*min_pro)
            max_pro = temp_max
            
            result = max(result, max_pro)
            
        return result
            