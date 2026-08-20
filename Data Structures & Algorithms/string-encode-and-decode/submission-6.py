class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        for item in strs:
            length = str(len(item))
            encodedStr += length
            encodedStr +="~"
            encodedStr += item
        return encodedStr
    def decode(self, s: str) -> List[str]:
        decodedArr = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '~':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            decodedArr.append(s[i:j])
            i = j
        return decodedArr

