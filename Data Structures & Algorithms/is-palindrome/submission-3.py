class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip().lower()
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i].lower().isalnum():
                if s[j].lower().isalnum():
                    if s[i] != s[j]:
                        return False
                    else:
                        i+=1
                        j-=1
                else:
                    j-=1
            else:
                i+=1
        return True
        
        

        