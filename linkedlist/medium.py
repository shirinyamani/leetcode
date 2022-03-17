#add two num
from cgitb import reset


def add(l1,l2):
    dummy = cur = l1[0]
    carry = 0

    while l1 or l2 or carry:
        if l1:
            carry += l1.val
        if l2:
            carry +=l2.val

        carry.next = l1[carry%10]
        carry //= 10

    return dummy.next

#intersection 2 lists
def intersect(headA,headB):
    if headA is None or headB is None:
        return None
    
    A = headA
    B = headB

    while A is not B:
        A = headB if A is None else A.next
        B = headA if B is None else B.next

    return A 






