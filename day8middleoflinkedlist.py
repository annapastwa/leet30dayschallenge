# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

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
    head = [7, 6, 4, 3, 1] # needs to be turned to linkedlist

    foo = Solution()
    print(foo.middleNode(head))


if __name__ == "__main__":
    main()