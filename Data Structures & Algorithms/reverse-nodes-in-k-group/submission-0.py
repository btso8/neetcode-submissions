# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupprev = dummy
        while True:
            kth = self.getKth(groupprev, k)
            if not kth:
                break
            groupnext = kth.next
            previous = kth.next
            current = groupprev.next
            while current != groupnext:
                temp = current.next
                current.next = previous
                previous = current
                current = temp
            temp = groupprev.next
            groupprev.next = kth
            groupprev = temp
        return dummy.next
    
    def getKth(self, current, k):
        while current and k > 0:
            current = current.next
            k -= 1
        return current