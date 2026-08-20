class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for i in range(len(strs)):
            key = [0] * 26
            for j in strs[i]:
                key[ord(j) - ord('a')] += 1
            map[tuple(key)].append(strs[i])
        return list(map.values())

        