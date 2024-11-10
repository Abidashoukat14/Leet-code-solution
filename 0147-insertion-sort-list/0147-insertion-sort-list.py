# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        res=[]
        current =head
        while current:
            res.append(current.val)
            current = current.next
        for i in range(1,len(res)):
            cur_val = res[i]
            j = i-1 
            while j>=0 and res[j] > cur_val:
                res[j+1]=res[j]
                j-=1
            res[j+1]=cur_val
        current = head
        for i in range(len(res)):
            current.val=res[i]
            current=current.next
        return head    



        