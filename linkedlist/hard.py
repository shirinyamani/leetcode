#Hard

#Merge K list
class Solution():
    def mergeklists(self, lists): #idea of merge sort! break then compare each section
        if not lists:
            return None 

        if len(lists) == 1:
            return lists[0]
        
        mid = len(lists) // 2

        l, r = self.mergeklists(lists[:mid]), self.mergeklists(lists[mid:])

        return self.merge(l,r)

    def merge(l1,l2): #merge 2 lists 
        dummy = cur = ListNode()

        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next

            cur = cur.next
            cur.next = l1 or l2

        return dummy.next