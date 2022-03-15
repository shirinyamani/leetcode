import heapq
from heapq import heappop, heappush

class Solution(object):
    def topKFrequent(self, nums, k):
        if len(nums) == 1:
            return [nums[0]]      
        #step 1: build a dic {num:feq}
        d = {}      
        for num in nums:
            if num in d:
                d[num] += 1 #if its already in the dic, then add to it frequency
            else: d[num] = 1           
        #step 2: build a heap of the most freq elements
        h = []
        for key in d:
            heappush(h, (d[key], key)) #freq - element
            if len(h) > k:
                heappop(h)  #if the heap is larger than k, then pop the smallest element       
        #step 3: store the results in an array
        res = []
        while h:
            freq, item = heappop(h)
            res.append(item)
        return res

#Find kth largest element   
class Solution(object):
    def findKthLargest(self, nums, k):
        
#Approach 1: using a Heap
        pq = nums[:k] #priority que to store the largest elements
        heapq.heapify(pq)
        for x in nums[k:]:
            heapq.heappush(pq, x) #keep pushing the elements in the pq
            heapq.heappop(pq) #pop out the smallest element from the que

        return pq[0] #cuz we added from the largest to smallest

        
#Approach 2: Using a quick search method
        
        if not nums: return 
        p = random,choice(nums)
        l, m , r = [x for x in nums if x > p], [x for x in nums if x == p], [x for x in nums if x < p ]
        nums, i ,j = l+m+r , len(l), len(l) + len(m)
        
        return findKthLargest(nums[:i], k) if k<= i else findKthLargest(nums[j:] ,k) if k < j-1 else nums[i]
    
    