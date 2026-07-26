class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        mag_hm = {}
        for char in magazine:
            mag_hm[char] = mag_hm.get(char, 0) + 1

        for char in ransomNote:
            if mag_hm.get(char, 0) == 0:
                return False
            mag_hm[char] -= 1
        return True