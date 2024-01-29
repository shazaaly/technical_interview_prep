# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        curr = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        if list1:
                curr.next = list1
        if list2:
                curr.next = list2
        return dummy.next
            


# curr.next = list1: This line sets the next pointer 
# of the current node (pointed by curr) to the next node in list1.
# In other words, 
# it connects the current node in the merged list to the next node in list1.

# list1 = list1.next: This line moves the list1 
# pointer to the next node in list1.
# It updates the list1 pointer to point to the
# next node in the original list1 linked list.

   


        
        