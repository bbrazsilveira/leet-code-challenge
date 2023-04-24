import math
from typing import Optional


class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    sum_list_node: Optional[ListNode] = None
    current_sum_list_node: Optional[ListNode] = None
    additional_sum = 0

    while True:
        sum_ = l1.val + l2.val + additional_sum
        val = sum_ % 10
        additional_sum = math.floor(sum_ / 10)

        l_sum = ListNode(val)
        if sum_list_node is None:
            sum_list_node = l_sum
        else:
            current_sum_list_node.next = l_sum

        current_sum_list_node = l_sum

        if l1.next is None and l2.next is None and additional_sum == 0:
            return sum_list_node

        l1 = l1.next if l1.next is not None else ListNode(0)
        l2 = l2.next if l2.next is not None else ListNode(0)


result = add_two_numbers(l1=ListNode(8, ListNode(3, ListNode(2))), l2=ListNode(9, ListNode(2, ListNode(1))))
print(result)
