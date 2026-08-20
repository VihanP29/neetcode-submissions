class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [0]*len(nums)
        suff = [0]*len(nums)
        res = [0]*len(nums)
        pref[0] = 1
        suff[len(nums)-1] = 1
        count = 1
        for i in range(1, len(nums)):
            count = nums[i-1] * count
            pref[i] = count
        count = 1
        for i in range(len(nums)-2, -1, -1):
            count = nums[i+1] * count
            suff[i] = count
        for i in range(len(nums)):
            res[i] = pref[i]*suff[i]
        return res