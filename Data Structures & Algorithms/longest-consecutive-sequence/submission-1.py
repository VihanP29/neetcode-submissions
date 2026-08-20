class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numSet = set(nums)
        maxLen = 0

        for num in nums:
            if not num-1 in numSet:
                currLen = 1
                i = num
                while i+1 in numSet:
                    currLen+=1
                    i += 1
                if currLen > maxLen:
                    maxLen = currLen
        return maxLen

