"""
O(log(n))
"""
class Solution:
   def hasCycle(self,head):
    clop1, clop2 = head, head
    while clop2 != None and clop2.next != None:
        clop1 = clop1.next
        clop2 = clop2.next.next
        if clop1 == clop2:
            return True
    return False