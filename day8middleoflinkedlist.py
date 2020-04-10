# # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class LinkedList:
    def __init__(self, first, next=()):
        self.first = first
        self.next = next


def listToLinkedList(lst):
    assert len(lst) > 0
    if len(lst) == 1:
        return LinkedList(lst[0])
    else:
        return LinkedList(lst[0], listToLinkedList(lst[1:]))


class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        red = head
        green = head
        while green.next != None:
            red = red.next
            green = green.next
            if green.next == None:
                break
            green = green.next
        return red


def main():
    head = listToLinkedList([7, 6, 4, 3, 1])  # needs to be turned to linkedlist

    foo = Solution()
    print(foo.middleNode(head))


if __name__ == "__main__":
    main()
