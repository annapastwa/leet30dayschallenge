class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for word in sorted(strs):
            key = "".join(sorted(word))
            dic[key] = dic.get(key, []) + [word]
        return dic.values()


def main():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

    foo = Solution()
    print(foo.groupAnagrams(strs))



if __name__ == "__main__":
    main()