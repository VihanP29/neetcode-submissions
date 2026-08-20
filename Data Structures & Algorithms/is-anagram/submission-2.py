class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        map = [0]*26
        map2 = [0]*26
        for l in s:
            map[ord(l) - ord('a')]+=1
        for l in t:
            map2[ord(l) - ord('a')]+=1
        for l in s:
            if map[ord(l) - ord('a')] != map2[ord(l) - ord('a')]:
                return False

        return True



        

        