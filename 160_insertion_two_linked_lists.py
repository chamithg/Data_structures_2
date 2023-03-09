# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        A_arr = []
        B_arr = []

        while headA:
            A_arr.append(headA.val)
            headA= headA.next
        
        while headB:
            B_arr.append(headB.val)
            headB= headB.next

        mearge_point = 0
        print(A_arr)
        print(B_arr)

        for i in range(1,len(A_arr)):
            if A_arr[-i] == B_arr[-i]:
                mearge_point = A_arr[-i]
            else:
                print(mearge_point)
                return mearge_point
        
        
        
        