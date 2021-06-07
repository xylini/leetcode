from __future__ import annotations
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def fromList(l: List[int]):
        l: List[ListNode] = list(map(lambda x: ListNode(x), l))

        # The last element should point to None
        for i in range(len(l) - 1):
            l[i].next = l[i + 1]
        return l[0]

    @staticmethod
    def asList(listNode: ListNode):
        head = listNode
        l = []
        while head is not None:
            l.append(head.val)
            head = head.next

        return l


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head: ListNode = ListNode()
        tmp = 0
        l3 = head

        while l1 and l2:
            tmp = tmp + l1.val + l2.val
            l3.next = ListNode(tmp % 10)
            tmp = tmp // 10
            l1 = l1.next
            l2 = l2.next
            l3 = l3.next

        while l1:
            tmp += l1.val
            l3.next = ListNode(tmp % 10)
            tmp = tmp // 10
            l1 = l1.next
            l3 = l3.next

        while l2:
            tmp += l2.val
            l3.next = ListNode(tmp % 10)
            tmp = tmp // 10
            l2 = l2.next
            l3 = l3.next

        while tmp != 0:
            l3.next = ListNode(tmp % 10)
            tmp = tmp // 10
            l3 = l3.next

        return head.next


def main():
    testCases = [(
        [2, 4, 3],
        [5, 6, 4]
    ), (
        [0],
        [0]
    ), (
        [9, 9, 9, 9, 9, 9, 9],
        [9, 9, 9, 9]
    )]

    for test in testCases:
        print(
            ListNode.asList(
                Solution().addTwoNumbers(
                    ListNode.fromList(test[0]),
                    ListNode.fromList(test[1])
                )
            )
        )


if __name__ == '__main__':
    main()
