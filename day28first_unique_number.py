import collections


class FirstUnique(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """

        self.queue = []
        self.dicnums = {}
        for i in nums:
            self.add(i)


    def showFirstUnique(self):
        """
        :rtype: int
        """
        while len(self.queue) > 0 and self.dicnums[self.queue[0]] > 1:
            self.queue.pop(0)
        if len(self.queue) == 0:
            return -1
        else:
            return self.queue[0]

    def add(self, value):
        """
        :type value: int
        :rtype: None
        """
        if value in self.dicnums:
            self.dicnums[value] += 1
        else:
            self.dicnums[value] = 1
            self.queue.append(value)


