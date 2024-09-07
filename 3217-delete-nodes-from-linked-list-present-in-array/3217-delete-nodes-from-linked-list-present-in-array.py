# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
class Solution(object):
    def modifiedList(self, nums, head):
        set_of_nums=set(nums)
        dummy=ListNode(0)
        dummy.next=head
        
        prev=dummy
        curr=head
        while curr:
            if curr.val in set_of_nums:
                prev.next=curr.next
            else:
                prev=curr
            curr=curr.next
        return dummy.next     