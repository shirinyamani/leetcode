#Easy
#remove nth node from a linkedlist 
from multiprocessing import dummy
from xml.dom.minicompat import NodeList


def removeNode(head,n):
    fast = slow = head
    for _ in range(n):
        fast = fast.next
    if not fast:
        return head.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    #delete nxt node
    slow.next = slow.next.next
    return head

#reverse a linkedlist
def reversell(head):
    prev = None
    crr = head
    while crr is not None:
        next = crr.next  #before changing the nxt node, store the crr node
        crr.next = prev  #now change the nxt of crr to prev for reverse purpose

        prev = crr #Move prev and curr one step forward 
        crr = next 

        head = prev
    return head

#Merge two sorted list into 1 LinkedList
def mergell(l1,l2):
    dummy = cur = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        elif l1.val > l2.val:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next

def isPalidrome(head): 
    fast = slow = head #initiate the pointers from head
    rev = None #if we devide the list, if the reverse of 1st half is equal to the 2nd half, then we have a Palinfrom
    while fast and fast.next:
        fast = fast.next.next #fast pointer 2 node ahead, when reaches the end, slow is in middle!
        rev, rev.next, slow = slow, rev, slow.next
    if fast: #fast at the end, move slow one step further
        slow = slow.next
    #compare the reversed first halp w/ the secont half
    while rev and rev.val == slow.val:
        slow = slow.next
        rev= rev.next
    #True if equal otherwise, False
    return not rev

def isPalidrome1(head):
    stack = []

    while head:
        stack.append(head.val)
        head = head.next

    return stack == stack[::-1]

#determine if a list has a cylcle in it 
def hasCycle(head):
    try:
        slow = head
        fast= head.next

        while slow is not fast:
            slow = slow.next
            fast = fast.next.next
        return True
    except:

        return False

def hasCycle1(head):
    if not head:
        return False
    slow = head
    fast= head.next

    while slow != fast:
        if not fast or not fast.next:
            return False
        slow= slow.next
        fast=fast.next.next
    return True

if __name__ == "__main__":
    #print(removeNode([34,5,6,-7,1], 3))
    #print(mergell([1,2,4,8],[-1,3,4,6]))
    print(isPalidrome1([1,2,3,3,2,1]))