class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashlist = set()
        for num in nums:
            if num in hashlist:
                return True
            hashlist.add(num)
        return False

        