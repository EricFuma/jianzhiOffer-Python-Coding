# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        # 方法2： 栈
        # 注意，栈比函数递归快得多
        stack, res = [], []
        while head:
            stack.append(head.val)
            head = head.next
        while stack:
            res.append(stack.pop())
        return res

        # 方法1： 递归
        '''
        if head == None:
            return []
        return self.reversePrint(head.next) + [head.val]
        '''
