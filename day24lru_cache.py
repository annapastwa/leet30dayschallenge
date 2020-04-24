import collections


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dic = collections.OrderedDict()
        self.remain = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dic:
            return -1
        v = self.dic.pop(key)
        self.dic[key] = v  # set key as the newest one
        return v

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """

        if key in self.dic:
            self.dic.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1
            else:  # self.dic is full
                self.dic.popitem(last=False)
        self.dic[key] = value


# old code
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# cache = LRUCache(2)  # /* capacity */
# cache.put(1, 1)
# cache.put(2, 2)
# cache.get(1)  # returns 1
# cache.put(3, 3)  # evicts key 2
# cache.get(2)  # returns -1 (not found)
# cache.put(4, 4)  # evicts key 1
# cache.get(1)  # returns -1 (not found)
# cache.get(3)  # returns 3
# cache.get(4)  # returns 4
#
# print(cache.store)

#####

# cache = LRUCache(1)  # /* capacity */
# cache.get(0)  # returns 1
# print(cache.store)
# # ["LRUCache","get"]
# # [[1],[0]]
#
# cache = LRUCache(2)  # /* capacity */
# cache.put(2, 1)
# cache.put(2, 2)
# cache.get(2)  # returns 1
# cache.put(1, 1)
# cache.put(4, 1)
# cache.get(2)
# print(cache.store)

# Input:
# ["LRUCache","put","put","get","put","put","get"]
# [[2],[2,1],[2,2],[2],[1,1],[4,1],[2]]
# Output:
# [null,null,null,1,null,null,-1]
# Expected:
# [null,null,null,2,null,null,-1]

# cache = LRUCache(2)  # /* capacity */
# cache.get(2)  # returns 1
# cache.put(2, 1)
# cache.put(1, 1)
# cache.put(2, 3)
# cache.put(4, 1)
# cache.get(1)
# cache.get(2)
# print(cache.store)

# Input:
# ["LRUCache","get","put","get","put","put","get","get"]
# [[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]]
# Output:
# [null,-1,null,-1,null,null,2,-1]
# Expected:
# [null,-1,null,-1,null,null,2,6]

cache = LRUCache(2)  # /* capacity */
cache.put(2, 1)
cache.put(1, 1)
cache.put(2, 3)
cache.put(4, 1)
cache.get(1)  # returns 1
cache.get(2)
print(cache.get(2))
