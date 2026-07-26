class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hm = {}
        for str in strs:
            str_lst = [0] * 26
            for char in str:
                pos = ord(char) - ord('a')
                str_lst[pos] += 1
            str_lst = tuple(str_lst)
            lst = hm.get(str_lst, [])
            lst.append(str)
            hm[str_lst] = lst

        res = []
        for val in hm.values():
            res.append(val)
        return res